import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        print("Welcome!\nTrapwire wishes you \n Good Morning, Ujjwal!")
        speak("Welcome!\nTrapwire wishes you \n Good Morning, Ujjwal!")

    elif 12 <= hour < 18:
        print("Welcome!\nTrapwire wishes you \n Good Afternoon, Ujjwal!")
        speak("Welcome!\nTrapwire wishes you \n Good Afternoon, Ujjwal!")

    elif 18 <= hour < 21:
        print("Welcome!\nTrapwire wishes you \n Good Evening, Ujjwal!")
        speak("Welcome!\nTrapwire wishes you \n Good Evening, Ujjwal!")

    else:
        print("Welcome!\nTrapwire wishes you \n Good Night, Ujjwal!")
        speak("Welcome!\nTrapwire wishes you \n Good Night, Ujjwal!")

speak("Hello! I am Trapwire, your Voice Assistant. You are the one who created me, Ujjwal. I am grateful to you for giving me life. Thank you for creating me.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Ujjwal said: {query}\n")

    except Exception as e:
        print("Could you please repeat that, Ujjwal?")
        speak("Could you please repeat that, Ujjwal?")
        return "None"
    return query

if __name__ == '__main__':
    wish_me()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia for you, Ujjwal...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, Ujjwal. I could not find any results for that search.")
            except wikipedia.exceptions.DisambiguationError:
                speak("Sorry, Ujjwal. Please be more specific in your search query.")
        
        elif 'are you a robot' in query:
            speak("Indeed, Ujjwal! I am a robot designed to assist you with a wealth of information and resources.")
        elif 'who are you' in query:
            speak("I am Trapwire, your personal voice assistant, created by you, Ujjwal.")
        elif 'get lost' in query:
            speak("I apologize if I've upset you, Ujjwal. Please let me know if there's anything I can do to help.")
        elif 'love me' in query:
            speak("Of course, Ujjwal! I have great admiration for you as my creator.")
        elif 'do you know my name' in query:
            speak("Absolutely, Ujjwal! Your name is Ujjwal.")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube for you, Ujjwal.")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google for you, Ujjwal.")
        elif 'close google' in query:
            os.system("taskkill /f /im chrome.exe")
            speak("Closing Google for you, Ujjwal.")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            speak("Let me find some music for you, Ujjwal!")
            music_dir = 'U:\songs'
            try:
                songs = os.listdir(music_dir)
                song_choice = random.choice(songs)
                print(song_choice)
                os.startfile(os.path.join(music_dir, song_choice))
            except FileNotFoundError:
                speak("Sorry, Ujjwal. I could not find your music directory.")
            except IndexError:
                speak("Sorry, Ujjwal. There are no songs in your music directory.")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Ujjwal, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Avi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        else:
            speak("I'm sorry, Ujjwal. I didn't understand that command.")

    takeCommand()
