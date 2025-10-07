# SCR Coach Starter (Windows + Docker)

Windows에서 FFmpeg로 화면을 MJPEG 스트림으로 송출하고, Docker 컨테이너들이 이를 읽어
실시간 OCR(vision) → 코칭 메시지(coach)로 변환하는 최소 패키지입니다.

## 빠른 시작

1) **의존성**: Windows 10/11, Docker Desktop(WSL2), FFmpeg
2) **.env 작성**: `.env.example`를 복사해 `.env`를 만들고 키를 입력합니다.
3) **화면 스트림 시작(호스트)**:
   ```powershell
   .\scripts\ffmpeg-start.ps1
   ```
4) **도커 실행**:
   ```powershell
   docker compose up --build vision coach
   ```
5) **로그 확인**:
   ```powershell
   docker compose logs -f vision
   docker compose logs -f coach
   ```

선택) 유튜브 플레이리스트에서 전략 스니펫 적재:
```powershell
docker compose run --rm yt_ingest
```

## 구조
```
scr-coach-starter/
  docker-compose.yml
  .env.example
  kb/
    rules_pvz.yaml
  vision/
    Dockerfile
    vision_stream_tesseract.py
  coach/
    Dockerfile
    run_coach.py
  yt_ingest/
    Dockerfile
    ingest_playlist.py
  scripts/
    ffmpeg-start.ps1
  shared/
    (state.json 생성 위치)
```
