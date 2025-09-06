# Script Developer: Gabriel Mihai Sandu
# GitHub Profile: https://github.com/Gabrieliam42

import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

def calculate_vram(params_in_billion, bits):
    params = params_in_billion * 1e9
    vram_gb = (params * bits) / (8 * 1024**3)
    return round(vram_gb, 2)

# overhead factor
overhead_factor = 1.15

# model sizes
model_sizes = [f"{i}B" for i in range(1, 36)]  # 1B–35B

# quantization configs
bit_configs = [4, 8, 16, 32]

# calculate VRAM requirements
vram_requirements_overhead = {"Model Size": model_sizes}
for bits in bit_configs:
    vram_requirements_overhead[f"{bits}-bit VRAM (GB)"] = [
        round(calculate_vram(int(size[:-1]), bits) * overhead_factor, 2) for size in model_sizes
    ]

df_vram_overhead = pd.DataFrame(vram_requirements_overhead)

# GUI
root = tk.Tk()
root.title("LLM GPU VRAM Calculator")

def check_models():
    try:
        available_vram = float(vram_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for VRAM.")
        return
    
    results = []
    for _, row in df_vram_overhead.iterrows():
        fits = []
        for bits in bit_configs:
            required_vram = row[f"{bits}-bit VRAM (GB)"]
            if required_vram <= available_vram:
                fits.append(f"{bits}-bit ({required_vram} GB)")
        if fits:
            results.append(f"{row['Model Size']}: " + ", ".join(fits))
    
    if not results:
        result_text.set("No models fit into the specified VRAM.")
    else:
        result_text.set("\n".join(results))

# input frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="ew")

ttk.Label(frame, text="Enter Available GPU VRAM (GB):").grid(row=0, column=0, sticky="w")
vram_entry = ttk.Entry(frame, width=10)
vram_entry.grid(row=0, column=1, padx=5)

check_button = ttk.Button(frame, text="Check Models", command=check_models)
check_button.grid(row=0, column=2, padx=5)

# results
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, justify="left", padding="10")
result_label.grid(row=1, column=0, sticky="w")

root.mainloop()
