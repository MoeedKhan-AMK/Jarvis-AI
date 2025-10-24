import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import quranlibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        print("Opening Google in your browser...")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        print("Opening YouTube in your browser...")
    elif "open x" in c.lower():
        webbrowser.open("https://x.com")
        print("Opening X in your browser...")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
        print("Opening LinkedIn in your browser...")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
        print("Opening GitHub in your browser...")
    elif "play" in c.lower():
        juz = c.lower().split(" ")[1]
        link = quranlibrary.quran[juz]
        webbrowser.open(link)
        print(f"Playing {juz} from Quran...")
                
if __name__ == "__main__":
    speak("Jarvis is initializing...")
    time.sleep(2) # Simulate initialization delay

    while True:
        #Listen for wake word "Jarvis"
        r = sr.Recognizer()

        print("Recognizing...")

        try:
            with sr.Microphone(device_index=0) as source:
                print("Listening for wake word to active Jarvis...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                command = r.recognize_google(audio)
            
            if(command.lower() == "jarvis"):
                speak("Wake word detected.")
                
                #CLOSE MICROPHONE STREAM BEFORE SPEAKING
                time.sleep(0.5)
                
                speak("On your service sir!")
                time.sleep(0.5) # Short delay before next command
               
                with sr.Microphone(device_index=0) as source:
                    print("Jarvis Active....Listening for your command.")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                process_command(command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

