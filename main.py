import tkinter as tk
from customtkinter.windows.widgets.scaling.scaling_base_class import CTkScalingBaseClass
import customtkinter as ctk
from image_workspace import ImageWorkspace

# Classe que referencia o container prinipal da aplicação
class MainWindow(CTkScalingBaseClass):

    def __load_canvas(self):
        # Cria o canvas image inicial
        self.canvas = ImageWorkspace(self.master)  # create widget

        # Posiciona no centro da tela
        self.canvas.grid(row=0, column=0)

    def __load_custom_bar(self):
         # # Cria um frame lateral para a barra de customizações
        self.left_frame = ctk.CTkFrame(root, width=300, height=600)
        # self.left_frame.configure(width=400)

        # Posiciona no centro da tela
        self.left_frame.grid(
            row=0, 
            column=1, 
            sticky="nsew",
            ipadx=10,
            padx=15)

    def __init__(self, mainframe):
        # Inicializa o Frame inicial

        super().__init__(mainframe)
        self.master = mainframe

        # definiçao dos contrast elementares
        self.contrast_min = 0
        self.contrast_max = 255

        # Título da janela inicial
        self.master.title('Image Workspace')

        self.__load_canvas()
        self.__load_custom_bar()

        # Permite que o quadro inicial se expanda de forma responsiva
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)


root = ctk.CTk()

root.geometry("1366x768")

app = MainWindow(root)
root.mainloop()