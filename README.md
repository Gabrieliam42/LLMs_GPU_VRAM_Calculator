## LLMs GPU VRAM Requirements Calculator

##### The script calculates the GPU VRAM Requirements for Large Language Models of different parameters sizes



##### This script has been tested on the Windows environment.



##### Requirements:

- `pandas`



<br><br>



<br><br>

![MasterHead](https://i.imgur.com/mEoyckM.png)

- In the image above you can see that for example for a 13B (13 Billion parameters) LLM you would need a GPU that has: at least 6.96GB free VRAM for a 4-bit version of the model, OR at least 13.93GB VRAM for a 8-bit version of the model, OR at least 27.84GB free VRAM for a 16-bit version of the model(FP16), and so on.
- For a 4B (4 Billion parameters) LLM you would need a GPU that has: at least 2.14GB VRAM for running the 4-bit version of the model, OR at least 4.29GB VRAM for a 8-bit version of the model, OR at least 8.57GB VRAM for a 16-bit version of the model(FP16), OR at least 17.13GB VRAM for a full 32-bit version of the model(FP32).



VRAM Requirements for Different Precisions

When using different precision levels, the memory required per parameter varies:

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
