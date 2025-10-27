import os
import speech_recognition as sr     #speech recognition library
import webbrowser           #to open web browser    
# import pyttsx3             #text to speech conversion
from gtts import gTTS       #Google text to speech conversion
from playsound import playsound  #to play sound
import time              #to add delays in the program
import requests           #to make API requests

from client import ask_Jarvis   #importing ask_Jarvis function from client.py
import quranlibrary          #importing quran library
import seerah_library       #importing seerah library

recognizer = sr.Recognizer()
# engine = pyttsx3.init()
new_api_key = "5ff34f7b2d9d4baab5584c46370d2676"        #News API key

# def speak(text):        #function to make the assistant speak
#     engine.say(text)
#     engine.runAndWait()

#google text to speech

def speak(text):
    # tts = gTTS(text)
    # tts.save('text.mp3')
    print("Jarvis: ", text)
    tts = gTTS(text=text, lang='en')
    
    filename = f"voice_{int(time.time())}.mp3"  # unique filename
    
    tts.save(filename)
    playsound(filename)
    
    os.remove(filename)  # delete temp audio file after playing

    
def process_command(c):     #function to process user commands
    
    #Opening websites commands
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google in your browser...")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube in your browser...")
    elif "open x" in c.lower():
        webbrowser.open("https://x.com")
        speak("Opening X in your browser...")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn in your browser...")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
        speak("Opening GitHub in your browser...")
        
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
    elif "play surah" in c.lower():
        surah_name = c.lower().replace("play surah", "").strip()
        if surah_name in quranlibrary.quran_surah:
            webbrowser.open(quranlibrary.quran_surah[surah_name])
            speak(f"Playing {surah_name}")
            
    elif "tell me about" in c.lower():
        topic = c.lower().replace("tell me about", "").strip()
        if topic in seerah_library.seerah_biography:
            webbrowser.open(seerah_library.seerah_biography[topic])
            speak(f"Opening information about {topic}")


    
    #News fetching command
    elif "news" in c.lower():
        responses = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&&apiKey={new_api_key}")  #category can be added using category=sports
        speak("Fetching the latest headlines...")

        for i, headline in enumerate(responses.json().get("articles"), start=1):  # First 10 news only
            print(f"{i}. {headline['title']}")
            speak(headline['title'])
            
    else:
        #let LLM API handle commands
        response = ask_Jarvis(c)
        print("User: " + command)
        print("Jarvis: " + response)
        speak(response)


# Main program loop
if __name__ == "__main__":
    speak("Jarvis is initializing...")

    while True:
        #Listen for wake word "Jarvis"
        r = sr.Recognizer()
        
        print("Recognizing...")
        
        #USE THE APPROPRIATE MICROPHONE DEVICE INDEX
        try:
            with sr.Microphone(device_index=0) as source:
                speak("Say Jarvis to wake me up.")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                command = r.recognize_google(audio)
            
            if(command.lower() == "jarvis"):
                speak("Yes? How can I help you?")

                
                #CLOSE MICROPHONE STREAM BEFORE SPEAKING
                # time.sleep(0.5)

                with sr.Microphone(device_index=0) as source:
                    # print("Jarvis Activated!")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                process_command(command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

