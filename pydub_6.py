# cut audio file

from pydub import AudioSegment

from pydub.playback import play

audio = AudioSegment.from_file("audio_file1.wav")

start,end=1,5

split_audio = audio[start*1000:end*1000]

play(split_audio)

