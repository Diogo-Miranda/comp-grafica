import tkinter as tk
from customtkinter.windows.widgets.scaling.scaling_base_class import CTkScalingBaseClass
import customtkinter as ctk
from image_workspace import ImageWorkspace
import sys

# Classe que referencia o container prinipal da aplicação
class MainWindow(CTkScalingBaseClass):
    
    def flood_fill(self):
        self.canvas.flood_fill(int(self.flood_x1_entry.get()), int(self.flood_y1_entry.get()), "blue")

    def boundary_fill(self):
        self.canvas.flood_fill(int(self.boundary_x1_entry.get()), int(self.boundary_y1_entry.get()), "blue")

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

    def run_dda(self):
        self.canvas.dda(
            int(self.dda_x1_entry.get()),
            int(self.dda_x1_entry.get()),
            int(self.dda_x2_entry.get()),
            int(self.dda_y2_entry.get()))
        
    def run_bres(self):
        self.canvas.bres(
            int(self.bres_x1_entry.get()),
            int(self.bres_x1_entry.get()),
            int(self.bres_x2_entry.get()),
            int(self.bres_y2_entry.get()))

    def __dda_custom_bar(self):
        self.dda_frame = ctk.CTkFrame(self.left_frame, width=300, height=100)

        self.dda_frame.grid(
            row=10,
            ipadx=10,
            padx=15)
    
        # x1 y1
        self.dda_x1_label = ctk.CTkLabel(
            self.dda_frame,
            text="x1", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.dda_x1_label.grid(row=0, column=0, pady=5)

        self.dda_x1_entry = ctk.CTkEntry(
            self.dda_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.dda_x1_entry.grid(row=0, column=1, pady=5)

        self.dda_y1_label = ctk.CTkLabel(
            self.dda_frame,
            text="y1", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.dda_y1_label.grid(row=0, column=2, pady=5)

        self.dda_y1_entry = ctk.CTkEntry(
            self.dda_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.dda_y1_entry.grid(row=0, column=3, pady=5)

        # x2 y2
        self.dda_x2_label = ctk.CTkLabel(
            self.dda_frame,
            text="x2", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.dda_x2_label.grid(row=1, column=0, pady=5)

        self.dda_x2_entry = ctk.CTkEntry(
            self.dda_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.dda_x2_entry.grid(row=1, column=1, pady=5)

        self.dda_y2_label = ctk.CTkLabel(
            self.dda_frame,
            text="y2", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.dda_y2_label.grid(row=1, column=2, pady=5)

        self.dda_y2_entry = ctk.CTkEntry(
            self.dda_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.dda_y2_entry.grid(row=1, column=3, pady=5)

    def __flood_custom_bar(self):
        self.flood_frame = ctk.CTkFrame(self.left_frame, width=300, height=100)

        self.flood_frame.grid(
            column=1,
            row=1,
            ipadx=10,
            padx=15)
    
        # x1 y1
        self.flood_x1_label = ctk.CTkLabel(
            self.flood_frame,
            text="x1", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.flood_x1_label.grid(row=0, column=0, pady=5)

        self.flood_x1_entry = ctk.CTkEntry(
            self.flood_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.flood_x1_entry.grid(row=0, column=1, pady=5)

        self.flood_y1_label = ctk.CTkLabel(
            self.flood_frame,
            text="y1", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.flood_y1_label.grid(row=0, column=2, pady=5)

        self.flood_y1_entry = ctk.CTkEntry(
            self.flood_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.flood_y1_entry.grid(row=0, column=3, pady=5)

    def __boundary_custom_bar(self):
        self.boundary_frame = ctk.CTkFrame(self.left_frame, width=300, height=100)

        self.boundary_frame.grid(
            column=1,
            row=3,
            ipadx=10,
            padx=15)
    
        # x1 y1
        self.boundary_x1_label = ctk.CTkLabel(
            self.boundary_frame,
            text="x1", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.boundary_x1_label.grid(row=0, column=0, pady=5)

        self.boundary_x1_entry = ctk.CTkEntry(
            self.boundary_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.boundary_x1_entry.grid(row=0, column=1, pady=5)

        self.boundary_y1_label = ctk.CTkLabel(
            self.boundary_frame,
            text="y1", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.boundary_y1_label.grid(row=0, column=2, pady=5)

        self.boundary_y1_entry = ctk.CTkEntry(
            self.boundary_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.boundary_y1_entry.grid(row=0, column=3, pady=5)

    def __bres_custom_bar(self):
        self.bres_frame = ctk.CTkFrame(self.left_frame, width=300, height=100)

        self.bres_frame.grid(
            row=12,
            ipadx=10,
            padx=15)
    
        # x1 y1
        self.bres_x1_label = ctk.CTkLabel(
            self.bres_frame,
            text="x1", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.bres_x1_label.grid(row=0, column=0, pady=5)

        self.bres_x1_entry = ctk.CTkEntry(
            self.bres_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.bres_x1_entry.grid(row=0, column=1, pady=5)

        self.bres_y1_label = ctk.CTkLabel(
            self.bres_frame,
            text="y1", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.bres_y1_label.grid(row=0, column=2, pady=5)

        self.bres_y1_entry = ctk.CTkEntry(
            self.bres_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.bres_y1_entry.grid(row=0, column=3, pady=5)

        # x2 y2
        self.bres_x2_label = ctk.CTkLabel(
            self.bres_frame,
            text="x2", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.bres_x2_label.grid(row=1, column=0, pady=5)

        self.bres_x2_entry = ctk.CTkEntry(
            self.bres_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.bres_x2_entry.grid(row=1, column=1, pady=5)

        self.bres_y2_label = ctk.CTkLabel(
            self.bres_frame,
            text="y2", 
            fg_color="transparent",
            font=('Sans-serif', 15))
        self.bres_y2_label.grid(row=1, column=2, pady=5)

        self.bres_y2_entry = ctk.CTkEntry(
            self.bres_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15),
            width=75)
        self.bres_y2_entry.grid(row=1, column=3, pady=5)

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

        self.x_label = ctk.CTkLabel(
            self.left_frame,
            text=X_LABEL_NAME, 
            fg_color="transparent",
            font=('Sans-serif', 15))

        self.x_label.grid(row=5, column=0, ipadx=35)

        self.x_entry = ctk.CTkEntry(
            self.left_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15))
        
        self.x_entry.grid(row=6, column=0, ipadx=35)

        self.y_label = ctk.CTkLabel(
            self.left_frame,
            text=Y_LABEL_NAME, 
            fg_color="transparent",
            font=('Sans-serif', 15))
        
        self.y_label.grid(row=7, column=0, ipadx=35)
        
        self.y_entry = ctk.CTkEntry(
            self.left_frame, 
            placeholder_text="0",
            fg_color="transparent",
            font=('Sans-serif', 15))
        
        self.y_entry.grid(row=8, column=0, ipadx=35)
        
        self.dda_button = ctk.CTkButton(
            self.left_frame,
            text="DDA",
            font=('Sans-serif', 15),
            command=self.run_dda)
        
        self.dda_button.grid(row=9, column=0, pady=15, padx=50)

        self.__dda_custom_bar()

        self.bres_button = ctk.CTkButton(
                    self.left_frame,
                    text="BRES",
                    font=('Sans-serif', 15),
                    command=self.run_bres)
                
        self.bres_button.grid(row=11, column=0, pady=15, padx=50)

        # row 13
        self.__bres_custom_bar()

        self.flood_button = ctk.CTkButton(
            self.left_frame,
            text="Flood",
            font=('Sans-serif', 15),
            command=self.flood_fill)
        
        # Row 0
        self.flood_button.grid(row=0, column=1, pady=15, padx=50)
        
        # Row 1
        self.__flood_custom_bar()

        self.boundary_button = ctk.CTkButton(
            self.left_frame,
            text="Boundary",
            font=('Sans-serif', 15),
            command=self.boundary_fill)
        
        # Row 2
        self.boundary_button.grid(row=2, column=1, pady=15, padx=50)
        
        self.__boundary_custom_bar()

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

X_LABEL_NAME = "x"
Y_LABEL_NAME = "y"

root = ctk.CTk()

print(sys.getrecursionlimit())

root.geometry("1366x768")
sys.setrecursionlimit(100000000)

app = MainWindow(root)
root.mainloop()