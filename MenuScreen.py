import tkinter as tk
from MathQuizApp import MathQuizApp

class MenuScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz Menu")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="black")

        self.frame = tk.Frame(root, bg="black")S
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label = tk.Label(self.frame, text="Select your name:", font=("Comic Sans MS", 18), bg="black", fg="white")
        self.label.pack(pady=20)

        self.names = ["Aisha", "Ibrahim", "Musa"]
        self.selected_name = tk.StringVar()
        self.selected_name.set("")

        for name in self.names:
            tk.Radiobutton(self.frame, text=name, variable=self.selected_name, value=name, font=("Comic Sans MS", 14), bg="black", fg="white").pack()

        self.start_button = tk.Button(self.frame, text="Start Quiz", command=self.start_quiz, font=("Comic Sans MS", 16), bg="black", fg="white")
        self.start_button.pack(pady=30)

    def start_quiz(self):
        selected_name = self.selected_name.get()
        if selected_name:
            self.root.destroy()
            root = tk.Tk()
            app = MathQuizApp(root)
            root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    menu = MenuScreen(root)
    root.mainloop()
