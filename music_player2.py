from pygame import mixer
mixer.init() #initialise the mixer

#load the music using file path
mixer.music.load(r"C:/Users/Dhiraj kumar/Desktop/My programs/First Kiss - Yo Yo Honey Singh.mp3")

#setting the volume

mixer.music.set_volume(0.8)

#start playing the song

mixer.music.play()

while True:
    print("Press 'p' to pause , 'r' to resume ")
    print("Press 'q' to quit the program ")
    query =input(" ")
    
    if query=='p':
        
        #pausing the music

        mixer.music.pause()
    elif query=='r':
        #resuming the music

        mixer.music.unpause()
    elif query=='e':
        
        #stop the mixer

        mixer.music.stop()
        break


