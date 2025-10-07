import os, time, json
from datetime import datetime
from openai import OpenAI

PROMPT = '''너는 Brood War 전략 코치다.
입력 상태(JSON): {state}
지식베이스 발췌: {kb}
출력 형식:
- ① 빌드/연구/생산(다음 30~60초)
- ② 즉시 행동(수치)
- ③ 타이밍(러시/압박/수비)
- ④ 리스크·카운터
'''

def load_kb_snippets(state):
    # TODO: /kb에서 매치업/맵 기반 텍스트 3–5개 로드
    return "예시: 6:30 히드라 타이밍, 코르세어 이전 지상 압박 대비"

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    while True:
        try:
            with open("/shared/state.json", encoding="utf-8") as f:
                state = json.load(f)
        except Exception:
            time.sleep(1.0)
            continue
        kb = load_kb_snippets(state)
        msg = PROMPT.format(state=json.dumps(state, ensure_ascii=False), kb=kb)
        try:
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": msg}],
                temperature=0.2,
            )
            advice = resp.choices[0].message.content.strip()
        except Exception as e:
            advice = f"(코치 응답 오류) {e}"
        print(f"[{datetime.now().strftime('%H:%M:%S')}] COACH\n{advice}\n")
        time.sleep(2.5)

if __name__ == "__main__":
    main()
