import os
import speech_recognition as sr
import pyttsx3
import openai
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
openai.api_key = "APIKEY"
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        pass

def resp():
    query=take_command()
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=query,
        temperature=0.1,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response['choices'][0]['text'])
    engine.say(response['choices'][0]['text'])
    engine.runAndWait()
    return response['choices'][0]['text']
resp()
