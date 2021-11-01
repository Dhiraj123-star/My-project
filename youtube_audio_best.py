# download the audio in the best quality

import pafy 

url ="https://www.youtube.com/watch?v=PlbupGCBV6w&list=PLsyeobzWxl7rrvgG7MLNIMSTzVCDZZcT4"

video = pafy.new(url)

bestaudio = video.getbestaudio()

bestaudio.download()

print("Audio is successfully saved in best quality!!")