import discord
import os
from SelenuimLogin import hhLogin
from ClusterStatus import hhLogin_cluster
from dotenv import load_dotenv
# Load .env variables
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$olympus'):
        ServerStatus = hhLogin('olympus')
        await message.channel.send('Olympus Server: ' + str(ServerStatus) + ".")

    if message.content.startswith('$valguero'):
        ServerStatus = hhLogin('valguero')
        await message.channel.send("Valguero Server: " + str(ServerStatus) + ".")

    if message.content.startswith('$fear'):
        ServerStatus = hhLogin('fear')
        await message.channel.send("Primal Fear Server: " + str(ServerStatus) + ".")

    if message.content.startswith('$status') or message.content.startswith("$Status"):
        await message.channel.send('ArkBot is running.')
    
    if message.content.startswith('$cluster') or message.content.startswith("$Cluster"):
        clusterStatus = hhLogin_cluster('cluster')
        await message.channel.send(clusterStatus)

# Define token & U
ArkBot_Token = os.environ.get('ARKBOT_TOKEN')
client.run(ArkBot_Token)