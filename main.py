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

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=3)

    print("Recognizing...")
    # recognize speech using Google Speech Recognition
    try:
        command = r.recognize_google(audio)
        print(command)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))