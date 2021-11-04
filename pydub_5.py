# overlay audio files

from pydub import AudioSegment

from pydub.playback import play

aud1 = AudioSegment.from_file("audio_file1.wav")
aud2 = AudioSegment.from_file("audio_file2.wav")

overlay_aud = aud1.overlay(aud2,position=0,loop=True)

play(overlay_aud)