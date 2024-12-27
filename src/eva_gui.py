# Ejemplo básico de interfaz gráfica, puedes usar frameworks como Tkinter, PyQt, etc.
import tkinter as tk
from eva_core import EVACore

class EVA_GUI:
    def __init__(self, root):
        self.eva = EVACore()
        self.root = root
        self.root.title("EVA - Asistente Virtual")
        
        self.chat_log = tk.Text(root)
        self.chat_log.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(root, text="Enviar", command=self.send_message)
        self.send_button.pack()

    def send_message(self, event=None):
        user_input = self.entry.get()
        self.chat_log.insert(tk.END, f"Tú: {user_input}\n")
        response = self.eva.process_input(user_input)
        self.chat_log.insert(tk.END, f"EVA: {response}\n")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = EVA_GUI(root)
    root.mainloop()