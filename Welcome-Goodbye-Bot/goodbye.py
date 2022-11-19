import discord
import model

from model import commands, bot, member, idGoodbye
from discord.utils import get
from discord import File
from easy_pil import Font, Editor, load_image_async


@bot.event
async def on_ready():
    print("Ready")

@bot.event
async def on_member_remove(member:model.member):
    channel = bot.get_channel(model.idGoodbye)

    background = Editor("background.jpg")
    profil_img = await load_image_async(str(member.avatar.url))
    profil = Editor(profil_img).resize((150,150)).circle_image()
    
    poppins = Font.poppins(size=50, variant="bold")
    poppinsSmall = Font.poppins(size=30, variant="light")

    background.paste(profil,(325, 90))
    background.ellipse((325, 90), 150, 150, outline="white", stroke_width=4)
    background.text((400,260),f"Goodbye {member.guild.name}", color="white", font=poppins, align="center")
    background.text((400,340), f" ---- {member.name} ---- ", color="white", font=poppinsSmall, align="center")

    file = File(fp=background.image_bytes, filename="background.jpg")
    await channel.send(f"See you {member.mention}")
    await channel.send(file=file)

botGoodbye = bot





