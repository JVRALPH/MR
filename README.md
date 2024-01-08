# MR
Recomendador de musica 

Flet - Guía de Instalación
Flet es una biblioteca para crear interfaces de usuario (UI) web interactivas y modernas utilizando Python. Esta guía proporciona instrucciones paso a paso para instalar y configurar Flet en tu entorno.

Requisitos previos
Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde python.org.

Instalación
Paso 1: Instalación de Flet
Puedes instalar Flet utilizando pip, el administrador de paquetes de Python. Abre una terminal o línea de comandos y ejecuta el siguiente comando:
pip install flet

Uso básico
Ahora que has instalado Flet, puedes comenzar a crear aplicaciones web utilizando esta biblioteca. Aquí hay un ejemplo simple:

import flet as ft

def main(page: ft.Page):
    page.title = "Mi primera aplicación web con Flet"
    page.add(ft.Text("¡Hola, mundo!"))

ft.app(target=main)

Documentación adicional
Para obtener más información sobre cómo utilizar Flet y sus características avanzadas, puedes consultar la documentación oficial de Flet en https://flet.dev/docs/

Ejecutar la aplicación
Abre una terminal o línea de comandos, navega hasta la ubicación donde guardaste tu archivo Python y ejecuta el siguiente comando:
python mi_aplicacion.py

Esto iniciará tu aplicación web utilizando Flet. Abre un navegador web y ve a la dirección http://localhost:8550 para ver tu aplicación en acción.
