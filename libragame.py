import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk

# Definir as perguntas e imagens
perguntas = [
    ("letraA.png", "Qual é a capital do Brasil?"),
    ("letraApng", "Qual é o maior país do mundo?"),
    ("letraA.png", "Qual é a fórmula química da água?"),
    ("letraA.png", "Qual é a bandeira do Brasil?")
]

respostas_corretas = [
    "Brasília",
    "Rússia",
    "H2O",
    "Verde e amarelo"
]

opcoes_resposta = [
    ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
    ["China", "Rússia", "Canadá", "Estados Unidos"],
    ["NaCl", "CO2", "H2O", "CH4"],
    ["Verde e amarelo", "Azul e branco", "Vermelho e preto", "Verde e branco"]
]

# Definir a variável de vidas
vidas = 3

# Definir a variável do índice da pergunta atual
indice_pergunta = 0

# Criar a janela principal
janela = tk.Tk()
janela.geometry("640x480")
janela.title("Jogo de Perguntas")

# Criar os elementos da interface
titulo = tk.Label(text="Jogo de Perguntas", font=("Arial", 18))
titulo.pack()

# Carregar a imagem da pergunta atual
imagem_pergunta = Image.open(perguntas[indice_pergunta][0])
imagem_pergunta = imagem_pergunta.resize((300, 300))
photo_imagem_pergunta = ImageTk.PhotoImage(imagem_pergunta)

# Label para imagem da pergunta
label_imagem_pergunta = tk.Label(image=photo_imagem_pergunta)
label_imagem_pergunta.pack()

texto_pergunta = tk.Label(text=perguntas[indice_pergunta][1])
texto_pergunta.pack()

# Label para vidas
texto_vidas = tk.Label(text=f"Vidas: {vidas}", font=("Arial", 12))
texto_vidas.pack()

botoes_resposta = []

for i in range(len(opcoes_resposta[indice_pergunta])):
    botao = tk.Button(text=opcoes_resposta[indice_pergunta][i], command=lambda i=i: verificar_resposta(i))
    botoes_resposta.append(botao)
    botao.pack()

# Label para feedback
texto_feedback = tk.Label(text="", font=("Arial", 12))
texto_feedback.pack()

# Função para verificar a resposta
def verificar_resposta(i):
    global vidas, indice_pergunta

    if opcoes_resposta[indice_pergunta][i] == respostas_corretas[indice_pergunta]:
        texto_feedback.config(text="Resposta correta!")
        print("Resposta correta!")

        # Avançar para próxima pergunta
        if indice_pergunta < len(perguntas) - 1:
            indice_pergunta += 1

            # Carregar a imagem da próxima pergunta
            imagem_pergunta = Image.open(perguntas[indice_pergunta][0])
            imagem_pergunta = imagem_pergunta.resize((300, 300))
            photo_imagem_pergunta = ImageTk.PhotoImage(imagem_pergunta)

            # Atualizar a label da imagem
            label_imagem_pergunta.config(image=photo_imagem_pergunta)

            texto_pergunta.config(text=perguntas[indice_pergunta][1])
            for j in range(len(botoes_resposta)):
                botoes_resposta[j].config(text=opcoes_resposta[indice_pergunta][j])
        else:
            # Fim do jogo
            messagebox.showinfo("Parabéns!", "Você venceu o jogo!")
            janela.destroy()
    else:
        vidas -= 1
        texto_feedback.config(text="Resposta errada!")
        print("Resposta errada! Vidas restantes:", vidas)
        texto_vidas.config(text=f"Vidas: {vidas}")

    if vidas == 0:
        # Exibir caixa de diálogo
        messagebox.showinfo("Você perdeu!", f"Você perdeu!\nVidas restantes: {vidas}")

        # Fechar a janela principal
        janela.destroy()
