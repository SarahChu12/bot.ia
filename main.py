import discord
from discord.ext import commands
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for image in ctx.message.attachments:
            file_name = image.filename
            file_url = image.url
            await ctx.send(f"Imagen guardada en {file_name}")
            await image.save(file_name)
            class_name = get_class("keras_model.h5","labels.txt", file_name)
            await ctx.send(class_name)
            try:
                
                if class_name[0] == "pikachu":
                    await ctx.send("Esto es un pikachu y algunos datos son tattatata...")
                elif class_name[1] == "eevee":
                    await ctx.send("Esto es un eeveee y algunos datos son tattatata...")
            except:
                await ctx.send("El formato de la imagen no funciona, o no se leyo bien la imagen. JPG, PNG o JPEG")
    else:
        await ctx.send("No subiste ninguna imagen :(")
bot.run("token")