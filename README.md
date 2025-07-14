# 🎬 YouTube Video & Audio Downloader

This project is a FastAPI + HTML-based tool to download YouTube videos in various formats including:
- 📹 Full video (with audio)
- 🎞️ Video-only (no audio)
- 🎧 Audio-only (MP3)

> 🔧 Currently working only on **local server**. GitHub Pages frontend loads, but download functionality depends on backend hosted locally.

---

## ✅ Features Implemented

- ✔️ Backend built using **FastAPI** & `yt-dlp`
- ✔️ Frontend form to input YouTube URL
- ✔️ Options to:
  - Download video-only
  - Download audio-only (MP3)
- ✔️ Local download to `backend/downloads/` folder
- ✔️ Backend processes:
  - Single videos
  - Playlists
- ✔️ Download folder structure maintained
- ✔️ Supports up to 4K (when available)

---

## ⚠️ Known Issues & Limitations

| Issue | Notes |
|-------|-------|
| ❌ GitHub Pages frontend can't connect to local backend | Not hosted remotely yet |
| ❌ Mobile devices can't download due to browser/OS restrictions | Use on desktop for best experience |
| ❌ No video preview before download | Could lead to incorrect selection |
| ❌ No download progress UI or auto refresh after download | User has to manually track status |
| ❌ MP3 downloads always fetch highest available quality | Cannot choose bitrate yet |
| ❌ "Video with audio" option often fails or downloads separate tracks only | Merging requires FFmpeg |
| ❌ Downloads sometimes silently fail | No popup or proper error UI yet |
| ❌ UI/UX is basic | Needs design improvements, responsiveness |
| ❌ Cannot select custom download location | All files go to `backend/downloads` by default |

---

## 🚀 Future Improvements (Planned)

- 🌐 Deploy backend on **Render** or **Replit** for full web access
- 📱 Make frontend **mobile-friendly and responsive**
- 🖼️ Add **video preview** with thumbnail + title before download
- 🔁 Auto refresh after each download completes
- 🎨 Improve UI/UX (buttons, layout, feedback messages)
- 🔧 Handle missing FFmpeg gracefully
- 📁 Let user pick **download quality** and **bitrate**
- ⬇️ Option to download both MP3 and MP4 together
- 📦 Add Docker + production build setup

---

## 🛠️ Technologies Used

- **FastAPI** – Backend API
- **yt-dlp** – For downloading YouTube content
- **HTML/CSS/JS** – Frontend interface
- **GitHub Pages** – For static frontend hosting

---

## 💻 How to Run Locally

```bash
# 1. Clone repo
git clone https://github.com/vishal-r16/youtubedownloader.git
cd youtubedownloader/backend

# 2. Set up Python environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate (Linux/Mac)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run FastAPI server
uvicorn app:app --reload

# 5. Visit frontend (if local):
# Open docs/index.html in browser
