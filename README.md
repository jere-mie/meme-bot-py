# Meme-Bot
## What it does
### There are several functions that my bot has, namely:
~**User verification** using the Google Sheets API to make sure users have registered before joining the server

~**Meme creation** using PIL, where users can use the !meme command to specify text to go on any of the 12 meme templates included.

~**Random joke** using the pyjokes API, where users can use the !joke command to get a joke from the bot.

~**Anonymous messages**, where users can send an anonymous message to the channel with the !anon command

~**Purge messages** (Admin only) for easy channel cleanup

~**Magic 8 Ball** via the !ask command, where the user gets a response to a question

~**Coin flip** and **custom dice rolling** via the !flip and !roll commands

## How I built it
The **overall bot** is written with the **discord.py API**.
**Verification** is done using the **Google Cloud Platform**, where a **Google Form** is used for registration, which automatically populates a **Google Sheet**, whereby the bot fetches the info from the **Google Drive and Google Sheets APIs** to validate user verification.
**Meme Creation** is done using ***PIL (the Python Imaging Library)** whereby text is affixed to various template images based on user input.
**Random Jokes** are fetched via the **pyjokes API**

## Challenges I ran into
As this was my first real Discord Bot, I found it difficult to traverse through the documentation, making it difficult to figure out how to manage roles necessary for verification.
Moreover, it was difficult to get the PIL meme creation working properly, as I had to hand-tune certain settings to make the text look presentable.

## Accomplishments that I'm proud of
I am proud of my accomplishment of successfully building and deploying a fully-featured Discord bot.
The two features that I am proud of are **verification and meme creation**. Both of these features required me to step outside my comfort zone and learn to use external APIs. 

## What I learned
This is my first Discord bot so I learned how to use **discord.py** over the weekend.
Moreover, it was my first time using the **Google Cloud Platform**, and my first time doing **image manipulation** (which I accomplished via **PIL**).
This is my first time using many different APIs in one project, so I definitely learned how to **compartmentalize and organize** them in a way that is legible.

## What's next for Meme Bot
I plan on adding **new meme templates**, as well as **new commands** based on user requests. Moreover, I plan on **adding Meme Bot** to some of the **various servers** I am a part of **so that real people can use it**.

## Domain.com Prize
I submit the domain http://make-memes.online for the best domain registered with Domain.com challenge

## APIs Used
~Google Drive API

~Google Sheets API

~Discord.py API

~Pyjokes API

~PIL (Python Imagine Library) API

## Best Use of Google Cloud
I utilize various Google services to employ secure and seamless verification for my bot.
These include: **Google Cloud Platform, Google Drive API, Google Sheets API, and Google Forms, as well as Google Sites** to host information about my bot.
Users fill out a **Google Form**, which populates a **Google Sheet**, which is fetched via the **Google Drive API and Google Sheets API** (from the **Google Cloud Platform**) and matched against user input. This allows users to verify themselves quickly, easily, and safely.
