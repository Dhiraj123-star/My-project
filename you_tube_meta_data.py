# get youtube meta data using Python

from pytube import YouTube

# function takes youtube object as argument

def video_info(yt):
    print("Title: ",yt.title)
    print("Total length: ",yt.length,"seconds")
    print("Total views: ",yt.views)
    print("Is Age restricted: ",yt.age_restricted)
    print("Video Rating: ",round(yt.rating))
    print("Thumbnail Url: ",yt.thumbnail_url)
    print("The description: ", yt.description)
    


link = "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
yt= YouTube(link) # create youtube object

# call the function

video_info(yt)
