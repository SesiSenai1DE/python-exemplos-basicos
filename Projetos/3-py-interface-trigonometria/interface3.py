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

def validar_entrada(texto):
    """
    Valida a entrada do usuário permitindo apenas números e garantindo que o valor esteja entre 0 e 90.
    """
    if texto.isdigit() or texto == "":  # Permite apenas números ou campo vazio
        if texto == "":  # Se o campo estiver vazio, permite a entrada
            return True
        valor = int(texto)  # Converte o texto para inteiro
        return 0 <= valor <= 90  # Retorna True se o valor estiver entre 0 e 90, caso contrário False
    return False  # Se o texto não for um número, retorna False

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

# Entrada do ângulo
frame_entrada = tk.Frame(janela, bg="#f0f0f0")  # Cria um frame para organizar a entrada
frame_entrada.pack(pady=10)  # Posiciona o frame na janela com um espaçamento vertical

label_angulo = tk.Label(frame_entrada, text="Ângulo (0 à 90):", font=('Arial', 14), bg="#f0f0f0")  # Label para o campo de entrada
label_angulo.pack(pady=(0, 5))  # Posiciona o label com um pequeno espaçamento inferior

validacao = janela.register(validar_entrada)  # Registra a função de validação para a entrada
entrada_angulo = tk.Entry(frame_entrada, width=3, justify='center', font=('Arial', 16), 
                          bd=0, highlightthickness=0, relief='flat', bg="#f0f0f0", fg='red',
                          validate="key", validatecommand=(validacao, '%P'))  # Cria o campo de entrada do ângulo
entrada_angulo.pack()  # Posiciona o campo de entrada

# Linha abaixo do campo de entrada
linha = tk.Frame(frame_entrada, bg="black", height=1, width=entrada_angulo.winfo_reqwidth())  # Cria uma linha decorativa abaixo do campo de entrada
linha.pack(pady=(0,5))  # Posiciona a linha com um pequeno espaçamento inferior


# Iniciar Janela
janela.mainloop() #Roda a tela e mantem aberta