import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('online')



client.run('hEXP7JCGsuOqPleGE71g9CanS0p4CG44')