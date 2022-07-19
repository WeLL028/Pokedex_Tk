#### 4 Projeto Pokedex em Python ####
#### Obervação projeto não é meu, mas curti a idéia #### 
# Autora https://github.com/venanciotayna/pokedex.git #

from cProfile import label
from re import L
from tkinter import *
from tkinter import ttk

# Importanto pillow
from PIL import Image, ImageTk

# Importando os Dados

from projeto4_dados_pokemons import *

#### Cores ####

cor0= '#000000' # preto
cor1= '#feffff' # branco
cor2= '#6f9fbd' # azul 
cor3= '#38576b' # valor
cor4= '#403d3d' # letra
cor5= '#ef5350' # vermelho

#### Criando Janela ###  

janela = Tk()
janela.title('Pokedex By WeLL 👨‍💻​')
janela.geometry('550x510') # comprimentoXaltura
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor0) #bg (backgrand)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style= ttk.Style(janela)
style.theme_use('clam')

# Criando Frame 

frame_pokemon= Frame(janela, width=550, height=290,relief='flat')
frame_pokemon.grid(row=1, column=0)

# Funcão de troca

def trocar_pok(i):
    global image_pok, poke_nome

# Trocando a cor de fundo do frame_pokemon 
    frame_pokemon['bg'] = pokemon[i]['Tipo'][3]
   
   #Tipo de Pokemon

    poke_nome['text'] = i
    poke_nome['bg'] = pokemon[i]['Tipo'][3]
    poke_tipo['text'] = pokemon[i]['Tipo'][1]
    poke_tipo['bg'] = pokemon[i]['Tipo'][3]
    poke_id['text'] = pokemon[i]['Tipo'][0]
    poke_id['bg'] = pokemon[i]['Tipo'][3]
    image_pok = pokemon[i]['Tipo'][2]

    # imagens dos pokemos 

    image_pok= Image.open(image_pok)
    image_pok= image_pok.resize((238,238))
    image_pok= ImageTk.PhotoImage(image_pok)

    poke_image= Label(frame_pokemon,image=image_pok ,relief='flat', font=('Ivy 10 bold '), bg=pokemon[i]['Tipo'][3], fg=cor0)
    poke_image.place(x=60,y=50)

    poke_tipo.lift()

    # Poke Status

    poke_hp['text']=pokemon[i]['Status'][0]
    poke_ataque['text']=pokemon[i]['Status'][1] 
    poke_defesa['text']=pokemon[i]['Status'][2] 
    poke_velo['text']=pokemon[i]['Status'][3] 
    poke_total['text']=pokemon[i]['Status'][4]

    # Poke Habilidades

    poke_habili1['text']=pokemon[i]['Habilidades'][0]
    poke_habili2['text']=pokemon[i]['Habilidades'][1]

# Criando frame nome

poke_nome= Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Verdana 20 bold'), bg=cor0, fg=cor1)
poke_nome.place(x=12,y=15)

# Criando frame categoria

poke_tipo= Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold '), bg=cor0, fg=cor1)
poke_tipo.place(x=12,y=55)

# Criando frame id do pokemon

poke_id= Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold '), bg=cor0, fg=cor1)
poke_id.place(x=12,y=80)

# Criando frame Status

poke_status= Label(janela, text='Status', relief='flat', anchor=CENTER, font=(' Vernada 20 bold '), bg=cor0, fg=cor1)
poke_status.place(x=15,y=310)

# Criando frame Hp

poke_hp= Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=(' Vernada 10 bold '), bg=cor0, fg=cor1)
poke_hp.place(x=15,y=360) 

# Criando frame Ataque

poke_ataque= Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=(' Vernada 10 bold '), bg=cor0, fg=cor1)
poke_ataque.place(x=15,y=385)

# Criando frame Defesa

poke_defesa= Label(janela, text='Defesa: 100', relief='flat', anchor=CENTER, font=(' Vernada 10 bold '), bg=cor0, fg=cor1)
poke_defesa.place(x=15,y=410)

# Criando frame Velocidade

poke_velo= Label(janela, text='Velocidade: 100', relief='flat', anchor=CENTER, font=(' Vernada 10 bold '), bg=cor0, fg=cor1)
poke_velo.place(x=15,y=435)

# Criando frame Total

poke_total= Label(janela, text='Total: 100', relief='flat', anchor=CENTER, font=(' Vernada 10 bold '), bg=cor0, fg=cor1)
poke_total.place(x=15,y=460)

# Criando frame Habilidade

poke_status= Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=(' Vernada 20 bold '), bg=cor0, fg=cor1)
poke_status.place(x=180,y=310)

# Criando frame Habilidade 1

poke_habili1= Label(janela, text='Choque do Trovão 🌩️', relief='flat', anchor=CENTER, font=(' Vernada 10 bold '), bg=cor0, fg=cor1)
poke_habili1.place(x=195,y=360)

# Criando frame Habilidade 2

poke_habili2= Label(janela, text='Cabeçada', relief='flat', anchor=CENTER, font=(' Vernada 10 bold '), bg=cor0, fg=cor1)
poke_habili2.place(x=195,y=385)


#Criando botões para pokemos 

image_pok1= Image.open('images/cabeca-pikachu.png')
image_pok1= image_pok1.resize((40,40))
image_pok1= ImageTk.PhotoImage(image_pok1)

button_pok1=Button(janela,command=lambda:trocar_pok('Pikachu'), image=image_pok1, text='Pikachu', width=154, relief='raised', overrelief=GROOVE, compound=LEFT, padx=5, anchor=NW, font=('Vernada 12 bold'), bg=cor1, fg=cor0    )
button_pok1.place(x=375,y=10)

#Criando botões para pokemos 2 

image_pok2= Image.open('images/cabeca-bulbasaur.png')
image_pok2= image_pok2.resize((40,40))
image_pok2= ImageTk.PhotoImage(image_pok2)

button_pok2=Button(janela,command=lambda:trocar_pok('Bulbasaur'), image=image_pok2, text='Bulbasaur', width=154, relief='raised', overrelief=GROOVE, compound=LEFT, padx=5, anchor=NW, font=('Vernada 12 bold'), bg=cor1, fg=cor0    )
button_pok2.place(x=375,y=65)

#Criando botões para pokemos 3 

image_pok3= Image.open('images/cabeca-charmander.png')
image_pok3= image_pok3.resize((40,40))
image_pok3= ImageTk.PhotoImage(image_pok3)

button_pok3=Button(janela,command=lambda:trocar_pok('Charmander'), image=image_pok3, text='Charmander', width=154, relief='raised', overrelief=GROOVE, compound=LEFT, padx=5, anchor=NW, font=('Vernada 12 bold'), bg=cor1, fg=cor0    )
button_pok3.place(x=375,y=120)

#Criando botões para pokemos 4 

image_pok4= Image.open('images/cabeca-gyarados.png')
image_pok4= image_pok4.resize((40,40))
image_pok4= ImageTk.PhotoImage(image_pok4)

button_pok4=Button(janela,command=lambda:trocar_pok('Gyarados'), image=image_pok4, text='Gyarados', width=154, relief='raised', overrelief=GROOVE, compound=LEFT, padx=5, anchor=NW, font=('Vernada 12 bold'), bg=cor1, fg=cor0    )
button_pok4.place(x=375,y=175)

#Criando botões para pokemos 5 

image_pok5= Image.open('images/cabeca-gengar.png')
image_pok5= image_pok5.resize((40,40))
image_pok5= ImageTk.PhotoImage(image_pok5)

button_pok5=Button(janela,command=lambda:trocar_pok('Gengar'), image=image_pok5, text='Gengar', width=154, relief='raised', overrelief=GROOVE, compound=LEFT, padx=5, anchor=NW, font=('Vernada 12 bold'), bg=cor1, fg=cor0    )
button_pok5.place(x=375,y=230)

#Criando botões para pokemos 6 

image_pok6= Image.open('images/cabeca-dragonite.png')
image_pok6= image_pok6.resize((40,40))
image_pok6= ImageTk.PhotoImage(image_pok6)

button_pok6=Button(janela,command=lambda:trocar_pok('Dragonite'), image=image_pok6, text='Dragonite', width=154, relief='raised', overrelief=GROOVE, compound=LEFT, padx=5, anchor=NW, font=('Vernada 12 bold'), bg=cor1, fg=cor0    )
button_pok6.place(x=375,y=285)

import random
Lista_poks=['Dragonite','Gengar','Charmander','Pikachu','Gyarados','Bulbasaur']
poke_escolhido= random.sample(Lista_poks, 1)

trocar_pok(poke_escolhido[0])

#print(poke_escolhido)

janela.mainloop()

