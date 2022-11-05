import discord
from decouple import config
from keep_alive import keep_alive
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        await message.channel.send('Hello There')

keep_alive()
client.run(config('TOKEN'))