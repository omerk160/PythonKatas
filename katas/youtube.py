from pytube import YouTube
import os


def youtube_download(url):
    """
    Downloads the audio only from a YouTube URL to the current workdir in mp3 format.

    :param url: YouTube video URL
    :return: None
    """
    try:
        # Initialize YouTube object
        yt = YouTube(url)

        # Get audio-only stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download audio stream as an mp4 file
        output_file = audio_stream.download(filename="audio.mp4")

        # Define the new filename with .mp3 extension
        base, ext = os.path.splitext(output_file)
        new_file = base + '.mp3'

        # Rename the file to .mp3
        os.rename(output_file, new_file)
        print(f"Download complete: {new_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    youtube_download('https://www.youtube.com/watch?v=xhud_6AHKfo')
