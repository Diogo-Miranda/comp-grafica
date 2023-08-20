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
    
    def set_active_tool(self):
        self.canvas.active_tool = self.tolls_optionmenu_var.get()
    
    def set_rubber_as_tool(self):
        self.canvas.active_tool = "Rubber"

    def set_active_tool(self):
        self.canvas.current_color = self.colors_optionmenu_var.get()

    def __load_custom_bar(self):
         # # Cria um frame lateral para a barra de customizações
        self.left_frame = ctk.CTkFrame(root, width=300, height=600)

        self.tolls_optionmenu_var = ctk.StringVar(value="Pen")

        tolls = self.canvas.tolls

        self.tolls_option_menu = ctk.CTkOptionMenu(
            self.left_frame,
            values=tolls,
            variable=self.tolls_optionmenu_var)

        self.tolls_option_menu.grid(row=0, column=0, pady=15, padx=10)

        self.draw_button = ctk.CTkButton(
            self.left_frame,
            text="Draw",
            font=('Sans-serif', 15),
            command=self.set_active_tool)
        
        self.draw_button.grid(row=1, column=0, pady=15, padx=50)

        self.erase_button = ctk.CTkButton(
            self.left_frame,
            text="Erase",
            font=('Sans-serif', 15),
            command=self.set_rubber_as_tool)
        
        self.erase_button.grid(row=2, column=0, pady=15, padx=50)

        # Posiciona no centro da tela
        self.left_frame.grid(
            row=0, 
            column=1, 
            sticky="nsew",
            ipadx=10,
            padx=15)
        
        self.colors_optionmenu_var = ctk.StringVar(value="black")

        colors = self.canvas.colors

        self.colors_option_menu = ctk.CTkOptionMenu(
            self.left_frame,
            values=colors,
            variable=self.colors_optionmenu_var)

        self.colors_option_menu.grid(row=3, column=0, pady=15, padx=10)

        self.color_button = ctk.CTkButton(
            self.left_frame,
            text="Pick color",
            font=('Sans-serif', 15),
            command=self.set_active_tool)
        
        self.color_button.grid(row=4, column=0, pady=15, padx=50)

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

        self.set_active_tool()


root = ctk.CTk()

root.geometry("1366x768")

app = MainWindow(root)
root.mainloop()