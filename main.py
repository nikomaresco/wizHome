'''
Created on Feb 28, 2016

@author: niko
'''


import speech_recognition as sr


r = sr.Recognizer()

listen = False

# Define methods

while True:
    print('loop 1')
    while listen == False:
        try:
            print('trying')
            with sr.Microphone() as source:
                print('got mic')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                pinger=r.recognize_google(audio)
            try:
                print(pinger.lower())
                if (pinger.lower() == "start") :
                    listen = True
                    print("Listening...")
                    break
                else:
                    continue
            except LookupError:
                continue
        except sr.UnknownValueError:
            continue

    while listen == True:

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                pinger=r.recognize_google(audio)
            print("1")

            print("2")
            if (pinger.lower() == "stop") :
                listen = False
                print("Listening stopped. Goodnight")
                break
            else:
                print("You said " + pinger)
        except LookupError:

            print("Could not understand audio")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            continue
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            continue