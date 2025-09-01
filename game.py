import tkinter as tk
import random
import csv
import time
from googletrans import Translator
from tkinter import messagebox

# Main Window
window = tk.Tk()
window.title("Rock Your Decades - Guess the Song")
window.geometry("500x550")
window.configure(bg="#fce4ec")  # soft pink background

# Game Variables
game_duration = 30
current_question = ""
current_answer = ""
score = 0
player_name = ""
start_time = 0

translator = Translator()

# ---------------- Core Functions ---------------- #
def gen_question():
    """Pick a random song title from Songs.txt and translate it to Hindi."""
    with open("Songs.txt", "r", encoding="utf-8") as f:
        songs = f.readlines()
        ques = random.choice(songs).strip()
        ans = translator.translate(ques, dest="hi").text
    return ques, ans

def update_timer():
    """Update countdown timer every second."""
    global game_duration, start_time
    elapsed_time = int(time.time() - start_time)
    remaining_time = game_duration - elapsed_time

    if remaining_time <= 0:
        result_label.config(text="⏰ Time's up! The song was: " + current_question)
        guess_entry.config(state="disabled")
        submit_button.config(state="disabled")
        show_current_score()
    else:
        timer_label.config(text=f"⏳ Time remaining: {remaining_time} sec")
        window.after(1000, update_timer)

def show_rules():
    rules = """🎵 Guess the Song - Rules 🎵
1. A random song title will be selected.
2. Its Hindi translation will be shown.
3. You must guess the original English title.
4. Correct guess ➝ +1 score & +5 seconds.
5. Wrong guess ➝ -5 seconds.
6. Try to score as high as you can before time runs out!
"""
    messagebox.showinfo("Rules", rules)

def start_game():
    """Start game by generating first question."""
    global current_question, current_answer, start_time, score, game_duration
    score = 0
    game_duration = 30
    score_label.config(text="⭐ Score: 0")
    guess_entry.config(state="normal")
    submit_button.config(state="normal")

    current_question, current_answer = gen_question()
    messagebox.showinfo("Guess the Song", f"Translate this to English:\n\n👉 {current_answer}")

    start_time = time.time()
    update_timer()

def check_guess():
    """Check if user guess is correct."""
    global current_question, score, game_duration
    guess = guess_entry.get().strip()

    if guess.lower() == current_question.lower():
        messagebox.showinfo("Result", "✅ Correct!")
        score += 1
        game_duration += 5
    else:
        messagebox.showinfo("Result", f"❌ Wrong! Correct answer: {current_question}")
        game_duration -= 5

    show_current_score()
    next_round()

def next_round():
    """Generate next question automatically."""
    global current_question, current_answer
    current_question, current_answer = gen_question()
    guess_entry.delete(0, tk.END)
    messagebox.showinfo("Next Round", f"Translate this to English:\n\n👉 {current_answer}")

def save_score():
    """Save score to CSV."""
    with open("scores.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([player_name, score])

def show_scores():
    """Show leaderboard from scores.csv."""
    scores_window = tk.Toplevel(window)
    scores_window.title("Leaderboard")
    scores_window.configure(bg="#fff3e0")

    scores_label = tk.Label(scores_window, text="🏆 Leaderboard 🏆", font=("Arial", 16, "bold"), bg="#fff3e0")
    scores_label.pack(pady=10)

    try:
        with open("scores.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                score_text = f"Player: {row[0]} | Score: {row[1]}"
                score_display = tk.Label(scores_window, text=score_text, font=("Arial", 12), bg="#fff3e0")
                score_display.pack()
    except FileNotFoundError:
        tk.Label(scores_window, text="No scores yet!", font=("Arial", 12), bg="#fff3e0").pack()

def show_current_score():
    score_label.config(text="⭐ Score: " + str(score))

def get_name():
    """Get player name before starting."""
    global player_name
    player_name = name_entry.get().strip()
    if not player_name:
        messagebox.showwarning("Warning", "Please enter your name first!")
        return
    name_entry.pack_forget()
    name_label.pack_forget()
    start_button.pack_forget()
    welcome_label.config(text=f"Welcome {player_name}! 🎶")
    start_game()

# ---------------- UI Layout ---------------- #
heading_label = tk.Label(window, text="Rock Your Decades", font=("Helvetica", 20, "bold"),
                         bg="#1565c0", fg="white", padx=10, pady=10)
heading_label.pack(fill="x")

welcome_label = tk.Label(window, text="Welcome to Guess the Song 🎼", font=("Arial", 14), bg="#fce4ec")
welcome_label.pack(pady=10)

name_label = tk.Label(window, text="Enter your name:", font=("Arial", 12), bg="#fce4ec")
name_label.pack()
name_entry = tk.Entry(window, font=("Arial", 12))
name_entry.pack()

start_button = tk.Button(window, text="▶ Start Game", command=get_name, bg="#4caf50", fg="white",
                         font=("Arial", 12, "bold"), width=15)
start_button.pack(pady=10)

guess_label = tk.Label(window, text="Enter your guess:", font=("Arial", 12), bg="#fce4ec")
guess_label.pack()

guess_entry = tk.Entry(window, font=("Arial", 12))
guess_entry.pack()

submit_button = tk.Button(window, text="✔ Submit", command=check_guess, bg="#6a1b9a", fg="white",
                          font=("Arial", 12, "bold"), width=15)
submit_button.pack(pady=5)

rules_button = tk.Button(window, text="📜 Rules", command=show_rules, bg="#ff9800", fg="white",
                         font=("Arial", 12, "bold"), width=15)
rules_button.pack(pady=5)

timer_label = tk.Label(window, text=f"⏳ Time remaining: {game_duration} sec", font=("Arial", 12), bg="#fce4ec")
timer_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12, "italic"), fg="red", bg="#fce4ec")
result_label.pack()

score_label = tk.Label(window, text="⭐ Score: 0", font=("Arial", 12, "bold"), bg="#fce4ec")
score_label.pack(pady=10)

leaderboard_button = tk.Button(window, text="🏆 Leaderboard", command=lambda: [save_score(), show_scores()],
                               bg="#000000", fg="white", font=("Arial", 12, "bold"), width=15)
leaderboard_button.pack(pady=15)

end_button = tk.Button(window, text="❌ End Game", command=window.destroy, bg="#e53935", fg="white",
                       font=("Arial", 12, "bold"), width=15)
end_button.pack(pady=10)

window.mainloop()
