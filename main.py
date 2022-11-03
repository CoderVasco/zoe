#Arquivo principal

#1.Importando o reconhecedor de Speech

import speech_recognition as sr

#2.Criando um reconhecedor de voz

r = sr.Recognizer()

#3. Abrindo o microfonhe para entrada de áudio

with sr.Microphone() as source:
#4. Definindo o Micriofone como entrada de áudio

    audio = r.listen(source)

    print(r.recognize_google(audio))