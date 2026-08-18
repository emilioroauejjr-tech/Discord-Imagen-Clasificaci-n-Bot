# 🤖 Bot de identificación de objetos con YOLOv8

## 📌 Descripción

Este proyecto consiste en un bot de Discord desarrollado en Python que utiliza el modelo YOLOv8 para detectar e identificar objetos dentro de imágenes enviadas por los usuarios.

El usuario envía una imagen junto con el comando `!identificar`. El bot descarga la imagen, la analiza utilizando YOLOv8 y devuelve una nueva imagen con los objetos detectados. Además, muestra los nombres de los objetos encontrados.

## 🚀 Funciones principales

* Recibir imágenes desde Discord.
* Procesar imágenes utilizando YOLOv8.
* Detectar diferentes objetos presentes en una imagen.
* Generar una imagen con las detecciones realizadas.
* Enviar el resultado nuevamente al canal de Discord.
* Mostrar los nombres de los objetos identificados.
* Responder al comando de saludo.

## 💬 Comandos

### `!identificar`

Se debe enviar una imagen adjunta junto con el comando:

`!identificar`

El bot procesa la imagen y devuelve el resultado con los objetos identificados.

### `!saludar`

Al escribir:

`!saludar`

El bot responde:

`Hola`

## 🧠 Modelo utilizado

El proyecto utiliza el modelo:

`yolov8n.pt`

YOLOv8 permite detectar y clasificar objetos presentes en imágenes.

## 🛠 Tecnologías utilizadas

* Python
* Discord.py
* Ultralytics YOLOv8
* Pillow
* NumPy
* OpenCV
* PyTorch

## ⚙️ Cómo funciona

1. El usuario envía una imagen con el comando `!identificar`.
2. El bot obtiene la imagen adjunta.
3. La imagen se guarda temporalmente.
4. YOLOv8 analiza la imagen.
5. Se genera una nueva imagen con las detecciones.
6. El bot envía la imagen procesada a Discord.
7. También muestra los nombres de los objetos detectados.

## 📷 Ejemplo

Se puede agregar una captura de pantalla del bot funcionando en Discord para mostrar cómo recibe una imagen y devuelve el resultado.

## 👨‍💻 Autor

Proyecto desarrollado como parte de una actividad de programación e inteligencia artificial.
