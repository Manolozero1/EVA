import pyttsx3
import speech_recognition as sr

class VoiceManager:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio, language="es-ES")
        except sr.UnknownValueError:
            return "No entendí lo que dijiste."
        except sr.RequestError:
            return "Error al conectar con el micrófono."

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()