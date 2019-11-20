# -*- coding: utf-8 -*-

import telebot
import random
import json

bot = telebot.TeleBot("881906354:AAGCRz33rl_75jd0clXDcr3urHWLPMXWPeg")




""" Aquests send_message s'activen nomes obrir el bot """
resp1="Eso no es bueno T-T' \nAquí te dejo una frase para que te animes ~^-^~"
resp2="Me alegro :D \nAquí tienes una frase para ser aun mas feliz -\^v^/-"


arxiuFeliz = open('feliz.txt', "r")
arxiuTrist = open('trist.txt', "r")

linesFeliz = arxiuFeliz.readlines()
linesTriste = arxiuTrist.readlines()




parBien = ["Bien","bien","Feliz","feliz"]
parMal = ["Mal","mal","Triste","triste"]

json_keyboard = json.dumps({'keyboard': [["Bien"], ["Mal"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})



json_keyboard2 = json.dumps({'keyboard': [["feliz.txt"], ["trist.txt"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})


@bot.message_handler(regexp="adios")
def adios(message):
    bot.send_message(message.chat.id, "Hasta pronto o/")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hola, benvenido/da! <3")
    bot.send_message(message.chat.id, "Como te va hoy? ")
    bot.send_message(message.chat.id, "Si no sabes que hacer escribe /help ")

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(message.chat.id, "Puedes decirme como te fue hoy el dia")
    bot.send_message(message.chat.id, "Tambien puedes añadir frases en el arxivo Feliz con /addF")
    bot.send_message(message.chat.id, "Tambien puedes añadir frases en el arxivo Triste con /addT")
    bot.send_message(message.chat.id, "Si no quieres hablar conmigo solo tienes que decir adios")


'''def frase(messages):
    for message in messages:
        arxiuGeneral = open("feliz.txt",'a')
        arxiuGeneral.write(message.text+"\n")
        arxiuGeneral.close()
        break
'''

@bot.message_handler(commands=['addF'])
def add_frase(message):
    frase=" "
    op=" "
    keyboard=message.text.split()
    if len(keyboard)>1:
        for n in keyboard:
            if(n=="/addF"):
                op=n
            else:
                frase=frase+n+" "

        arxiuGeneral = open("feliz.txt",'a')
        arxiuGeneral.write(frase.strip()+"\n")
        arxiuGeneral.close()

        bot.send_message(message.chat.id,"S'ha afegit la frase: \""+frase+"\" correctament a l'arxiu feliz.txt")

    else:
        bot.send_message(message.chat.id,"Escribe la frase al lado de /addF \nEjemplo: \"/addF frase que quiero\"")
    #bot.send_message(message.chat.id, "Que frase quieres añadir?")
           #frase=message
    #bot.send_message(message.chat.id, "hola")

@bot.message_handler(commands=['addT'])
def add_frase(message):
    frase=" "
    op=" "
    keyboard=message.text.split()
    if len(keyboard)>1:
        for n in keyboard:
            if(n=="/addT"):
                op=n
            else:
                frase=frase+n+" "

        arxiuGeneral = open("trist.txt",'a')
        arxiuGeneral.write(frase.strip()+"\n")
        arxiuGeneral.close()

        bot.send_message(message.chat.id,"S'ha afegit la frase: \""+frase+"\" correctament a l'arxiu trist.txt")

    else:
        bot.send_message(message.chat.id,"Escribe la frase al lado de /addT \n Ejemplo: \"/addT frase que quiero\"")



@bot.message_handler(func=lambda message:True)

def compro(message):
    l=0
    m=0
    paraules=message.text.split(" ")
    for i in paraules:

        for j in parBien:

            if i == j:
                l=l+1

        for s in parMal:

            if i == s:
                m=m+1


    if l>=1 and m>=1:

                bot.send_message(message.chat.id,"Estas bien o mal?",reply_markup=json_keyboard)

    elif l==0 and m==0:
                bot.send_message(message.chat.id,"Explicame mas sobre tu día!!")

    else:

            if l == 1 or m == 1:
                    if l == 1:
                        bot.send_message(message.chat.id,resp2)
                        bot.send_message(message.chat.id, linesFeliz[random.randint(0,len(linesFeliz)-1)])
                    if m == 1:
                        bot.send_message(message.chat.id,resp1)
                        bot.send_message(message.chat.id, linesTriste[random.randint(0,len(linesTriste)-1)])



    #    if j >=1:
    #        bot.send_message(message.chat.id,"Estas bien o mal?",reply_markup=json_keyboard)





" Aquesta funcio s'activa quan troba les paraules 'triste' o 'deprimido'. Utilitza l'array frasesTristes """
" La frase surt aleatoriament de les que hi ha a l'array"""
"""
@bot.message_handler(regexp="feliz" or "euforico")
# Emociones felices=FreasesFeliz
def feliz(message):
    bot.send_message(message.chat.id, frasesFeliz[random.randint(0,len(frasesTriste)-1)])



@bot.message_handler(regexp="feliz" and "triste")

def eleccion(message):
    bot.send_message(message.chat.id,"Estas triste o feliz")





@bot.message_handler(regexp="Adios")
# Despedida
def control(message):

        bot.send_message(965523336, "Adios, vuelve pronto!!!. Siempre eres bienvenido <3")

"""
arxiuTrist.close()
arxiuFeliz.close()

bot.polling()
