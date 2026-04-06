import tkinter as tk
import random

class Magic8Ball:
    def __init__(self, root):
        self.root = root
        self.root.title("La Boule de Cristal")
        self.root.geometry("350x450")
        self.root.configure(bg='#2c3e50')

        # Titre
        self.label = tk.Label(root, text="Posez une question dans votre tête\net cliquez sur le bouton !", 
                              fg="white", bg="#2c3e50", font=("Helvetica", 12), wraplength=280)
        self.label.pack(pady=30)

        # Zone de la boule
        self.canvas = tk.Canvas(root, width=200, height=200, bg='#2c3e50', highlightthickness=0)
        self.canvas.pack()
        # Le cercle noir de la boule
        self.canvas.create_oval(10, 10, 190, 190, fill="#000000", outline="#ecf0f1", width=3)
        # Le texte de réponse à l'intérieur
        self.answer_text = self.canvas.create_text(100, 100, text="?", fill="#3498db", font=("Helvetica", 16, "bold"), width=150, justify="center")

        # Bouton
        self.button = tk.Button(root, text="Demander au destin !", command=self.get_answer, 
                                bg="#e74c3c", fg="white", font=("Helvetica", 11, "bold"), 
                                relief="flat", padx=20, pady=10, cursor="hand2")
        self.button.pack(pady=40)

        self.answers = [
            "Oui, absolument !",
            "C'est certain.",
            "Peut-être...",
            "Demande plus tard.",
            "Non, pas du tout.",
            "Ma réponse est non.",
            "Les astres disent oui.",
            "Absolument pas !",
            "Il y a un doute.",
            "Compte là-dessus !",
            "C'est très probable.",
            "Oublie ça.",
            "Signe clair !",
            "Pas maintenant."
        ]

    def get_answer(self):
        answer = random.choice(self.answers)
        self.canvas.itemconfig(self.answer_text, text=answer, fill="#ecf0f1")
        self.label.config(text="Le destin dit :")

if __name__ == "__main__":
    root = tk.Tk()
    app = Magic8Ball(root)
    root.mainloop()
