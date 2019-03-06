import discord
import asyncio

TOKEN = 'NDc1ODAxNzY2MzgyNzk2ODAw.DkoBIQ.nLgQy1uVJzlVsV9JmPwX17N8pMc'


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!add'):
        f = open("C:\SongList\SongList.txt", "a")
        f.write(message.content[5:] + "\n")
        f.close()

    elif message.content.startswith('!play'):
        f = open("C:\SongList\SongList.txt", "r")
        voice_channel = message.author.voice.voice_channel
        voice = await client.join_voice_channel(voice_channel)
        inQueue = True
        while inQueue:
            nextSong = f.readline()
            print(nextSong)
            if nextSong == '':
                inQueue = False
                break

            player = await voice.create_ytdl_player(nextSong)
            player.start()
            tmp = open("C:\SongList\TmpFile", "w")
            await asyncio.sleep(player.duration)
            print(player.duration)


   # elif message.content.startswith('!info'):
        #title = player.title
        #await client.send_message(message.channel, member)

client.run(TOKEN)
