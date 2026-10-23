import discord
from discord.ext import commands
from discord import app_commands
import logging
from dotenv import load_dotenv
import app_command_output
import os
from aiohttp import web


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True


class MyBot(commands.Bot):
    async def setup_hook(self):
        # Start a tiny web server so Render detects an open port
        async def health(request):
            return web.Response(text="Bot is running")

        app = web.Application()
        app.router.add_get('/', health)
        app.router.add_get('/health', health)

        runner = web.AppRunner(app)
        await runner.setup()
        port = int(os.environ.get('PORT', 10000))
        site = web.TCPSite(runner, '0.0.0.0', port)
        await site.start()
        print(f"Web server listening on port {port}")


bot = MyBot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"error syncing commands : {e}")

    print(f'Logged in as {bot.user.name}')


@app_commands.command(name='generate_loadout', description='Generate a random loadout')
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.user_install()

async def generate_loadout(interaction: discord.Interaction,selected_class = None):
    desc = app_command_output.random_loadout_output(selected_class)

    embed = discord.Embed(
        title=f"**{interaction.user.display_name}'s Loadout**",
        description=desc,
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)


@generate_loadout.autocomplete('selected_class')
async def generate_loadout_autocomplete(interaction: discord.Interaction,current: str,) -> List[app_commands.Choice[str]]:
    classes = ['Light','Medium','Heavy']
    return [
        app_commands.Choice(name=generate_loadout, value=c)
        for c in classes if current.lower() in c.lower()
    ]


bot.tree.add_command(generate_loadout)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)