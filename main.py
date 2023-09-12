import random
import tkinter as tk


def generate_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])

    if operator == '+':
        solution = num1 + num2
    else:
        # Ensure the result is non-negative
        if num1 < num2:
            num1, num2 = num2, num1
        solution = num1 - num2

    problem = f"What is {num1} {operator} {num2}?"

    return problem, solution


def check_answer(event=None):
    user_answer = entry.get()
    try:
        user_answer = int(user_answer)  # Parse as an integer
        if user_answer == solution:
            global correct_answers
            correct_answers += 1
            status_label.config(text=f"Correct! {10 - correct_answers} problems left", font=("Comic Sans MS", 36))
            entry.delete(0, tk.END)
            if correct_answers == 10:
                status_label.config(text="Congratulations! You can play the computer now.")
                close_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
                entry.grid_remove()
                check_button.grid_remove()
                problem_label.grid_forget()
            else:
                new_problem()
        else:
            status_label.config(text="Incorrect. Try again.")
            entry.delete(0, tk.END)
    except ValueError:
        status_label.config(text="Please enter a valid whole number.")
        entry.delete(0, tk.END)


def close_program():
    root.destroy()  # Close the program


def new_problem():
    global problem, solution
    problem, solution = generate_math_problem()
    problem_label.config(text=problem, font=("Comic Sans MS", 48))


root = tk.Tk()
root.title("Math Login")
root.attributes('-fullscreen', True)
root.wm_attributes('-topmost', True)

correct_answers = 0

root.configure(bg="black")
font = ("Comic Sans MS", 18)
fg_color = "white"

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = tk.Frame(root, bg="black")
frame.grid(row=0, column=0, sticky="nsew")

frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

problem_label = tk.Label(frame, text="", font=("Comic Sans MS", 48), bg="black", fg=fg_color)
problem_label.grid(row=0, column=0, pady=50, columnspan=2)

entry = tk.Entry(frame, font=font, bg="black", fg=fg_color)
entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
entry.bind('<Return>', check_answer)

check_button = tk.Button(frame, text="Check", command=check_answer, font=font, bg="black", fg=fg_color, width=10,
                         height=2)
check_button.grid(row=2, column=0, pady=20, columnspan=2)

status_label = tk.Label(frame, text="", font=("Comic Sans MS", 36), bg="black", fg="white")
status_label.grid(row=3, column=0, pady=10, columnspan=2)

# Initially, hide the "Close" button
close_button = tk.Button(frame, text="Close", command=close_program, font=("Comic Sans MS", 18), bg="black", fg="white",
                         width=10, height=2)

new_problem()

root.mainloop()
