import speech_recognition as sr
from pydub import AudioSegment

def convert_ogg_to_wav(ogg_filename, wav_filename):
    sound = AudioSegment.from_ogg(ogg_filename)
    sound.export(wav_filename, format="wav")


def convert_speech_to_text(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
            return text.lower()
        except sr.UnknownValueError:
            return None