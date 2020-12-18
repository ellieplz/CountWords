import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        

        client.run('Nzg4Nzk1MzA0MTk0OTk4MzY0.X9os3w.Gc_Aru6xWuQnJmPo8dil2LsR3-8')
        
        
        #        discord.Permissions ('read_message_history' == 0)
#
# async def on_message(message):
#    if message.author == client.user:
#        return
#
#    if message.content.startswith('count'):
#        await message.channel.send('Hello!')
#
#        async for hello in history(*, limit=100, before=None, after=None, around=None, oldest_first=None)¶
#
#
#        counter = 0
#        async for message in channel.history(limit=200):
#        if message.author == client.user:
#        counter += 1
#
#        messages = await channel.history(limit=123).flatten()
