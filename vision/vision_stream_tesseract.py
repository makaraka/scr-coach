import os, time, json
from datetime import datetime
import cv2, pytesseract

STREAM_URL = os.getenv("MJPEG_URL", "http://host.docker.internal:8099/stream")

# ROI 좌표(1280x720 기준 예시) - 환경에 맞게 조정하세요.
ROI = {
    "timer":    (1180, 10, 80, 30),
    "minerals": (1220, 10, 80, 30),
    "gas":      (1320, 10, 80, 30),
    "supply":   (1420, 10, 100, 30),
}

# 숫자/슬래시만 허용, 단일 라인 인식
TESS_CFG = r"--psm 7 -c tessedit_char_whitelist=0123456789/"

def read_token(frame, box):
    x, y, w, h = box
    gray = cv2.cvtColor(frame[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
    # Otsu 이진화
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    raw = pytesseract.image_to_string(bw, config=TESS_CFG)
    return "".join([c for c in raw if (c.isdigit() or c == "/")]).strip()

def main():
    cap = cv2.VideoCapture(STREAM_URL)
    if not cap.isOpened():
        print(f"[vision] MJPEG open failed: {STREAM_URL}")
    last = {}
    while True:
        ok, frame = cap.read()
        if not ok:
            time.sleep(0.05)
            continue
        state = {"time": datetime.now().isoformat()}
        for k, box in ROI.items():
            state[k] = read_token(frame, box)
        # 간단한 디바운싱(값이 모두 공백이면 직전값 유지)
        if all(v == "" for k, v in state.items() if k != "time"):
            state.update({k: last.get(k, "") for k in ROI.keys()})
        with open("/shared/state.json", "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False)
        last = state
        print(f"[vision] {json.dumps(state, ensure_ascii=False)}")
        time.sleep(0.3)

if __name__ == "__main__":
    main()
