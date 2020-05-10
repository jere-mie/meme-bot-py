import discord
from discord.ext import commands
from random import randint
from imageStuff import makeMeme
from pyjokes import get_joke
import json

with open('secrets.json') as f:
  data = json.load(f)

client = commands.Bot(command_prefix='!')
client.remove_command("help")
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Unverified")
    await member.add_roles(role)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)


@client.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@client.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

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
async def meme(ctx, fname, *, text):
    if text=='template':
        text=''
    makeMeme(fname, text)
    await ctx.send(file=discord.File('out.png'))

@client.command()
async def help(ctx):
    text="""
***MEME BOT HELP MENU***
List of Commands:

**!help**
Displays the help menu
**!joke**
Displays a random programming joke
**!anon <text>**
Sends a message anonymously (deletes the command)
**!ask <text>**
Ask advice or a yes/no question to the all-knowing meme bot and see it's response
**!flip**
Flips a coin (heads or tails)
**!roll <num>**
Rolls a die with <num> sides
**!verify <Full Name>**
Verifies you into the server if you are registered via the Google Form
**!purge <limit>**
ADMIN ONLY!
Deletes a certain number of messages
**!meme <name of meme> <text>**
Creates a meme based on the name of the meme you provided, and the text you input.
Acceptable meme names are: chungus, coffee, comingtogether, crazysponge, drake, imin, nice, sadcat, sadgry, sadsponge, tom, uh
*Note: If you just want the template, put 'template' as your text.* 
"""
    await ctx.send(text)


@client.command()
@commands.has_role("Admin")
async def purge(ctx, arg):
    await ctx.message.channel.purge(limit=int(arg))

@client.command()
async def joke(ctx):
    await ctx.send(get_joke())


@client.command()
@commands.has_role("Unverified")
async def verify(ctx, *, arg):
    # from sheets import col
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("drive.json", scope)

    driveClient = gspread.authorize(creds)

    sheet = driveClient.open("Verification").sheet1
    col = sheet.col_values(2)
    if arg in col:
        role = discord.utils.get(ctx.guild.roles, name='Unverified')
        await ctx.message.author.remove_roles(role)
        role = discord.utils.get(ctx.guild.roles, name='Verified')
        await ctx.message.author.add_roles(role)
        await ctx.message.delete()
    
client.run(data['token'])