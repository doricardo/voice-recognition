import speech_recognition as sr
from os import path
from pydub import AudioSegment

#https://snapinsta.app/
#https://audio-extractor.net/pt/

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("dear-god.mp3")
print(sound.duration_seconds)
sound.export("transcript.wav", format="wav")

# transcribe audio file                                                         
AUDIO_FILE = "estranho.wav"

# use the audio file as the audio source
r = sr.Recognizer()
for i in range(2):
        with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  #read the entire audio file
        print("Transcription: " + r.recognize_google(audio, language='en-US'))

# use the audio file as the audio source
#r = sr.Recognizer()
#for i in range(2):
 #       with sr.AudioFile(AUDIO_FILE) as source:
                #audio = r.record(source, offset = i*60, duration = 60) 
#        print("Transcription: " + r.recognize_google(audio, language='en-US'))