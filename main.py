import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrery
import requests

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "98470e04293d458b89293b7da59c6f39"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")       
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")     
    elif c.lower().startswith("play"):                     
        song = c.lower().split(" ")[1] 
        link = musicLibrery.music[song]
        webbrowser.open(link)   
        
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=98470e04293d458b89293b7da59c6f39")
        
         # Check if the request was successful
        if r.status_code == 200:
           # Parse the JSON response
           data = r.json()
        
           # Extract the articles from the response
           articles = data.get('articles', [])
        
           # Speak each headline
           for article in articles:
             speak(article['title'])
       
        
                
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #Listen for the wake word "jarvis"
        #obtain audio from the microphone
        r  = sr.Recognizer()
        
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #listen for cammand
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
        except Exception as e :
            print("Error; {0}".format(e))        
                   