## LLMs GPU VRAM Requirements Calculator

##### The algorithm calculates which LLMs (Large Language Models) parameters sizes and quantized versions that fit the user's specified GPU VRAM amount.
##### You can use the compiled version on Windows: `LLMs_GPU_VRAM_Calculator.exe`


##### This script has been tested on the Windows environment.


##### Requirements:

- `pandas`
- `tk` (tkinter)



![MasterHead](https://i.imgur.com/GyT2EXf.png)

- In the image above you can see that the user has inserted 24 in the input (for 24 GPU VRAM) and the script calculated the LLMs versions that are Ok for it for each parameter size LLM.
- For example for a 13B (13 Billion parameters) LLM only the 4-bit (q4) and 8-bit(q8) fit that VRAM amount, the 16-bit and the 32-bit are too large. for the 13B LLM you would need a GPU that has: at least 6.96GB free VRAM for a 4-bit version of the model, OR at least 13.93GB VRAM for a 8-bit version of the model. (It would need 27.84GB free VRAM for a 16-bit version of the LLM model(FP16), so 24GB is clearly not enough.)
- For a 4B (4 Billion parameters) LLM you would need a GPU that has: at least 2.14GB VRAM for running the 4-bit version of the model, OR at least 4.29GB VRAM for a 8-bit version of the model, OR at least 8.57GB VRAM for a 16-bit version of the model(FP16), OR at least 17.13GB VRAM for a full 32-bit version of the model(FP32).



VRAM Requirements for Different Precisions

When using different precision levels, the memory required per parameter varies as follows:

* FP32 (32-bit floating point): 4 bytes per parameter
* FP16 (16-bit floating point): 2 bytes per parameter
* 8-bit precision: 1 byte per parameter
* 4-bit precision: 0.5 bytes per parameter


Overhead Factor:
Additionally, a 1.15x overhead factor is applied to account for extra memory usage, meaning the final memory requirement is calculated by multiplying by 1.15.








<br><br>





<br><br>








**Script Developer:** Gabriel Mihai Sandu  
**GitHub Profile:** [https://github.com/Gabrieliam42](https://github.com/Gabrieliam42)
