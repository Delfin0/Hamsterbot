import discord




intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('!help'):
        embed=discord.Embed(title="🛟 Segítség 🛟", description="**Parancsok és információk** \n Hamsterbot egy ideje nem üzemelt. Mostanában megjött a kedvem hozzá hogy csináljam szóval most újra lesz. \n **Parancsok:** \n **!help** Parancsok és információk  ", color=0xFF5733)
        await message.channel.send(embed=embed)
    if message.content.startswith('!hamstercraft'):
        embed=discord.Embed(title="🕹️ Hamstercraft 🕹️", description="**Információk a Hamstercraft minecraft szerverről.** \n A Hamstercraft egy túléló minecraft szerver. \n **IP cím:** hamstercraft.craft.run \n **Verzió:** 1.19(Java) \n **Admin:** Pergerot", color=0x00ff62)
        await message.channel.send(embed=embed)

client.run('ODU0MzEyMTUzMDc4NTYyODM3.GHhsuN.Anp10g6maHef4DPESI_x8rY9TSADnOARZKRPxM')
