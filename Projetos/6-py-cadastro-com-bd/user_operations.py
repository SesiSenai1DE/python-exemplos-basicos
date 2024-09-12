from tkinter import messagebox

# Inicializa a classe com ref. BD e a UI
class UserOperations:
    def __init__(self, db, ui):
        self.db = db
        self.ui = ui

# Cadastrar um novo usuario no banco de dados
def cadastrar(self):
    nome = self.ui.nome_entry.get()
    if nome:
        self.db.insert_user(nome)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.ui.nome_entry.delete(0, 'end')
        self.ui.carregar_dados()
    else:
        messagebox.showerror("Erro", "Por favor, preencha o campo Nome.")

# Atualizar um usuario existente no banco de dados
def atualizar_usuario(self):
    if self.ui.selected_user:
        novo_nome = self.ui.nome_entry.get()
        if novo_nome:
            self.db.update_user(self.ui.select_user[0], novo_nome)
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
            self.ui.carregar_dados()
            self.ui.nome_entry.delete(0, 'end')
            self.ui.selected_user = None
        else:
            messagebox.showerror("Erro", "Por favor, preencha o campo Nome.")
    else:
       messagebox.showerror("Erro", "Por favor, selecione um usuário para atualizar.")

# Excluir um usuario no banco de dados
def excluir_usuario(self):
    if self.ui.selected_user:
      if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir o usuário?"):
        self.db.delete_user(self.ui.select_user[0])
        messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
        self.ui.carregar_dados()
        self.ui.nome_entry.delete(0, 'end')
        self.ui.selected_user = None
    else:
        messagebox.showerror("Erro", "Por favor, selecione um usuário para excluir.")