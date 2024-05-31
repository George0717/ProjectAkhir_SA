import customtkinter as ctk
from tkinter import messagebox
from pivot_sort import pivot_sort
from radix_sort import radix_sort
import time

def update_progress(step_text, progress, text_widget):
    text_widget.insert(ctk.END, step_text + "\n")
    text_widget.see(ctk.END)
    progress_bar.set(progress)
    root.update_idletasks()
    time.sleep(0.5)

def process_data(data):
    result = ""
    result += "Data asli: " + str(data) + "\n\n"

    # Gabungkan semua data yang akan diurutkan
    combined_data = data.copy()

    # Proses Pivot Sort untuk semua data
    steps_pivot = []
    result += "Tahapan pengurutan semua data dengan Pivot Sort:\n"
    sorted_combined_pivot = pivot_sort(combined_data.copy(), steps_pivot, update_progress, text_result)
    for step in steps_pivot:
        result += step + "\n"
    result += "\nData terurut (Pivot Sort): " + str(sorted_combined_pivot) + "\n\n"

    # Proses Radix Sort untuk bilangan bulat saja
    steps_radix = []
    integers = [x for x in data if isinstance(x, int)]
    result += "Tahapan pengurutan bilangan bulat dengan Radix Sort:\n"
    radix_sort(integers, steps_radix, update_progress, text_result)
    for step in steps_radix:
        result += step + "\n"
    result += "\nBilangan bulat terurut (Radix Sort): " + str(integers) + "\n\n"

    return result

def on_submit():
    raw_data = entry.get()
    try:
        data = eval(raw_data)
        if not isinstance(data, list):
            raise ValueError
    except:
        messagebox.showerror("Input Error", "Masukkan daftar angka yang valid.")
        return

    text_result.delete("1.0", ctk.END)
    progress_bar.set(0)
    label_progress.configure(text="Processing...")

    result = process_data(data)
    
    text_result.insert(ctk.END, result)
    progress_bar.set(1)
    label_progress.configure(text="Completed")

# Setup GUI
ctk.set_appearance_mode("dark")  # Modes: "light" (standard), "dark", "system" (default)
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = ctk.CTk()
root.title("Perbandingan Algoritma Pivot Sort dan Radix Sort")

frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label_title = ctk.CTkLabel(frame, text="Perbandingan Algoritma Pivot Sort dan Radix Sort", font=ctk.CTkFont(size=20, weight="bold"))
label_title.pack(pady=10)

label = ctk.CTkLabel(frame, text="Masukkan daftar angka:", font=ctk.CTkFont(size=14, weight="bold"))
label.pack(pady=10)

entry = ctk.CTkEntry(frame, width=400, height=30, border_width=2, corner_radius=10)
entry.pack(pady=5)

button = ctk.CTkButton(frame, text="Urutkan Data", command=on_submit, corner_radius=10)
button.pack(pady=10)

progress_bar = ctk.CTkProgressBar(frame, width=500)
progress_bar.pack(pady=10)
progress_bar.set(0)

label_progress = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=12, weight="bold"))
label_progress.pack(pady=5)

text_result = ctk.CTkTextbox(frame, width=500, height=300, corner_radius=10)
text_result.pack(pady=10)

# Run the GUI loop
root.mainloop()
