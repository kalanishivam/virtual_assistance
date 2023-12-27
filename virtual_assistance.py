import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# speech recognition engine initialization
r = sr.Recognizer()

# the text-to-speech engine initialization
engine = pyttsx3.init()

#  function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

#  function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source, timeout = 3)
        try:
            text = r.recognize_google(audio)
            print(f'Recognized: {text}')
            return text
        except:
            print('Sorry, could not recognize speech.')
            return ''

#  function to get the current time
def get_time():
    now = datetime.datetime.now()
    return now.strftime('%I:%M %p')

#  function to get information from Wikipedia
def search_wikipedia(query):
    try:
        # print(query + "IN THE QUERY FUNCTION ")
        results = wikipedia.summary(query, sentences=2)
        speak('According to Wikipedia...')
        speak(results)
    except:
        speak('Sorry, could not find information on that topic.')

# Main loop
while True:
    text = recognize_speech().lower()
    print(f"User said: {text}") 
    if 'hello' in text:
        speak('Hello, how can I help you?')
    elif 'what time is it' in text:
        speak(f'The time is {get_time()}.')
    elif 'search wikipedia for' in text:
        query = text.replace('search wikipedia for', '')
        print(f"Searching Wikipedia for: {query}") 
        search_wikipedia(query)
    elif 'exit' in text:
        speak('Goodbye!')
        break
