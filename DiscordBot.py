from UpdateCheck import hhLogin_update
import discord
import os
from SelenuimLogin import hhLogin
from ClusterStatus import hhLogin_cluster
from UpdateCheck import hhLogin_update
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

    if message.content.startswith('$update') or message.content.startswith("$Update"):
        updateStatus = hhLogin_update('update')
        await message.channel.send(updateStatus) 

    if message.content.startswith('$help') or message.content.startswith('$Help'):
        message1 = "Hello I am ArkBot.\nFor the status of all servers enter: '$cluster'.\n"
        message2 = "For individual server status enter: '$valguero', $olympus', or '$fear'.\n"
        message3 = "To see if I am running, please enter: '$status'.\n"
        message4 = "Please note it may take me up to 30 seconds for server information to be retrieved.\n"
        message5 = "Input of excessive commands will slow down my search.\n"
        message6 = "My future updates include identifying pending updates and auto-updating.\n"
        message7 = "If you have any questions or obnoxious feedback, message McDoodle."
        await message.channel.send(message1+message2+message3+message4+message5+message6+message7)

# Define token & U
ArkBot_Token = os.environ.get('ARKBOT_TOKEN')
client.run(ArkBot_Token)