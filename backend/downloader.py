# downloader.py
from yt_dlp import YoutubeDL
import os
import shutil


def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in " ._-" else "_" for c in name)


def download_video(url, format="mp4_best", mode="single"):
    is_single = mode == "single"
    downloads_path = os.path.join(os.path.dirname(__file__), "downloads")
    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)

    ydl_opts = {
        "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),
        "noplaylist": is_single,
    }

    if format.startswith("mp4"):
        quality = format.split("_")[1]
        ydl_opts["format"] = (
            f"bestvideo[height={quality}]+bestaudio/best"
            if quality != "best" else "bestvideo+bestaudio/best"
        )

    elif format.startswith("videoonly"):
        quality = format.split("_")[1]
        ydl_opts["format"] = f"bestvideo[height={quality}]" if quality != "best" else "bestvideo"

    elif format.startswith("mp3"):
        audio_quality = format.split("_")[1]
        ydl_opts["format"] = "bestaudio[ext=mp3]/bestaudio[ext=m4a]/bestaudio/best"

        if audio_quality == "best":
            pass  # Skip FFmpeg for best quality
        else:
            ydl_opts["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": audio_quality,
                },
                {"key": "FFmpegMetadata"}
            ]
            ydl_opts["postprocessor_args"] = ["-ar", "44100"]
            ydl_opts["prefer_ffmpeg"] = True
            ydl_opts["ffmpeg_location"] = "C:/ffmpeg/bin"  # Change as per your setup

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        base = os.path.basename(filename)

        # Correct extension if FFmpeg was skipped but user expects .mp3
        if format.startswith("mp3") and audio_quality == "best" and not base.endswith(".mp3"):
            new_name = base.rsplit(".", 1)[0] + ".mp3"
            old_path = os.path.join(downloads_path, base)
            new_path = os.path.join(downloads_path, new_name)
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                base = new_name

        return sanitize_filename(base)


def get_preview(url):
    ydl_opts = {"quiet": True, "skip_download": True}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title", "Unknown Title"),
            "thumbnail": info.get("thumbnail", ""),
            "duration": seconds_to_hms(info.get("duration", 0)),
            "channel": info.get("uploader", "Unknown")
        }


def seconds_to_hms(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes}m {sec}s"
    return f"{minutes}m {sec}s"
