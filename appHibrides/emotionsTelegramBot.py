# -*- coding: utf-8 -*-

import telebot
import random
import json

bot = telebot.TeleBot("881906354:AAGCRz33rl_75jd0clXDcr3urHWLPMXWPeg")

bot.send_message(965523336, "Hola, benvenido/da! <3")
bot.send_message(965523336, "Como te va hoy? ")
""" Aquests send_message s'activen nomes obrir el bot """

frasesTriste = ["Eso no es bueno T.T","Piensa en un t-rex intentando hacer la cama","No es lo que tienes, lo que eres o dónde estas lo que te hace feliz o infeliz. Es lo que piensas sobre ello"]
frasesFeliz = ["Me alegro :D","Sigue asi, la felicidad se encuentra en las cosas pequeñas.","La felicidad es efimera, asi que, recuerda no sobrecargarte."]

parBien = ["Bien","bien"]
parMal = ["Mal","mal"]

json_keyboard = json.dumps({'keyboard': [["Bien"], ["Mal"]],
                            'one_time_keyboard': True,
                            'resize_keyboard': True})


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

    else:

                    if l == 1 or m == 1:
                            if l == 1:
                                bot.send_message(message.chat.id, frasesFeliz[random.randint(0,len(frasesFeliz)-1)])
                            if m == 1:
                                bot.send_message(message.chat.id, frasesTriste[random.randint(0,len(frasesTriste)-1)])



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

bot.polling()
