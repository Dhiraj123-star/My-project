# concat audio files
# we can concat many audio files into one audio file

from pydub import AudioSegment
from pydub.playback import play

audio1 = AudioSegment.from_file('audio_file1.wav')
audio2= AudioSegment.from_file('audio_file2.wav')

combined_audio = AudioSegment.empty()

# concat audio files in 1..

combined_audio = audio1+audio2


play(combined_audio)