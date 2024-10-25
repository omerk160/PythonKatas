from pytube import YouTube


def youtube_download(url):
    """
    The function receives a valid YouTube URL and downloads the audio only to the current workdir, in a mp3 format (must end with .mp3).

    Note: the function uses the `pytube` package

    :param url: video url
    :return: None
    """
    return None


if __name__ == '__main__':
    youtube_download('https://www.youtube.com/watch?v=xhud_6AHKfo')
