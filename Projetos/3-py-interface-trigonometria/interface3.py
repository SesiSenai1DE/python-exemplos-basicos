import tkinter as tk #Biblioteca para criação de interface
import math #Biblioteca para realizar operações matemáticas
from PIL import Image, ImageTk #Manipula imagens
import os #Arquivos de sistema
import sys #Variáveis de sistema

def resource_path(relative_path):
    """ 
    Obtém o caminho absoluto para o recurso, funciona tanto em ambiente de desenvolvimento 
    quanto após o empacotamento com PyInstaller.
    """
    try:
        # PyInstaller cria um diretório temporário e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Se não estiver executando pelo PyInstaller, utiliza o caminho absoluto do diretório atual
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)  # Retorna o caminho completo do arquivo

# Configuração da janela principal
janela = tk.Tk() #Cria a janela principal
janela.title("Calculadora Trigonométrica") #Título
janela.geometry("400x550") #Tamanho
janela.configure(bg="#f0f0f0") #Cor de fundo

# Carregar e definir o ícone da janela
try:
    icone_path = resource_path("seno.png")  # Obtém o caminho da imagem do ícone
    icone = Image.open(icone_path)  # Abre a imagem do ícone
    icone = ImageTk.PhotoImage(icone)  # Converte a imagem para um formato compatível com Tkinter
    janela.iconphoto(True, icone)  # Define a imagem como ícone da janela
except FileNotFoundError:
    print("Imagem 'seno.png' não encontrada para o ícone")  # Caso o arquivo não seja encontrado, exibe uma mensagem de erro

# Imagem seno2.png
try:
    imagem_path = resource_path("seno2.png")  # Obtém o caminho da imagem principal
    imagem = Image.open(imagem_path)  # Abre a imagem
    imagem = imagem.resize((380, 200), Image.LANCZOS)  # Redimensiona a imagem
    foto = ImageTk.PhotoImage(imagem)  # Converte a imagem para um formato compatível com Tkinter
    label_imagem = tk.Label(janela, image=foto, bg="#f0f0f0", borderwidth=0)  # Cria um label para exibir a imagem
    label_imagem.image = foto  # Mantém uma referência da imagem para evitar que o garbage collector a remova
    label_imagem.pack(pady=20)  # Posiciona a imagem na janela
except FileNotFoundError:
    # Caso a imagem não seja encontrada, exibe uma mensagem de texto no lugar da imagem
    label_imagem = tk.Label(janela, text="Imagem 'seno2.png' não encontrada", bg="#f0f0f0")
    label_imagem.pack(pady=20)


# Iniciar Janela
janela.mainloop() #Roda a tela e mantem aberta