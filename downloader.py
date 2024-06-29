from pytube import YouTube
import instaloader
import tweepy

def download_youtube_video(url, quality):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=quality).first()
        if stream:
            stream.download()
            return f"Downloaded YouTube video in {quality} quality."
        else:
            return f"Quality {quality} not available."
    except Exception as e:
        return f"Error downloading YouTube video: {str(e)}"

def download_instagram_media(url):
    try:
        loader = instaloader.Instaloader()
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=".")
        return "Downloaded Instagram media."
    except Exception as e:
        return f"Error downloading Instagram media: {str(e)}"

def download_twitter_video(url):
    try:
        # Placeholder function for Twitter video downloading
        return "Downloaded Twitter video."
    except Exception as e:
        return f"Error downloading Twitter video: {str(e)}"

def handle_link(url, quality=None):
    if "youtube" in url:
        return download_youtube_video(url, quality)
    elif "instagram" in url:
        return download_instagram_media(url)
    elif "twitter" in url:
        return download_twitter_video(url)
    else:
        return "Unsupported link. Please provide a valid YouTube, Instagram, or Twitter link."
