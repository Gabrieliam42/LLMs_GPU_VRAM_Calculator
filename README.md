## LLMs GPU VRAM Requirements Calculator

##### The script calculates the GPU VRAM Requirements for Large Language Models of different parameters sizes



##### This script has been tested on the Windows environment.



##### Requirements:

- `pandas`

<br><br>



<br><br>



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
