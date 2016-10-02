'''
Created on Feb 28, 2016

@author: niko
'''

import win32com.client
import speech_recognition
import datetime
import pyaudio
import wave
import sys


system_name = "system"


def tts_sapi_init():
    vox = win32com.client.Dispatch("SAPI.SpVoice")

    print("S.A.P.I. TTS speech engine initialized")
    #self.vox.Speak("S.A.P.I. speech engine initialized")

    return vox



class Sound

    chunk = 1024
    wave_file = None
    stream = None
    
    def __init__(self, file):

        # init audio stream
        self.wave_file = wave.open(file, 'rb')
        
        self.p = pyaudio.PyAudio()
        
        self.stream = self.p.open(format = self.p.get_format_from_width(self.wave_file.getsampwidth()),
                                    channels = self.wave_file.getnchannels(),
                                    rate = self.wave_file.getframerate(),
                                    output = True)

    # play file
    def play(self):
        data = self.wave_file.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wave_file.readframes(self.chunk)

    # close audio stream
    def close(self):
        self.stream.close()
        self.p.terminate()

s = Sound('what.wav')

class Speaker:

    vox = None
    recognizer = None

    def __init__(self, tts_engine, stt_engine):

        #self.tts_engine = tts_engine
        #self.stt_engine = stt_engine

        # initialize text-to-speech engine
        if tts_engine == "SAPI":
            self.vox = tts_sapi_init()

        # initialize speech recognition
        self.recognizer = speech_recognition.Recognizer()



    # speak a message
    def say(self, message):

        self.vox.Speak(message)


    # listen for and process a single speech command
    def listen(self):

        try:
            with speech_recognition.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

                # use Google speech recognition
                text = self.recognizer.recognize_google(audio)

                return text

        except speech_recognition.UnknownValueError:
            print("couldn't understand audio")

        except speech_recognition.RequestError as e:
            print("recognition error: {0}".format(e))

        return ''





# prototype speech processing loop
def main():

    speaker = Speaker("SAPI", "Google")
    #speaker.say("a-yo mahfuckuh! wattup in da hizzie my nizzie")

    # "listening" in this case is actually "listening for and interpereting commands";
    # the code is ALWAYS listening
    listening = False

    # timestamp of last command, used for timeout
    last_command = None

    # main speech processing loop
    while True:

        # listening and not listening loops are separated 
        # command interperetation should be off, but listen for start command
        while not listening:
            
            # get voice input as text and convert to lowercase
            voice_input = speaker.listen().lower()
            
            # check if voice input starts with system name
            if voice_input == system_name + ' start':

                # and begin listening
                listening = True

                speaker.say('say a command')

                print('started listening')


        # command interperetation should be on
        while listening:

            voice_input = speaker.listen().lower()

            if voice_input.startswith(system_name):
                command = voice_input.split(-)
                if command == 'stop':
    
                    listening = False
    
                    speaker.say('say "start" to resume listening')
    
                    print('stopped listening')
    
                else: 
                    print("received:", command)
                    print()

        print("done")


if (__name__ == "__main__"):
    main()
