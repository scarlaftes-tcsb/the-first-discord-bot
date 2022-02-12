import os
import discord

token = os.environ['token']
client = discord.Client()

@client.event
async def on_ready():
  print('{0.user} has connected to Discord!'.format(client))
@client.event
async def on_message(message):
  author = str(message.author)
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  if message.author == client.user:
    return
  await message.channel.send(f'hello {username} {author} {user_message} {channel}')

client.run(token)

