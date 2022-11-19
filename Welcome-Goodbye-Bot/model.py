import discord

from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)
member = discord.Member
# =================
token = (TOKEN)
idWekcome = (ID_CHANNEL_DISCORD)
idGoodbye = (ID_CHANNEL_DISCORD)