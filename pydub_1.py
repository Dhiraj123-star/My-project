# play audio file using pydub

from pydub import AudioSegment

from pydub.playback import play

audio = AudioSegment.from_file('audio_file1.wav')

# play the sound

play(audio)
