import os
import time
from gtts import gTTS
import speech_recognition as sr
import re

def bot_says(spoken_text,file_name):
    """makes the program reproduce the text in audio format"""
    """faz o programa reproduzir o texto em formato de audio"""
    
    speech_name = gTTS(text = spoken_text, lang = 'pt')
    speech_name.save("{}.wav".format(file_name))
    os.system("start C:\\Users\\John\\Desktop\\lei_bot\\{}.wav".format(file_name)) #you should specify the directory the audio files will be created | specificar a diretorio onde os arquivos de audio vão ser criados

    
bot_says("Olá bem vindo ao lei bot, por favor fale seu nome",'ask_name')

time.sleep(5.3)

#the bot will now take your name | o bot vai agora salvar seu nome

while True:
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("fale seu nome agora: ")
        audio = r.listen(source)

        try:
            user_name = r.recognize_google(audio,language = 'pt-BR')
            user_name = user_name.strip()
            user_name.replace("nome","")
            print("seu nome:{}".format(user_name))

        except:
            print("desculpa nao entendi")
            bot_says("desculpa não entendi, por favor repita",'name_error')
            time.sleep(4)
            
        else:
            break

bot_says("seja bem vindo {}, vamos começar o processo".format(user_name),'greeting')

time.sleep(2.5)

bot_says('por favor fale seu cpf','ask_cpf')

time.sleep(3.5)

# the bot will now take your cpf and check if it is correctly formatted | o bot vai agora pegar seu cpf e ver se a formatcao estar correta
# This could also be done with regular expressions using the python re module | isso pode ser feito tambem com expressoes regulares usando modulo re do python

while True:
    
    with sr.Microphone() as source:
        print("fale seu cpf agora: ")
        audio = r.listen(source)

        try:
            user_cpf = r.recognize_google(audio, language = 'pt-BR')
            print("seu cpf : {}".format(user_cpf))
        except:
            print("desculpa nao entendi: ")
            bot_says("desculpa não entendi, por favor repita seu cpf",'cpf_error')
            time.sleep(7)
            

        else:
            user_cpf = user_cpf.replace("-","")
            user_cpf = user_cpf.replace(".","")
            user_cpf = user_cpf.replace(" ","")
            user_cpf = user_cpf.replace("x","")
            user_cpf = user_cpf.replace("C","")
                
            if re.compile(r'\d{11}') :

                bot_says(user_cpf,'user_cpf')
                break

            else:
                bot_says("seu cpf contem caracteres inadequados, por favor reinsira seu cpf",'cpf_broke')
                time.sleep(7)

print("""nome: {}
cpf: {}""".format(user_name,user_cpf))
