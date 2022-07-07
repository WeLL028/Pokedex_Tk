#Importanto tkinter
from tkinter import *
from tkinter import ttk

from setuptools import Command

#Cores 

cor1 = '#1e1f1e' # preto 
cor2 = '#feffff' # branco
cor3 = '#38576b' # azul
cor4 = '#ECEFF1' # cizenta 
cor5 = '#FFAB40' # laranja



#Criar a Janela da Calculadora e fazer as configurações Basicas 

janela =Tk()
janela.title("Calcu By WeLL") # Titulo da calculadora
janela.geometry("235x310") # Definição largura e comprimento
janela.config(bg=cor1) # Configuração da cor da calculadora 

# Criando Frames
frame_tela = Frame(janela, width=235, height=50,bg=cor3) # Dispplay
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela, width=235, height=268,) # 2 Frame corpo da calculadora onde vai os botões
frame_corpo.grid(row=1,column=0)


#Criando Label >> uma tela.

valor_texto=StringVar() 

#Variavél todos valores 

todos_valores = '' ## todos os valores estão sendo armazenados nessa variávél. 

# Logica da Calculadora Operaçãoes # Criando função


def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    #resultado= eval(todos_valores)

#Passando valor para tela

    valor_texto.set(todos_valores)

#Função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)    
    
    valor_texto.set(str(resultado)) # Mostrando valor na tela da calculadora 


#Função Limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')






app_label=Label(frame_tela, textvariable=valor_texto,width=16,height=2,padx=7
,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 16'),bg=cor3,fg=cor2)
app_label.place(x=0,y=0)


# Criando Botoẽs # command=lambda:entrar_valores(''),


b_1=Button(frame_corpo, command=limpar_tela ,text='C', width=11, height=2,bg=cor4,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)# Botão clear #limpar opereção
b_1.place(x=0, y=0) # x horinzontal y vertical

b_2=Button(frame_corpo,command=lambda:entrar_valores('%'),text='%', width=4, height=2, bg=cor4,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) #Botão %resto da divisão
b_2.place(x=118, y=0) 

b_3=Button(frame_corpo,command=lambda:entrar_valores('/'), text='/', width=4, height=2, bg=cor5,fg=cor2,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # Botão divisão
b_3.place(x=177, y=0) 

b_4=Button(frame_corpo,command=lambda:entrar_valores('7'), text='7', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # Botão 7
b_4.place(x=0, y=52) 

b_5=Button(frame_corpo,command=lambda:entrar_valores('8'), text='8', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # Botão 8
b_5.place(x=59, y=52) 

b_6=Button(frame_corpo,command=lambda:entrar_valores('9'), text='9', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # botao 9
b_6.place(x=118, y=52) 

b_7=Button(frame_corpo,command=lambda:entrar_valores('*'), text='*', width=5, height=2, bg=cor5,fg=cor2,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # botão Multiplicação
b_7.place(x=177, y=52)

b_8=Button(frame_corpo,command=lambda:entrar_valores('4'), text='4', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # Botão 4
b_8.place(x=0, y=104) 

b_9=Button(frame_corpo,command=lambda:entrar_valores('5'), text='5', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # Botão 5
b_9.place(x=59, y=104) 

b_10=Button(frame_corpo,command=lambda:entrar_valores('6'), text='6', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # botao 6
b_10.place(x=118, y=104) 

b_11=Button(frame_corpo,command=lambda:entrar_valores('-'), text='-', width=5, height=2, bg=cor5,fg=cor2,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # botão Subtração
b_11.place(x=177, y=104)

b_12=Button(frame_corpo, command=lambda:entrar_valores('1'),text='1', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # Botão 1
b_12.place(x=0, y=156) 

b_13=Button(frame_corpo,command=lambda:entrar_valores('2'), text='2', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # Botão 2
b_13.place(x=59, y=156) 

b_14=Button(frame_corpo,command=lambda:entrar_valores('3'), text='3', width=4, height=2, bg=cor4,fg=cor1,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # botao 3
b_14.place(x=118, y=156) 

b_15=Button(frame_corpo,command=lambda:entrar_valores('+'), text='+', width=5, height=2, bg=cor5,fg=cor2,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # botão de Soma
b_15.place(x=177, y=156)

b_16=Button(frame_corpo,command=lambda:entrar_valores('0'), text='0', width=11, height=2,bg=cor4,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)# Botão 0
b_16.place(x=0, y=208) # x horinzontal y vertical

b_17=Button(frame_corpo,command=lambda:entrar_valores('.'), text='.', width=4, height=2, bg=cor4,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) #Botão de ponto
b_17.place(x=118, y=208) 

b_18=Button(frame_corpo,command=calcular, text='=', width=4, height=2, bg=cor5,fg=cor2,
font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE) # Botão de Igual =
b_18.place(x=177, y=208) 


janela.mainloop() # Laço principal 
