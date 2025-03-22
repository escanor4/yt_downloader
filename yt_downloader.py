import yt_dlp

def download_yt_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube Video URL: ")
    download_yt_video(video_url)
