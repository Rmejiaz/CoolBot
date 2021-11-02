# CoolBot

ChatBot implementado en python con `flask`, `nltk` y `tensorflow` 

Hecho por [_rmejiaz_](https://github.com/Rmejiaz) y [_sbuitragoo_](https://github.com/sbuitragoo), estudiantes de Ingeniería Electrónica de la Universidad Nacional de Colombia, sede Manizales.


CoolBot es un chatbot que pretende funcionar como apoyo en los temas de lógica de predicados y marcos en el contexto de la asignatura de Sistemas Inteligentes Computacionales.


## Probar en Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12AIbnnf80CH1Z7h4zQ4ir3JE00KiRfj5?usp=sharing)

## Uso

### 1. Clonar el repositorio:

```bash
$ git clone https://github.com/Rmejiaz/CoolBot
$ cd CoolBot
```

### 2. Instalar dependencias:

```bash
$ pip install -r requirements.txt
```
### 3. Descargar archivos necesarios para el funcionamiento de `nltk`:

```bash
$ python nltk_setup.py
```

### 4. Usar aplicación

#### 4.1 (GUI):

```bash
$ python main.py
```

Luego, acceder en un navegador a: http://127.0.0.1:5000/

#### 4.2 (CLI) (apto para correr en entornos como google colaboratory):

```bash
$ python cli_main.py
```
