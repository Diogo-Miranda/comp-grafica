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
        self.pixel_colors = {}

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
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=1, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.last_x = x
            self.last_y = y 
            self.pixel_colors[(x, y)] = "black"

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
    
    def dda(self, x1, y1, x2, y2):
        self.__dda(x1, y1, x2, y2)
    
    def __dda(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        x_incr = 0
        y_incr = 0
        x, y = x1, y1
        steps = 0
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
        x_incr = dx / steps
        y_incr = dy / steps
        self.__set_pixel(round(x), round(y))
        for k in range(1, steps):
            x = x + x_incr
            y = y + y_incr
            self.__set_pixel(round(x), round(y))
    
    def bres(self, x1, y1, x2, y2):
        self.__bres(x1, y1, x2, y2)

    def __bres(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        incr_x = 0
        incr_y = 0
        
        if (dx >= 0):
            incr_x = 1
        else:
            incr_x = -1
            dx = -dx
        
        if (dy >= 0):
            incr_y = 1
        else:
            incr_y = -1
            dy = -dy
        
        x = x1
        y = y1
        self.__set_pixel(x, y)

        if (dy < dx):
            p = 2*dy - dx
            const_a = 2*dy
            const_b = 2*(dy - dx)
            for i in range(0, dx):
                x = x + incr_x
                if (p < 0):
                    p = p + const_a
                else:
                    y = y + incr_y
                    p = p + const_b
                self.__set_pixel(x, y)
        else:
            p = 2*dx - dy
            const_a = 2*dx
            const_b = 2*(dx - dy)
            for i in range(dy):
                y = y + incr_y
                if (p < 0):
                    p = p + const_a
                else:
                    x = x + incr_x
                    p = p + const_b
                self.__set_pixel(x, y)


    def flood_fill(self, x, y, fill_color):
        stack = [(x, y)]
        start_color = self.__get_pixel_color(x, y)

        if start_color == fill_color:
            return

        while stack:
            x, y = stack.pop()

            neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

            self.__paint_pixel(x, y, color=fill_color)

            for nx, ny in neighbors:
                if (0 <= nx < self.canvas.winfo_width() and 0 <= ny < self.canvas.winfo_height()):
                    neighbor_color = self.__get_pixel_color(nx, ny)
                    if neighbor_color == start_color  and not self.__is_border(nx, ny):
                        stack.append((nx, ny))
    
    def __boundary_fill(self, x, y, boundary_color, fill_color):
        if (
            x < 0
            or y < 0
            or x >= 200
            or y >= 200
        ):
            return

        current_color = self.__get_pixel_color(x, y)

        if current_color != boundary_color and current_color != fill_color:
            self.__paint_pixel(x, y, fill_color)
            self.__boundary_fill(x + 1, y, boundary_color, fill_color)
            self.__boundary_fill(x - 1, y, boundary_color, fill_color)
            self.__boundary_fill(x, y + 1, boundary_color, fill_color)
            self.__boundary_fill(x, y - 1, boundary_color, fill_color)

    def fill_shape_boundary(self, x, y, fill_color):
        boundary_color = self.current_color
        self.__boundary_fill(x, y, boundary_color, fill_color)


    def __set_pixel(self, x, y):
        self.canvas.create_rectangle(x, y, x + 1, y + 1, fill="black")
        self.pixel_colors[(x, y)] = "black"

    def __paint_pixel(self, x, y, color):
        self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)
        self.pixel_colors[(x, y)] = color
    
    def __get_pixel_color(self, x, y):
        return self.pixel_colors.get((x, y), None)

    def __is_border(self, x, y):
        pixel_color = self.__get_pixel_color(x, y)
        return pixel_color == "black"