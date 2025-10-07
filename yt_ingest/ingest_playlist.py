import os, sys, json, time
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

PLAYLIST_ID = sys.argv[1] if len(sys.argv) > 1 else ""
OUT_DIR = "/kb"

def list_video_ids(playlist_id, api_key):
    yt = build("youtube", "v3", developerKey=api_key)
    vids, page = [], None
    while True:
        res = yt.playlistItems().list(
            part="contentDetails", playlistId=playlist_id, maxResults=50, pageToken=page
        ).execute()
        vids += [it["contentDetails"]["videoId"] for it in res.get("items", [])]
        page = res.get("nextPageToken")
        if not page:
            break
    return vids

def fetch_transcript(video_id):
    try:
        trs = YouTubeTranscriptApi.get_transcript(video_id, languages=["ko","en"])
        return "\n".join([f"{x['start']:.1f}: {x['text']}" for x in trs])
    except Exception:
        return None

def extract_build_events(text):
    KEYS = ["해처리","히드라","뮤탈","성큰","커세어","질럿","러시","압박","더블","삼해처","드랍","탱크","레이스"]
    lines = [ln for ln in text.splitlines() if any(k in ln for k in KEYS)]
    return {"events": lines[:80]}

def main():
    api_key = os.getenv("YT_API_KEY")
    if not api_key or not PLAYLIST_ID:
        print("YT_API_KEY 또는 PLAYLIST_ID 누락")
        sys.exit(1)
    video_ids = list_video_ids(PLAYLIST_ID, api_key)
    for vid in video_ids:
        text = fetch_transcript(vid)
        if not text:
            continue
        kb_item = {"videoId": vid, "strategy": extract_build_events(text)}
        with open(os.path.join(OUT_DIR, f"{vid}.json"), "w", encoding="utf-8") as f:
            json.dump(kb_item, f, ensure_ascii=False, indent=2)
        time.sleep(0.2)

if __name__ == "__main__":
    main()
