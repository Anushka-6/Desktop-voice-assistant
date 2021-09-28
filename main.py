import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import ctypes
import subprocess
import pyjokes





warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) #[1] for female voice

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:

        data = recog.recognize_google(audio)
        print("You said: " + data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")

    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data

def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)

def call(text):
    action_call = "assistant"
    text = text.lower()

    if action_call in text:
        return True

    return False

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."

def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello", "howdy", "whats good", "hello", "hey there"]

    response = ["hi", "hey", "hola", "greetings", "wassup", "hello", "howdy", "whats good", "hello", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return " "

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


while True:

    try:
        text = rec_audio()
        speak = " "

        if call(text):
            speak = speak + say_hello(text)
            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()

                meridiem = " "
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour
                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."
            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is " in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki
            elif "who are you" in text or "define yourself" in text:
                speak = speak + """Hello, my name is Assistant. A voice assistant. I can help you do various tasks when you command me to do so"""
            elif "your name" in text:
                speak = speak + "My name is Assistant"
            elif "who am I" in text:
                speak = speak + "you must be a human"
            elif "how are you" in text:
                speak = speak + "I am fine, thank you"
                speak = speak + "\nHow are you?"
            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that you are fine"
            elif "open" in text.lower():

                if "word" in text.lower():
                    speak = speak + "Opening Microsoft Word"
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft Excel"
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

                elif "vs code" in text.lower():
                    speak = speak + "Opening Visual Studio Code"
                    os.startfile(
                    r"C:\Users\Kiran\AppData\Local\Programs\Microsoft VS Code\Code.exe")

                else:
                    l = text.split()
                    b = l[2]
                    speak = speak + "opening " + b + "...."
                    os.startfile(b)

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                "http://www.youtube.com/results?search_query=" +"+".join(search))
                speak = speak + "Opening " + str(search) + " on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"
            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "change background" in text or "change wallpaper" in text:
                img = r"C:\Users\Kiran\OneDrive\Documents\Wallpapers"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = speak + "Background changed successfully"

            elif "play music" in text or "play song" in text:
                talk("Here you go with music")
                music_dir = r"C:\Users\Kiran\Music\Songs"
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                random = os.path.join(music_dir, d)
                playsound.playsound(random)

            elif "note" in text or "remember this" in text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that."

            elif "joke" in text:
                speak = speak + pyjokes.get_joke()

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)

            response(speak)
    except:
        talk("I don't know that")



