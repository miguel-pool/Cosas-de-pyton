import tkinter as tk

class Calculadora:
    def __int__(self, root):     
        self.root = root    
        #self.root.Tit('Calculadora Basica')
        #self.root.Configure(bg='#2b3e50')
        
        self.pantalla = tk.Entry(self.root,width=50, bg = "3b4b5b", borderwidth=5, fg="white")
        self.pantalla.grid(row=0, column = 0)
        
        
root = tk.Tk()
#Calculadora = Calculadora(root)
root.mainloop()