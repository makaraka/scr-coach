# scripts/ffmpeg-start.ps1
$ffmpeg = "ffmpeg"

# 입력 장치 자동 감지
$devices = & $ffmpeg -hide_banner -devices 2>&1
if ($devices -match "gdigrab") { $grab = "gdigrab" }
elseif ($devices -match "ddagrab") { $grab = "ddagrab" }
else {
  Write-Error "지원되는 화면 캡처 장치(gdigrab/ddagrab)를 찾지 못했습니다."
  exit 1
}

# 전체 데스크톱 → 12fps, 가로 1280, MJPEG HTTP 서버(8099)
& $ffmpeg -hide_banner -f $grab -framerate 12 -i desktop `
  -vf "scale=1280:-1,fps=12" `
  -q:v 6 -f mjpeg -listen 1 http://0.0.0.0:8099/stream
