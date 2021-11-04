# amplify audio files
# increase or decrease the default volume of audio files

from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_file('audio_file1.wav')

# boost volume by value dB or use - "subtract" 


amplify_audio = audio+10

play(amplify_audio)

