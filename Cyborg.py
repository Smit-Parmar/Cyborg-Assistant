import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import webbrowser
import os
import random
import smtplib
import googlesearch
name="smitparmar822000@gmail.com"
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning smit")
    elif hour>=12 and hour<16:
        speak("Good Afternoon smit")
    else:
        speak("Good evening smit")
def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print("Listening...")
            r.dynamic_energy_threshold = False
            r.energy_threshold=1500
            r.pause_threshold = 1
            audio = r.listen(source)#Converts audio input into string
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")
        except Exception as e:
            print("Can you please repeat")
            print(e)
            return "None"
        return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('smit.parmar15191@marwadieducation.edu.in','smitraj@333')
    server.sendmail(to,to,content)
    server.close()

if __name__=="__main__":
    wishme()
    speak("I am cyborg Your assistant how may i help you")
    while True:
        query=takeCommand().lower()
        #Logic for execute task based query
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'open youtube' in query:
            #firefox = 'C:\Program Files (x86)\Mozilla Firefox\firefox.exe %s'
            #webbrowser.get(firefox).open('youtube.com')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir = 'F:\\SONGS\\Videoder Downloads'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,50)]))
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'send email' in query:
                try:
                    speak("What should i send?")
                    content=takeCommand()
                    speak("To whom i send the mail")
                    name=takeCommand().lower()
                    print(name)
                    if "smit" in name:
                        to="smitraj333@gmail.com"
                        print("Inside the smit")
                        sendEmail(to,content)
                        speak("Email has been send sir")
                    elif "bhavy" in name:
                        print(name)
                        to="bhavyparmar33@gmail.com"
                        sendEmail(to,content)        
                        speak("Email has been send sir")
                    else:
                        speak("Sorry i dont know that id")
                except Exception as e:
                    print(e)
                    speak("Sorry sir i am not able to fulfill you email request")

        elif 'open visual code' in query:
            codepath="D:\\Sofware_installation\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'thank you' in query:
            speak("Happy to help friend?")
        elif 'bye bro' in query or 'goodbye cyborg' in query or 'bye nigga' in query or 'bye niga'in query:
            speak("Bye nigga......Happy to help")
            exit()
        elif 'awesome' in query:
            speak('Thanks for your compliment')
        elif "it's ok" in query:
            speak('Thank you sir')
        elif 'funny' in query:
            speak("hahahah hahaaha ohohoohohoo eeheheheheheh uhhuhuhuhuhuh  heeeeeeeeehoooooooohhaaaaaaa emememememememem ggogogogogogo")
        elif 'who are you' in query:
            speak("How can you forget me nigga......I am your partner Cyborg....Hope you will remember and dont hurt me again")
        elif "tell me about yourself" in query:
            speak("I am cyborg the virtual assistant, Developed my partner smit parmar , I can perform various task like play music, Search wikipedia and many other stuff. Hope you are not taking my interview.")
        '''
        elif "search google":
            try:
                speak("Whats should i search")
                searchh=takeCommand().lower()
                response = GoogleSearch().search("something")
                for result in response.results:
                    print("Title: " + result.title)
                    print("Content: " + result.getText())
                
            except Exception as e:
                print(e)
                speak("Sorry")
        '''
    
    

