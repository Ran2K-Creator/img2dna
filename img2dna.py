import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
import numpy as np

def open_image():
    filepath = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    if not filepath:
        return

    image = Image.open(filepath)
    _, dna_sequence = process_image(image)
    dna_text.delete(1.0, tk.END)
    dna_text.insert(tk.END, dna_sequence)

    # Reset progress bar after processing
    progress_bar['value'] = 0

def save_dna_sequence():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, 'w') as f:
            f.write(dna_text.get(1.0, tk.END))

def process_image(image):
    image = image.convert("L")  # Convert to grayscale
    arr = np.array(image)

    conditions = [
        (arr < 64),
        (64 <= arr) & (arr < 128),
        (128 <= arr) & (arr < 192),
        (arr >= 192)
    ]
    codons = ['ATA', 'CGC', 'GCG', 'TAT']

    dna_array = np.select(conditions, codons, default='ATA')
    dna_sequence = ''.join(codon for slice_2d in dna_array for codon in slice_2d)

    # For the progress bar
    total_pixels = dna_array.size
    for index in range(total_pixels):
        progress = (index + 1) / total_pixels * 100
        progress_bar['value'] = progress
        app.update_idletasks()

    return image, dna_sequence


app = tk.Tk()
app.title("Image to DNA Converter")

# Main frame
frame = tk.Frame(app, padx=20, pady=20)
frame.pack(pady=20)

# Title
title_label = tk.Label(frame, text="IMG2DNA", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Subtitle
subtitle_label = tk.Label(frame, text='By Ran Malamud', font=("Arial", 12))
subtitle_label.pack(pady=10)

# Button to open the image
open_btn = tk.Button(frame, text="Open PNG Image", command=open_image)
open_btn.pack(pady=10)

# Button to save the DNA sequence
save_btn = tk.Button(frame, text="Save DNA Sequence", command=save_dna_sequence)
save_btn.pack(pady=10)

# Text box to display the DNA sequence
dna_text = tk.Text(frame, height=10, width=50)
dna_text.pack(pady=20)

# Progress bar
progress_bar = ttk.Progressbar(frame, orient='horizontal', length=400, mode='determinate')
progress_bar.pack(pady=20)

app.mainloop()