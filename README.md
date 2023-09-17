# Demonstration Interface for NMT using CTranslate2 + GRADIO

[![Estado del Proyecto](https://img.shields.io/badge/Estado-Activo-brightgreen.svg)](https://github.com/tuusuario/tuproyecto)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-blue.svg)](LICENSE)


## Tabla de Contenidos

- [Instalación](#instalación)
- [Demo](#demo)
- [Visualization](#capturas-de-pantalla)

## Installation
```bash
!pip install -r requirements.txt
```
```bash
!ct2-transformers-converter --model facebook/nllb-200-distilled-600M --output_dir nllb-200-distilled-600M-ct2
```

## Demo
All of demos for NMT  are based in HuggingFace Model's for NMT with CTranslate2 Transformation. You could see all of the models supported [[here](https://opennmt.net/CTranslate2/guides/transformers.html)]

To use this project you should put in bash terminal the following command:

```bash
python3 gradio_nllb.py demo --model_ct2 nllb-200-distilled-600M-ct2 --model_base facebook/nllb-200-distilled-600M  -lang "Spanish-French"
```

## Visualization
![alt text](https://github.com/MarkoAVILA/CTranslate_Gradio_Demo/blob/main/images/translator.png?raw=true)




