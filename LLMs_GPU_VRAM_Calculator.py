# Script Developer: Gabriel Mihai Sandu
# GitHub Profile: https://github.com/Gabrieliam42

import pandas as pd

def calculate_vram(params_in_billion, bits):
    params = params_in_billion * 1e9
    vram_gb = (params * bits) / (8 * 1024**3)
    return round(vram_gb, 2)

overhead_factor = 1.15

model_sizes = ["3B", "4B", "5B", "6B", "7B", "8B", "10B", "11B", "12B", "13B", "14B", "15B", "16B", "17B", "18B", "20B", "22B", "23B", "24B", "27B", "30B", "32B", "33B", "34B", "35B"]

bit_configs = [4, 8, 16, 32]

vram_requirements_overhead = {
    "Model Size": model_sizes
}

for bits in bit_configs:
    vram_requirements_overhead[f"{bits}-bit VRAM (GB)"] = [
        round(calculate_vram(int(size[:-1]), bits) * overhead_factor, 2) for size in model_sizes
    ]

df_vram_overhead = pd.DataFrame(vram_requirements_overhead)

print(df_vram_overhead.to_string(index=False))
