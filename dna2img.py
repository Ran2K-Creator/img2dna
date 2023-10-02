import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
import numpy as np

def open_dna_sequence():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return

    with open(filepath, 'r') as f:
        dna_sequence = f.read().strip()

    image = process_dna_sequence(dna_sequence)
    image.save("output.png")  # Saving the image as "output.png"
    dna_text.delete(1.0, tk.END)
    dna_text.insert(tk.END, dna_sequence)

    # Reset progress bar after processing
    progress_bar['value'] = 0

def save_image():
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Images", "*.png")])
    if filepath:
        image = Image.open("output.png")
        image.save(filepath)

def process_dna_sequence(dna_sequence):
    codon_to_pixel = {
        'ATA': 32,  # Midpoint of 0-63
        'CGC': 96,  # Midpoint of 64-127
        'GCG': 160,  # Midpoint of 128-191
        'TAT': 224   # Midpoint of 192-255
    }

    num_pixels = len(dna_sequence) // 3
    side_length = int(np.sqrt(num_pixels))  # Assuming a square image for simplicity
    arr = np.zeros((side_length, side_length), dtype=np.uint8)

    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        x = (i // 3) // side_length
        y = (i // 3) % side_length
        arr[x, y] = codon_to_pixel.get(codon, 32)

        # For the progress bar
        progress = (i + 3) / len(dna_sequence) * 100
        progress_bar['value'] = progress
        app.update_idletasks()

    return Image.fromarray(arr)

app = tk.Tk()
app.title("DNA to Image Converter")

# Main frame
frame = tk.Frame(app, padx=20, pady=20)
frame.pack(pady=20)

# Title
title_label = tk.Label(frame, text="DNA2IMG", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Subtitle
subtitle_label = tk.Label(frame, text='By Ran Malamud', font=("Arial", 12))
subtitle_label.pack(pady=10)

# Button to open the DNA sequence
open_btn = tk.Button(frame, text="Open DNA Sequence", command=open_dna_sequence)
open_btn.pack(pady=10)

# Button to save the image
save_btn = tk.Button(frame, text="Save Image", command=save_image)
save_btn.pack(pady=10)

# Text box to display the DNA sequence
dna_text = tk.Text(frame, height=10, width=50)
dna_text.pack(pady=20)

# Progress bar
progress_bar = ttk.Progressbar(frame, orient='horizontal', length=400, mode='determinate')
progress_bar.pack(pady=20)

app.mainloop()
