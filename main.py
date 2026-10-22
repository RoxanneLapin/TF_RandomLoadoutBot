import discord
from discord.ext import commands
from discord import app_commands
import logging
from dotenv import load_dotenv
import app_command_output
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log',encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True



bot: commands.Bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"error syncing commands : {e}")

    print(f'Logged in as {bot.user.name}')
    


@app_commands.command(name='generate_loadout',description='Generate a random loadout')
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) 
@app_commands.user_install()
async def generate_loadout(interaction):
    desc = app_command_output.random_loadout_output()
    
    embed = discord.Embed(
    title=f"**{interaction.user.display_name}'s Loadout**",
    description=desc,
    color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)

bot.tree.add_command(generate_loadout)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)

