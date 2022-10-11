import speech_recognition as sr
from os import path
from pydub import AudioSegment

#https://snapinsta.app/
#https://audio-extractor.net/pt/

# transcribe audio file                                                         
AUDIO_FILE = "data/estranho.wav"
LANGUAGE = "pt-BR"

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("data/dear-god.mp3")
print(sound.duration_seconds)
sound.export("data/transcript.wav", format="wav")

# use the audio file as the audio source
r = sr.Recognizer()
for i in range(2):
        with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  #read the entire audio file
        print("Transcription: " + r.recognize_google(audio, language=LANGUAGE))

# use the audio file as the audio source
#r = sr.Recognizer()
#for i in range(2):
 #       with sr.AudioFile(AUDIO_FILE) as source:
                #audio = r.record(source, offset = i*60, duration = 60) 
#        print("Transcription: " + r.recognize_google(audio, language='en-US'))