# youtube downloading 

from pytube import YouTube

def download_yt(yt):
    # filter mp4 streams from object
    my_stream = yt.streams.filter(file_extension='mp4',only_video=True)

    for streams in my_stream:
        # print itag,resolution and codec format of Mp4 streams

        print(f"Video tag:{streams.itag} Resolution:{streams.resolution}")

        # enter the itag value of resolution on which you want to download the video

    input_itag = input("Enter itag Value: ")

    # get video using itag value
    video = yt.streams.get_by_itag(input_itag)

    # finally download the youtube video...
    video.download()

    print("Video is downloading as ",yt.title+".mp4")

link  = "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
# create youtube object

yt = YouTube(link)

# call the function

download_yt(yt)