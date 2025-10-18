import speech_recognition as sr  #speech_recognition is a library in Python used for recognizing speech input
import webbrowser       #webbrowser is a standard library in Python used to open web pages in the default browser
import pyttsx3      #pyttsx3 is a text-to-speech conversion library in Python

recognizer = sr.Recognizer()            #Recognizer is an instance of the Recognizer class from the speech_recognition library
engine = pyttsx3.init()            #engine is an instance of the pyttsx3 class for text-to-speech conversion

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("How may I be of service?")