import flet as ft
import random

#Función para adivinar el número
def verificar_adivinanza(e,page):
    adivinanza_usuario=int(entrada_numero.value)
    
    if adivinanza_usuario==numero_Secreto:
        texto_resultado.value="¡Felicidades! Adivinaste el número secreto"
        boton_adivinar.disabled=True
        page.add(ft.Audio(src="Victoria.mp3",autoplay=True))
    elif adivinanza_usuario < numero_Secreto:
        texto_resultado.value="¡Fallaste! El número secreto es mayor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))
    else:
        texto_resultado.value="¡Fallaste! El número secreto es menor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))
        
        entrada_numero.value=""
        page.update()


#Función principal
def main(page: ft.Page):
    #Variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar
    
    page.title = "Adivina el número"
    
    #Generar un número aleatorio
    numero_Secreto = random.randint(1,100)
    
    #Crear los elementos interfaz
    titulo=ft.Text("Adivina el número secreto entre el 1 y 100",size= 20,color="white")
    entrada_numero=ft.TextField(label="Tu Adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    texto_resultado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.giff",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="black",
        width=page.window.width,
        height=page.window.height,
        padding=20
    
    
    )
    
    page.add(contenedor_princpal)


ft.app(main)
