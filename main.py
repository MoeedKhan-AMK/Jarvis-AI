import speech_recognition as sr     #speech recognition library
import webbrowser           #to open web browser    
import pyttsx3             #text to speech conversion
import time              #to add delays in the program
import requests           #to make API requests

import quranlibrary          #importing quran library
import seerah_library       #importing seerah library

recognizer = sr.Recognizer()
engine = pyttsx3.init()
new_api_key = "5ff34f7b2d9d4baab5584c46370d2676"        #News API key

def speak(text):        #function to make the assistant speak
    engine.say(text)
    engine.runAndWait()

def process_command(c):     #function to process user commands
    
    #Opening websites commands
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
        
        # Quran recitation commands ON HOLD
    # elif "play part" in c.lower():
    #     juz = "juz 1"  # Default juz
    #     if juz in quranlibrary.part:
    #         webbrowser.open(quranlibrary.part[juz])
    #         print(f"Playing {juz}...")
        # Seeerah biography commands ON HOLD
    # elif c.lower().startswith("play"):
    #     biography = c.lower().split("")[1]
    #     link = seerah_library.biography[biography]
    #     webbrowser.open(link)
    
    #News fetching command
    elif "news" in c.lower():
        responses = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&&apiKey={new_api_key}")  #category can be added using category=sports
        speak("Fetching the latest headlines...")

        for i, headline in enumerate(responses.json().get("articles"), start=1):  # First 10 news only
            print(f"{i}. {headline['title']}")
            speak(headline['title'])
            
    else:
        #let LLM API handle commands
        pass
        
# Main program loop
if __name__ == "__main__":
    speak("Jarvis is initializing...")
    time.sleep(2) # Simulate initialization delay

    while True:
        #Listen for wake word "Jarvis"
        r = sr.Recognizer()
        
        print("Recognizing...")
        
        #USE THE APPROPRIATE MICROPHONE DEVICE INDEX
        try:
            with sr.Microphone(device_index=0) as source:
                print("Listening for wake word to active Jarvis...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                command = r.recognize_google(audio)
            
            if(command.lower() == "jarvis"):
                speak("Wake word detected.")
                
                #CLOSE MICROPHONE STREAM BEFORE SPEAKING
                # time.sleep(0.5)
                
                speak("On your service sir!")
               
                with sr.Microphone(device_index=0) as source:
                    print("Jarvis Activated!")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                process_command(command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

