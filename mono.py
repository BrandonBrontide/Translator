from pydub import AudioSegment

audio = AudioSegment.from_wav("a short audio message in Spanish.wav")

mono_audio = audio.set_channels(1)

mono_audio.export("path_to_mono_file.wav", format="wav")
