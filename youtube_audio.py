# downloading audio from youtube

import pafy
url = "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"

video = pafy.new(url)

audiostreams =video.audiostreams

for  i in audiostreams:
    print(i.bitrate, i.extension,i.get_filesize())

audiostreams[3].download()

print("audio is successfully saved!!")

