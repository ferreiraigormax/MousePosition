from pyautogui import position
from time import sleep
from tkinter import *
def posicao():
    x, y = position()
    root.after(2000, posicao) # .after cria a repeticao da funcao "posicao" em 2000 milisegundos
    resposta_x.set(str(x))
    resposta_y.set(str(y))

# Definições do programa
root = Tk()
root.geometry('250x50+0+0')
root.title('Position v1.0')
root.resizable(width=False, height=False)
# String Variavéis do programa
resposta_x = StringVar()
resposta_y = StringVar()
# Definindo os Widgets do programa
label1 = Label(root, text='Posição X', font='Arial, 8')
label2 = Label(root, text='Posição Y', font='Arial, 8')
label3 = Label(root, textvariable=resposta_x, font='Consolas, 12')
label4 = Label(root, textvariable=resposta_y, font='Consolas, 12')
# Organizando os Widgets do programa
label1.grid(row=0, column=0, ipadx=35)
label2.grid(row=0, column=1, ipadx=35)
label3.grid(row=1, column=0, ipadx=35)
label4.grid(row=1, column=1, ipadx=35)


root.after(2000, posicao) # Criar a repetição da função "posicao"
root.mainloop()