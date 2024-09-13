from google.cloud import translate_v2 as translate
from speech2text import transcribe_audio

transcribed_text = transcribe_audio("path_to_mono_file.wav")


def translate_text(text, target_language="en"):
    translate_client = translate.Client()


    result = translate_client.translate(text, target_language=target_language)

    return result['translatedText']


translated_text = translate_text(transcribed_text, target_language="en")

print("Translated Text:", translated_text)
