import discord

token = "OTQyMTIwNDcwNTE2NDc3OTcz.Ygf4Dw.5KD6tfa3gC0OjCEQ259U4nePKMc"
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
