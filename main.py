import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        print("Opening Google in your browser...")

if __name__ == "__main__":
    speak("Jarvis is initializing...")
    # time.sleep(2) # Simulate initialization delay

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

