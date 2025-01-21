import discord
import re
import os
from keep_alive import keep_alive

# Bot Token from Replit Secrets
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents for the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

# Regular expression to detect Bengali characters
bengali_regex = re.compile(r'[\u0980-\u09FF]')

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if the message contains Bengali characters
    if bengali_regex.search(message.content):
        try:
            # Delete the message
            await message.delete()

            # Notify the user
            warning_message = f"{message.author.mention}, chup nengta kuttar baccha"
            await message.channel.send(warning_message)
        except discord.Forbidden:
            print("Bot doesn't have permission to delete messages.")
        except discord.HTTPException as e:
            print(f"Failed to delete message or send warning: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Start the web server
keep_alive()

client.run(TOKEN)
