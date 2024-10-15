import flet as ft
import random

#Funcion para adivinar el numero 
def verificar_adivinanza(e,page):
    adivinanza_usuario=int(entrada.numero.value)
    
    if adivinanza_usuario==numero_secreto:
        texto_resultado.value="¡Felicidades! Adivinaste el numero secreto"
        boton_adivinar.disabled=True
        page.add(ft.Audio(src="Victoria.mp3",autoplay=True))
    elif adivinanza_usuario < numero_secreto:
        texto_resultado.value="¡Fallaste! El numero es mayor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))
    else:
        texto_resulado.value="¡Fallaste! El numero es menor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))
        
    entrada_numero.value=""
    page.update()
    
    

# Función principal
def main(page: ft.Page):
    # Variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar
    
    page.title = "Adivina el número"
    
    # Generar un número aleatorio
    numero_secreto = random.randint(1, 100)
    
    # Crear los elementos de la interfaz
    titulo = ft.Text("Adivina el número secreto entre el 1 y 100", size=20, color="white")
    entrada_numero = ft.TextField(label="Tu Adivinanza", width=150)
    adivinar = ft.ElevatedButton("Adivinar",on_click=lambada e: verificar_adivinanza(e,page))
    resultado = ft.Text("",color="white")
    
    def adivinar(e):
        try:
            adivinanza = int(entrada_numero.value)
            if adivinanza < numero_secreto:
                texto_resultado.value = "Demasiado bajo! Intenta de nuevo."
            elif adivinanza > numero_secreto:
                texto_resultado.value = "Demasiado alto! Intenta de nuevo."
            else:
                texto_resultado.value = "¡Correcto! Has adivinado el número."
        except ValueError:
            texto_resultado.value = "Por favor, ingresa un número válido."
        
        # Limpiar el campo de entrada después de intentar adivinar
        entrada_numero.value = ""
        page.update()  # Actualizar la página para mostrar el nuevo resultado

    boton_adivinar = ft.ElevatedButton("Adivinar", on_click=adivinar)
    texto_resultado = ft.Text("", color="white")
    
    contenedor_principal = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200
                )
            ],
            alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="red",
        width=page.window.width,
        height=page.window.height,
        padding=20
    )
    
    page.add(contenedor_principal)

ft.app(main)