from sympy import *
from sympy.parsing.sympy_parser import parse_expr 
from tkinter import * 

def derivada():
    try:
        x = symbols('x')
        fun_escrita = funcion.get()
        f = parse_expr(fun_escrita)
        derivada = diff(f,x)
        etiqueta.configure(text= derivada)
    except:
        etiqueta.configure(text= "Coloque a função correta")
        
        
def integral():
    try:
        x = symbols('x') 
        fun_escrita2 = funcion.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g,x)
        etiqueta.configure(text= integral)
    except:
        etiqueta.configure(text= "Coloque a função correta")
    
janela = Tk()
janela.geometry('400x280')
janela.title("Cálculo Diferencial e Integral: f(x)")

anuncio = Label(janela, text="Coloque a função de x:", font=("Arial", 15), fg="blue")
anuncio.pack()

funcion = Entry(janela, font=("Arial", 15))
funcion.pack()

etiqueta = Label(janela, text="Resultado", font=("Arial", 15), fg="red")
etiqueta.pack()

butao1 = Button(janela, text="Derivar Função", font=("Arial", 15), command=derivada)
butao1.pack()

butao2 = Button(janela, text="Integrar Função (integral indefinida)", font=("Arial", 15), command=integral)
butao2.pack()

def _quit(): #Função sair
    janela.quit()     #deleta o mainloop
    janela.destroy()  #elimina a janela da memoria
                    

butao3 = Button(master=janela, text="Sair", font=("Arial", 15), command=_quit)
butao3.pack()
janela.mainloop()