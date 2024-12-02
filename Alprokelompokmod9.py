import tkinter as tk
from tkinter import messagebox
import threading
import time
import random

# Global variable for timer thread
timer_running = False

# Fungsi Timer Belajar
def start_timer():
    global timer_running
    try:
        timer_running = True
        minutes = int(timer_input.get())
        seconds = minutes * 60
        while seconds > 0 and timer_running:
            mins, secs = divmod(seconds, 60)
            timer_label.config(text=f"{mins:02}:{secs:02}")
            app.update()
            time.sleep(1)
            seconds -= 1
        if timer_running:
            messagebox.showinfo("Waktu Habis", "Timer selesai!")
    except ValueError:
        messagebox.showwarning("Error", "Masukkan waktu dalam angka.")

def stop_timer():
    global timer_running
    timer_running = False

def clear_timer():
    stop_timer()
    timer_label.config(text="00:00")
    timer_input.delete(0, tk.END)

# Fungsi Catatan Harian
def save_note():
    with open("notes.txt", "w") as file:
        file.write(note_text.get("1.0", tk.END))
    messagebox.showinfo("Berhasil", "Catatan disimpan.")

def load_note():
    try:
        with open("notes.txt", "r") as file:
            note_text.delete("1.0", tk.END)
            note_text.insert(tk.END, file.read())
    except FileNotFoundError:
        messagebox.showwarning("Error", "File catatan tidak ditemukan.")

# Fungsi To-Do List
def add_task():
    task = todo_input.get()
    if task:
        todo_listbox.insert(tk.END, task)
        todo_input.delete(0, tk.END)

def mark_done():
    selected = todo_listbox.curselection()
    for i in selected:
        todo_listbox.itemconfig(i, foreground="green")

def clear_tasks():
    todo_listbox.delete(0, tk.END)

# Fungsi Kalkulator
def on_button_click(value):
    if value == "=":
        try:
            result = eval(calc_display.get())
            calc_display.delete(0, tk.END)
            calc_display.insert(0, str(result))
        except:
            calc_display.delete(0, tk.END)
            calc_display.insert(0, "Error")
    elif value == "C":
        calc_display.delete(0, tk.END)
    else:
        calc_display.insert(tk.END, value)

# Fungsi Motivational Quote
def show_quote():
    quotes = [
        "Do something today that your future self will thank you for.",
        "Believe you can and you're halfway there.",
        "Stay positive, work hard, and make it happen.",
        "Success doesn't come from what you do occasionally, it comes from what you do consistently."
    ]
    quote_label.config(text=random.choice(quotes))

# Aplikasi Utama
app = tk.Tk()
app.title("Student Productivity Toolkit")
app.geometry("900x600")
app.configure(bg="#f0f4f7")

# Frame Timer Belajar
frame_timer = tk.Frame(app, bg="#ffe0b2", relief="ridge", bd=5)
frame_timer.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Label(frame_timer, text="Timer Belajar", bg="#ffe0b2", font=("Arial", 16, "bold")).pack()
timer_input = tk.Entry(frame_timer, width=10, font=("Arial", 14))
timer_input.pack(pady=5)
tk.Button(frame_timer, text="Mulai Timer", command=lambda: threading.Thread(target=start_timer).start(), bg="#ff7043", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_timer, text="Hentikan Timer", command=stop_timer, bg="#ff7043", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_timer, text="Bersihkan Timer", command=clear_timer, bg="#ff7043", fg="white", font=("Arial", 12)).pack(pady=5)
timer_label = tk.Label(frame_timer, text="00:00", bg="#ffe0b2", font=("Arial", 24, "bold"))
timer_label.pack()

# Frame Catatan Harian
frame_notes = tk.Frame(app, bg="#bbdefb", relief="ridge", bd=5)
frame_notes.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
tk.Label(frame_notes, text="Catatan Harian", bg="#bbdefb", font=("Arial", 16, "bold")).pack()
note_text = tk.Text(frame_notes, height=8, width=30, font=("Arial", 12))
note_text.pack(pady=5)
tk.Button(frame_notes, text="Simpan Catatan", command=save_note, bg="#1e88e5", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_notes, text="Buka Catatan", command=load_note, bg="#1e88e5", fg="white", font=("Arial", 12)).pack(pady=5)

# Frame To-Do List
frame_todo = tk.Frame(app, bg="#c8e6c9", relief="ridge", bd=5)
frame_todo.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
tk.Label(frame_todo, text="To-Do List", bg="#c8e6c9", font=("Arial", 16, "bold")).pack()
todo_input = tk.Entry(frame_todo, width=20, font=("Arial", 12))
todo_input.pack(pady=5)
tk.Button(frame_todo, text="Tambah Tugas", command=add_task, bg="#43a047", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_todo, text="Tandai Selesai", command=mark_done, bg="#43a047", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_todo, text="Hapus Semua", command=clear_tasks, bg="#43a047", fg="white", font=("Arial", 12)).pack(pady=5)
todo_listbox = tk.Listbox(frame_todo, height=10, width=30, font=("Arial", 12))
todo_listbox.pack(pady=5)

# Frame Kalkulator
frame_calc = tk.Frame(app, bg="#ffcdd2", relief="ridge", bd=5)
frame_calc.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
tk.Label(frame_calc, text="Kalkulator Sederhana", bg="#ffcdd2", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=4, pady=5)
calc_display = tk.Entry(frame_calc, width=25, font=("Arial", 14))
calc_display.grid(row=1, column=0, columnspan=4, pady=5)

# Tombol Kalkulator
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row_idx, row in enumerate(buttons):
    for col_idx, button in enumerate(row):
        tk.Button(frame_calc, text=button, width=5, font=("Arial", 14),
                  command=lambda b=button: on_button_click(b),
                  bg="#f06292", fg="white").grid(row=row_idx+2, column=col_idx, padx=5, pady=5)

# Frame Motivational Quote
frame_quote = tk.Frame(app, bg="#d7ccc8", relief="ridge", bd=5)
frame_quote.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=10, pady=10)
tk.Label(frame_quote, text="Motivational Quote", bg="#d7ccc8", font=("Arial", 16, "bold")).pack()
quote_label = tk.Label(frame_quote, text="", bg="#d7ccc8", font=("Arial", 12), wraplength=200, justify="center")
quote_label.pack(pady=10)
tk.Button(frame_quote, text="Tampilkan Kutipan", command=show_quote, bg="#6d4c41", fg="white", font=("Arial", 12)).pack(pady=10)

# Membuat layout grid responsif
app.grid_columnconfigure((0, 1, 2), weight=1)
app.grid_rowconfigure((0, 1), weight=1)

# Menjalankan aplikasi
app.mainloop()