from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from downloader import download_video, get_preview
import os

app = FastAPI()

# Serve files in "downloads" folder
app.mount("/files", StaticFiles(directory="downloads"), name="files")

@app.get("/download")
def download(url: str, format: str = "mp4_best", mode: str = "single"):
    file_name = download_video(url, format, mode)
    file_url = f"http://127.0.0.1:8000/files/{file_name}"
    return {"message": f"✅ Ready: {file_name}", "url": file_url}

@app.get("/preview")
def preview(url: str):
    return get_preview(url)
