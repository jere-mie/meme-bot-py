import discord
from discord.ext import commands
from random import randint
from memeMaker import makeMeme
from pyjokes import get_joke
import json

with open('secrets.json') as f:
  data = json.load(f)

client = commands.Bot(command_prefix='!')
client.remove_command("help")

commands_list={
    "help": "`!help <command>`\nDisplays details about a specific command, or all commands if <command> field is empty",
    "meme": "`!meme <name of meme> <text>`\nCreates a meme based on the name of the meme you provided, and the text you input.\nAcceptable meme names can be found by typing `!memes`\nNote: If you just want the template, put 'template' as your text.",
    "memes": "`!memes`\nDisplays the list of acceptable meme names",
    "anon": "`!anon <text>`\nSends a message anonymously (deletes the command)",
    "joke": "`!joke`\nDisplays a random programming joke",
    "ask": "`!ask <text>`\nAsk advice or a yes/no question to the all-knowing meme bot and see its response",
    "flip": "`!flip`\nFlips a coin (heads or tails)",
    "roll": "`!roll <num>`\nRolls a die with <num> sides",
    "purge": "`!purge <limit>`\n**ADMIN ONLY!**\nDeletes a certain number of messages",
    "hidify": "`!hidify <phrase>`\nMarks each character of your message in spoilers",
    "bigify": "`!bigify <letters>`\nMakes each letter in your phrase bigger",
    "ping":"`!ping`\nDisplays latency in ms"
}

memesList="""
~arthur
~chungus
~coffee
~comingtogether
~crazysponge
~disgust
~drake
~everyoneisstupid
~funnysponge
~futurama
~imin
~meandtheboys
~nice
~noyouaint
~ohyea
~okconnor
~patrick
~pikachu
~poorsquid
~professional
~sadcat
~sadgry
~sadsponge
~smugsponge
~spiderman
~spongemock
~stark
~stonks
~thisisfine
~tom
~uh
"""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

# Commands

@client.command()
async def ask(ctx, *, arg):
    x = randint(0,6)
    messages = ["Im gonna go with yes.", 
                "I mean, I could go either way, but yea I guess.", 
                "TBH idk mate.", 
                "Please stop asking me questions. Geez.", 
                "Nah, I'm feeling no on this one.", 
                "Yea whatever. If I say yes will you be happy?", 
                "Are you serious? Of course not."]
    await ctx.send(messages[x])

@client.command()
async def ping(ctx):
    await ctx.send(f"Latency: {round(client.latency * 1000)}ms")

@client.command()
async def pong(ctx):
    await ctx.send(f"Lootency: {round(client.latency * 1000000)}months")


@client.command()
async def ziad(ctx):
    await ctx.send("```kobti```")

@client.command()
async def flip(ctx):
    x=randint(0,1)
    messages=["HEADS\nhttps://tenor.com/view/champagne-heads-tails-heads-or-tails-coin-gif-13943298", "TAILS\nhttps://tenor.com/view/champagne-heads-tails-heads-or-tails-coin-gif-13943297"]
    await ctx.send(messages[x])

@client.command()
async def roll(ctx, arg):
    x=randint(1,int(arg))
    await ctx.send(f"You rolled a {x}")

@client.command()
async def anon(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)

@client.command()
async def bigify(ctx, *, arg):
    await ctx.message.delete()
    output=""
    for i in arg:
        if i==' ':
            output+='   '
        else:
            output+=':regional_indicator_'+i.lower()+': '
    await ctx.send(output)


@client.command()
async def hidify(ctx, *, arg):
    await ctx.message.delete()
    output = "`"
    for i in arg:
        output+="||"+i+"||"
    await ctx.send(output+'`')

# thank you to Wahid Bawa for the following command 
# from https://github.com/UWindsor-Robotics-Tech/UWin-Robotics-Robot/blob/master/robot/main.py
@client.command()
async def searchify(ctx, *, searchTerm):
    link = "https://lmgtfy.com/?q="
    link += searchTerm.replace(" ", "+")
    await ctx.send(link)

@client.command()
async def meme(ctx, fname, *, text):
    if text=='template':
        text=''
    makeMeme(fname, text)
    await ctx.send(file=discord.File('out.png'))

# Thank you to Wahid Bawa for allowing me to use his code for this help menu
# View his code here: https://github.com/UWindsor-Robotics-Tech/UWin-Robotics-Robot/blob/master/robot/main.py
@client.command()
async def help(ctx, *, command=None):
    embed = discord.Embed(title="HELP", colour=0xcccc00)
    if command is None:
        for i in commands_list:
            embed.add_field(name=i, value=commands_list[i], inline=False)
    elif command in commands_list:
        embed.add_field(name=command, value=commands_list[command], inline=False)
    else:
        await ctx.send("This is not an existing command")
        return
    await ctx.send(embed=embed)


@client.command()
async def memes(ctx):
    embed = discord.Embed(title="LIST OF MEMES", colour=0xcccc00)
    embed.add_field(name="Memes List", value=memesList, inline=False)
    await ctx.send(embed=embed)


@client.command()
@commands.has_role("Admin")
async def purge(ctx, arg):
    await ctx.message.channel.purge(limit=int(arg))

@client.command()
async def joke(ctx):
    await ctx.send(get_joke())
    
client.run(data['token'])
