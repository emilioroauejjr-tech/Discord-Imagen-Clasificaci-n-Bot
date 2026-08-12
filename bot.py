import discord, random
from discord.ext import commands
from ultralytics import YOLO
from PIL import Image


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

modelo = YOLO("yolov8n.pt")



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name = "identificar")
async def identificar(ctx):

    # Verificar si se adjunto una imagen
    if ctx.message.attachments:

        # Obtener la imagen
        imagen = ctx.message.attachments[0]

        # Crear un nombre para guardar la imagen.abs
        nombre = f"imagen{random.randint(1,1000)}.png"

        # Guardar la imagen
        await imagen.save(nombre)

        resultados = modelo(nombre)

        imagen_resultado = resultados[0].plot()


        imagen_convertida = Image.fromarray(imagen_resultado)

        imagen_convertida.save("imagen_resultado.jpg")

        await ctx.send(file = discord.File("imagen_resultado.jpg"))

        objetos = []

        for resultado in resultados:
            for caja in resultado.boxes:
                
                clase  =  int(caja.cls[0])
                nombre =  modelo.names[clase]
                objetos.append(nombre) 


        if objetos:
            await ctx.send(objetos)
        else:                
            await ctx.send("No se detecto nada")


@bot.command(name = "saludar")
async def saludar(ctx):              
    await ctx.send("Hola")



bot.run("TOKEN")
