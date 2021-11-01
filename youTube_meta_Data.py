# get meta data using pafy

import pafy 

# url of the video

url = "https://www.youtube.com/watch?v=POPLF-Qc0OU&list=PLsyeobzWxl7rrvgG7MLNIMSTzVCDZZcT4&index=2"

# instant created 

video = pafy.new(url)

# print title

print("Title of the video:",video.title)

# print the rating
print("Rating: ",video.rating)

# print viewpoint

print("ViewPoint: ",video.viewcount)

# print author and video length

print(f" author of video: {video.author} and video length: {video.length}")

print("The likes:",video.likes)
print("Unlikes: ",video.dislikes)
