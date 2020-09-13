import discord
import os
from dotenv import load_dotenv
load_dotenv()
from discord.ext import commands

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print(f'{bot.user} is ready')


@bot.command()
async def hello(ctx):
    await ctx.send('bye')


@bot.command()
async def potty(ctx):
    for x in range(10):
        await ctx.send(f"<@438937208582307842> ({x + 1})")


@bot.command()
async def show_me_pranav(ctx):
    await ctx.send(
        "https://media.discordapp.net/attachments/395799856322445315/754218540571164763/20200201_193408.jpg?width=193&height=496"
    )


@bot.command()
async def ajitessh_is(ctx):
    await ctx.send("mundri kotta")


@bot.command()
async def pranav(ctx):
    await ctx.send("its too sad :expressionless:")


@bot.command()
async def show_me_sujju(ctx):
    await ctx.send(
        "https://media.discordapp.net/attachments/462906549510078476/508960337765203968/suuuu.PNG?width=209&height=496"
    )


@bot.command()
async def kidnap_pranav(ctx):
    await ctx.send("omnivan incomming!")


@bot.command()
async def pottyX(ctx):
    for x in range(10):
        await ctx.send(f"<@362862038042673152>({x+1})")


@bot.command()
async def so_tell_me_about_yourself(ctx):
    await ctx.send(
        "saar iam sitting in pront of your self myshelp raakesh mahanti i work in BSNL telepone kompany but if u will ask me what is my pasiooon i billu saay haadware when ever the line goes opp i ride the corrent kommba  make the line goood saar iam happy even when iam saad :smiley:"
    )


@bot.command()
async def what_do_you_in_your_spare_time(ctx):
    await ctx.send(
        "saar during my spare time i chat on gaarls on facepook and i also collect paan masala wrapors i have a huge collection almost tuu thouusan"
    )


@bot.command()
async def navi(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/723376162658582599/754324056664309880/unknown.png"
    )


@bot.command()
async def navi2(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/395799856322445315/754325119236833300/unknown.png"
    )


@bot.command()
async def navi3(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/395799856322445315/754327403819433984/unknown.png"
    )


@bot.command()
async def hello_nitesh(ctx):
    await ctx.send("saar is currently busy")


@bot.command()
async def hello_nandha(ctx):
    await ctx.send("saar is currently stealing others food")


@bot.command()
async def hello_pranav(ctx):
    await ctx.send("saar is currently writing thesis")


@bot.command()
async def hello_nishaant(ctx):
    await ctx.send("fizz aduchitu paduthutaan")


@bot.command()
async def hello_braga(ctx):
    await ctx.send("parkour panni vizhundhutaan")


@bot.command()
async def hello_ajitessh(ctx):
    await ctx.send("saar currently is mugging up:nerd:")


bot.run(os.getenv("TOKEN"))
