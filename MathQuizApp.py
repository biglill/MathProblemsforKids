import tkinter as tk
from MathProblemGenerator import MathProblemGenerator

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        self.root.attributes('-fullscreen', True)
        self.root.wm_attributes('-topmost', True)

        self.correct_answers = 0
        self.math_problem_generator = MathProblemGenerator()

        self.root.configure(bg="black")
        font = ("Comic Sans MS", 18)
        fg_color = "white"

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.frame = tk.Frame(self.root, bg="black")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.problem_label = tk.Label(self.frame, text="", font=("Comic Sans MS", 48), bg="black", fg=fg_color)
        self.problem_label.grid(row=0, column=0, pady=50, columnspan=2)

        self.entry = tk.Entry(self.frame, font=font, bg="black", fg=fg_color)
        self.entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        self.entry.bind('<Return>', self.check_answer)

        self.check_button = tk.Button(self.frame, text="Check", command=self.check_answer, font=font, bg="black", fg=fg_color, width=10, height=2)
        self.check_button.grid(row=2, column=0, pady=20, columnspan=2)

        self.status_label = tk.Label(self.frame, text="", font=("Comic Sans MS", 36), bg="black", fg="white")
        self.status_label.grid(row=3, column=0, pady=10, columnspan=2)

        self.close_button = tk.Button(self.frame, text="Close", command=self.close_program, font=("Comic Sans MS", 18), bg="black", fg="white", width=10, height=2)

        self.new_problem()

    def check_answer(self, event=None):
        user_answer = self.entry.get()
        try:
            user_answer = int(user_answer)
            if user_answer == self.math_problem_generator.solution:
                self.correct_answers += 1
                self.status_label.config(text=f"Correct! {10 - self.correct_answers} problems left", font=("Comic Sans MS", 36))
                self.entry.delete(0, tk.END)
                if self.correct_answers == 10:
                    self.status_label.config(text="Congratulations! You can play the computer now.")
                    self.close_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
                    self.entry.grid_remove()
                    self.check_button.grid_remove()
                    self.problem_label.grid_forget()
                else:
                    self.new_problem()
            else:
                self.status_label.config(text="Incorrect. Try again.")
                self.entry.delete(0, tk.END)
        except ValueError:
            self.status_label.config(text="Please enter a valid whole number.")
            self.entry.delete(0, tk.END)

    def close_program(self):
        self.root.destroy()

    def new_problem(self):
        problem, solution = self.math_problem_generator.generate_math_problem()
        self.problem_label.config(text=problem)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
