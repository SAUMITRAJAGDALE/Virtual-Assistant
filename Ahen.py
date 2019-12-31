import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12 :
        speak("Good Morining!")
    elif hour>12 and hour<18 :
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")

    speak(" Sir I am Ahen Please tell me how may I help you")



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print('Say that again please....')
        return 'None'
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('saumitracruise@gmail.com','9892909015')
    server.sendmail('saumitracruise@gmail.com',to,content)
    server.close()




if __name__=="__main__" :
    wishMe()
    dict={'abhishek':'abhishek1931jadhav@gmail.com','soumitra':'jagdale65@gmail.com','mom':'saumilucky@gmail.com'}
    while True :
        query=takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("Wikipedia", "")
            results= wikipedia.summary(query,sentences=2)
            speak('According to wikipedia...')
            print(results)
            speak(results)

        elif 'open youtube' in query: 
            webbrowser.open("youtube.com")    

        elif 'open google' in query: 
            webbrowser.open("google.com")   

        elif 'open facebook' in query: 
            webbrowser.open("facebook.com")   

        elif 'open whatsapp' in query: 
            webbrowser.open("web.whatsappweb.com")        
        elif 'play music' in query:  
            music_dir= 'D://Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}\n")

        elif 'open code' in query:
            codePath="C:\\Users\\jagda\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open python' in query:
            codePath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'send email' in query :
            
            speak('Whom should I send?')
            name = takeCommand().lower()
            to=dict[name]
            
            try :
                speak('what should I say?')
                content= takeCommand()
                sendEmail(to,content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry email could not be sent...please Try again later')

        elif 'how are you' in query :
            speak('I am fine Sir...how are you?? How can I help you??')

        elif 'maitri' in query :
            speak('Maitry Gaur wife of Soumitra Jagdale is the most cutest girl in the college.....She has a fearless attitude....She loves Bald people but...still fell for Soumitra Jagdale ...her biggest regret')
        elif 'rutuja' in query :
            speak('Rutuja Kothurkar is the beloved daughter of Maitri Gaur  and Saumitra Jagdale... She will be married to Saurabh gawas as soon as possible...to give birth to Chintamani...She has beautiful eyes and mesmerizing vibes.Also the chairperson of etsa') 
        elif 'vaishnavi' in query:
            speak('Vaishnavi Eache also known as mother of Ted X F C R I T is     mother in law of Maitri Gaur. She is beautiful according to most boys....She has great oratory skills and is a born leader... oh oh oh I am sorry Dictator.')
        elif 'abhishek' in query :
            speak('Abhishek Jadhav son of Saumitra Jagdale and Neha Nerurkar is also known as Playboy. He will be soon married to Snehal. He has a very caring nature and he came first in chess tournament. He is also Bastard of Saumitra  ')
        elif 'sudhanshu' in query:
            speak('Sudhanshu Kurle son of Chinmay thakre   has a perfect all round personality in academics and in sports. At times his jokes are lame but he flirts good to   cover it up. At times he is a gentleman   when he is not present')
        elif 'chinmay' in query :
            speak('Chinmay thakre the eldest and wisest member of the family has some of woman qualities. He is the parent element of this family tree.  He has very good muscles and biceps   Sometimes he is mysterious ')
        elif 'who are you' in query :
            speak('Sir  I am Ahen your virtual assistant created by Soumitra Jagdale')
        elif ('hi' or 'hello' or 'hey') in query:
            speak('Hello Sir, How may I help you')
        elif 'i love you' in query:
            speak('thank you sir but I do not understand what is love')
        else :
            speak(f"Sorry I don't understand {query}")

        
            
    

        

        

        
