# para fazer a calculadora, usarei a blibioteca Tkinter
import tkinter as tk

# Criando Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x580")
janela.configure(bg="#313131")

# Criando cor aos botões

fonte_botao = ("Segoe UI", 14, "bold")

# Cores dos botões
cor_num = "#3a3a3a"
cor_op = "#ff9500"
cor_igual = "#34c759"
cor_clear = "#ff3b30"

# bloquear redimensionamento
janela.resizable(False, False)

# Criar variavel para quando der erro, digitação limpa
erro = False

# Definições
# Função dos botões

def clicar(valor):
    global erro

    if erro:
        visor.delete(0, tk.END)
        erro = False

    visor.insert(tk.END, valor)


# Função do C (apagar tudo)
def limpar():
    visor.delete(0, tk.END)

# Função de apagar um por vez
def apagar_um():
    texto = visor.get()
    if len(texto) > 0:
        visor.delete(len(texto)-1, tk.END)

# Função das operaçoes matematicas
def calcular():
    global erro

    conta = visor.get()
    conta = conta.replace("X", "*")
    conta = conta.replace("÷", "/")
    conta = conta.replace(",", ".")
    conta = conta.replace("%", "/100")

    try:
        resultado = round(eval(conta), 2)

        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))

    except ZeroDivisionError:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Zero não é divisível")
        erro = True

    except:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Inválido")
        erro = True

# Função para os numeros do teclado
def teclado(event):
    tecla = event.char

    teclas_permitidas = "0123456789+-*/.,%"

    if tecla in teclas_permitidas:
        clicar(tecla)
    
    elif event.keysym == "Return":
        calcular()

    elif event.keysym == "KP_Enter":
        calcular()

    elif event.keysym == "BackSpace":
        apagar_um()

    return "break"

# Faz o enter do teclado dar =
janela.bind("<Return>", lambda event: calcular())
janela.bind("<KP_Enter>", lambda event: calcular())

# x = lado, y = subir
# width = largura
# height = altura

num0 = tk.Button(
    janela,
    text="0",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("0")
)
num0.place(x=22, y=470)

virg = tk.Button(
    janela,
    text=",",
    width=6,
    height=3,
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar(","))
virg.place(x=113, y=470)

igual = tk.Button(
    janela, 
    text="=",
    width=14, 
    height=3, 
    font=fonte_botao,
    bg=cor_igual,
    fg="white",
    bd=0,
    command=calcular) 
igual.place(x=206, y=470)

num1 = tk.Button(
    janela, 
    text="1",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("1"))
num1.place(x=22, y=381)

num2 = tk.Button(
    janela, 
    text="2",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("2"))

num2.place(x=113, y=381)

num3 = tk.Button(
    janela, 
    text="3",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("3"))
num3.place(x=204, y=381)

num4 = tk.Button(
    janela,    
    text="4",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("4"))
num4.place(x=22, y=293)

num5 = tk.Button(
    janela, 
    text="5",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("5"))
num5.place(x=113, y=293)

num6 = tk.Button(
    janela, 
    text="6",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("6"))
num6.place(x=204, y=293)

num7 = tk.Button(
    janela, 
    text="7",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("7"))
num7.place(x=22, y=205)

num8 = tk.Button(
    janela, 
    text="8",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("8"))
num8.place(x=113, y=205)

num9 = tk.Button(
    janela, 
    text="9",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("9"))
num9.place(x=204, y=205)

mais = tk.Button(janela, 
    text="+",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("+"))
mais.place(x=295, y=381)

menos = tk.Button(
    janela, 
    text="-",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("-"))
menos.place(x=295, y=293)

vezes = tk.Button(
    janela, 
    text="X",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("X"))
vezes.place(x=295, y=205)

clear = tk.Button(
    janela, 
    text="C",
    width=6, 
    height=3, 
    font=fonte_botao,
    bg=cor_clear,
    fg="white",
    bd=0,
    command=limpar) #tem q apagar o visor
clear.place(x=22, y=117)

back = tk.Button(
    janela,
    text="⌫",
    width=6,
    height=3,
    font=fonte_botao,
    bg=cor_op,
    fg="white",
    bd=0,
    command=apagar_um
)
back.place(x=113, y=117)

porc = tk.Button(
    janela, 
    text="%",
    width=6, 
    height=3, 
     font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("%")) #tem q fazer %
porc.place(x=204, y=117)

divido = tk.Button(
    janela, 
    text="÷",
    width=6, 
    height=3, 
     font=fonte_botao,
    bg=cor_num,
    fg="white",
    bd=0,
    command=lambda: clicar("÷")) #tem q fazer divisão
divido.place(x=295, y=117)

# Criando visor e adicionando cor e fonte
visor = tk.Entry(
    janela,
    font=("Segoe UI", 28),
    justify="right",
    bd=0,
    bg="#1E1E1E",
    fg="white",
    insertbackground="white"
)
visor.place(x=20, y=30, width=360, height=70)

# Conectar o teclado ao visor
visor.bind("<Key>", teclado)

# focar ele para digitar direto
visor.focus()

# x = lado, y = subir
janela.mainloop()
