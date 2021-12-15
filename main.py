from datetime import datetime as dt
import pyttsx3
from decouple import config
import speech_recognition as sr
from random import choice
from functions.offline_ops import open_camera, open_cmd, open_chrome
from functions.online_ops import get_iss_location, get_random_joke, play_on_youtube, search_on_google, search_on_wikipedia

USER = config('USER')
BOTNAME = config('BOTNAME')


opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]

error_text = [
    "Sorry, I could not understand. Could you please say that again?",
    "I am having trouble understanding sir. Please try again.",
    "Oh boy, my ears have a lot of dust in them if you know what I mean. Another try please?"
]

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user according to the time of day"""
    hour = dt.now().hour
    if hour >= 6 and hour < 12:
        speak(f"Good Morning {USER}")
    elif hour >= 12 and hour < 16:
        speak(f"Good Afternoon {USER}")
    else:
        speak(f"Good Evening {USER}")
    speak(f"My name is {BOTNAME}, I am at your service")

def take_user_input():
    """Takes user speech, and converts to text"""
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(query)
        if not 'exit' in query and 'stop' not in query:
            speak(choice(opening_text))
        else:
            hour = dt.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night, take care!")
            else:
                speak('Have a good day!')
            exit()
    except Exception:
        query = 'None'
    return query

if __name__ == '__main__':
    greet_user()
    waiting = True
    while True:
        query = take_user_input().lower()

        if waiting and query == 'none':
            print("Waiting...")
        else:
            waiting = False

        if 'open command line' in query:
            open_cmd()
            waiting = True
        
        elif 'open chrome' in query:
            open_chrome()
            waiting = True
        
        elif 'camera' in query:
            open_camera()
            waiting = True

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, mate?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen mate.")
            print(results)
            waiting = True
        
        elif 'search on google' in query:
            speak('What do you want to search on Google?')
            query = take_user_input().lower()
            search_on_google(query)
            waiting = True
        
        elif 'youtube' in query:
            speak('What do you want to play on Youtube my man?')
            video = take_user_input().lower()
            play_on_youtube(video)
            waiting = True
        
        elif 'joke' in query:
            joke = get_random_joke()
            print(joke)
            speak(joke)
            speak("Ha ha ha ha ha....get it?")
        
        elif 'iss' in query:
            get_iss_location()
            waiting = True

        elif not waiting and query != 'none':
            speak(choice(error_text))
            waiting = True
