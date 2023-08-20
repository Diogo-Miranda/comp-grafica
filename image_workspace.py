from tkinter import filedialog
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, colorchooser
from tkinter import Canvas, messagebox
from PIL import Image, ImageDraw
    
from enum import Enum
   
class ImageWorkspace:
    """ Mostra a imagem, zoom e filtros"""

    def __init__(self, placeholder):
        """ Iniciar a imagem inicial """
        self.__image_frame = ctk.CTkFrame(placeholder)     # Define um placeholder inicial para renderizar a image
        
        # Definição do workspace da imagem e atribuindo as barras de rolagem
        # Público para alteração por outras classes
        self.canvas = ctk.CTkCanvas(self.__image_frame,
                                highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nswe')
        self.canvas.update()

        # Setup variables
        self.tolls = ["Pen"]
        self.colors = ["black", "blue", "white", "yellow", "brown", "purple", "green"]

        self.active_tool = self.tolls[0]
        self.text_input = None
        self.current_color = "black"
        self.eraser_color = "white"

        # Atribuir botões para trabalhar em conjunto com o workspace
        self.__bind_keys()

    def __bind_keys(self):
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
    
    def start_drawing(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.active_tool == "Rubber":
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.eraser_color, width=5, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.last_x = x
            self.last_y = y
        elif self.active_tool == "Pen":
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.current_color, width=2, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.last_x = x
            self.last_y = y

    def set_active_tool(self, toll):
        self.active_tool = toll
    
    def stop_drawing(self, event):
        pass

    def grid(self, **kw):
        """ Inclui o widget em um frame do seu parent """
        self.__image_frame.grid(**kw)  # place CanvasImage widget on the grid
        self.__image_frame.grid(sticky='nswe')  # make frame container sticky
        self.__image_frame.rowconfigure(0, weight=1)  # make canvas expandable
        self.__image_frame.columnconfigure(0, weight=1)
