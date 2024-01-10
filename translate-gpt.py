# source ~/Translate-gpt/Dependencies/bin/activate && python3 ~/Translate-gpt/translate-gpt.py
import speech_recognition as sr
from openai import OpenAI
import pyttsx3
r=sr.Recognizer()


engine=pyttsx3.init()
engine.setProperty('voice', 'english-us')
def speak(say):
    engine.say(say)
    engine.runAndWait()

    
client = OpenAI(api_key="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")
def chat_english():
    messages = [ {"role": "system", "content": 
              "I am going to use you as a translator. Google translate is bad, as its AI is not as advanced as you. I want you to take my english input and translate it into proper spanish and proper grammar. There should be no context or explanantion, just the translation"} ]

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('speak english')
            audio=r.listen(source)
            print('done')
            saidtxt=r.recognize_google(audio)
    except:
        saidtxt=" "
    message = saidtxt
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(message)
    print(reply)
    engine.setProperty('voice', 'spanish')
    speak(reply)
    messages.append({"role": "assistant", "content": reply})
def chat_spanish():
    messages = [ {"role": "system", "content": 
              "I am going to use you as a translator. Google translate is bad, as its AI is not as advanced as you. I want you to take my spanish input and translate it into proper english and proper grammar. There should be no context or explanantion, just the translation"} ]

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Habla español')
            audio=r.listen(source)
            print('Hecho')
            saidtxt=r.recognize_google(audio,language="es-LA")
    except:
        saidtxt=" "
    message = saidtxt
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(message)
    print(reply)
    engine.setProperty('voice', 'english-us')
    speak(reply)
    messages.append({"role": "assistant", "content": reply})
while True:
    asklang=input('Español or English? ')
    asklang=asklang.lower()
    if 'esp' in asklang:
        chat_spanish()
    elif 'eng' in asklang:
        chat_english()
    elif 'exit' in asklang:
        exit()
    else:
        print('Not understood/No comprendo')