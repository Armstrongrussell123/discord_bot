from discord.ext.commands import Bot
from discord import Game
import discord
import json
import requests
import asyncio
import time
from d_bot.lib.rss import *
import re

TOKEN = 'NTQzMTQ4Nzk5NzQ5NzgzNTcz.Dz5sRA.sE8y8SjEcH7JoUiyVgYwgoozOH8'
BOT_PREFIX = ("?","!")
WEATHER_API = "https://fcc-weather-api.glitch.me/api/current?lat=39.3722&lon=104.8561"



bot = Bot(command_prefix=BOT_PREFIX)


@bot.command()
async def echo(e):
    await bot.say(e)




@bot.command()
async def weather():
    res = requests.get(WEATHER_API)
    weather = json.loads(res.text)

    await bot.say(weather['main']['temp'])

@bot.command()
async def oldy():
    await bot.say("https://archive.org/details/Against_The_Storm/1940-05-13_-_xxxx_-_Against_The_Storm_-_Supper_In_The_Park_-_32-16_-_14m54s.mp3")


@bot.command()
async def rtitle():
    await bot.say(print_title())

@bot.command(pass_context=True)
async def reddit(context):
    end = 1
    msg = context.message.content
    print('I GOT {}'.format(msg))
    sr = msg.split()
    if len(sr) <= 1:
        subreddit = reddit_url(None)
        feed = get_rss(subreddit)
        for i in get_entries(feed):
            await bot.say(i)
    if len(sr) >= 2:
        subreddit = reddit_url(None)
        feed = get_rss(subreddit)
        if sr[1] == "random":
            await bot.say(get_random_entry(feed))
        elif re.match("(\d+)",sr[1]):
            end = int(sr[1])
            for i in get_entries(feed,start=0,end=end):
                await bot.say(i)
        else:
            subreddit = reddit_url(sr[1])
            feed = get_rss(subreddit)
            if len(sr) >= 3:
                if sr[2] == "random":
                    await bot.say(get_random_entry(feed))
                else:
                    try:
                        end = int(sr[2])
                    except:
                        end = 1
                    for i in get_entries(feed, start=0, end=end):
                        await bot.say(i)


@bot.command(pass_context=True)
async def rss(context):
    msg = context.message.content
    print('I GOT {}'.format(msg))
    sr = msg.split()
    end = 1
    if len(sr) <= 1:
        await bot.say("I need a url and a number of items from that page")
    if len(sr) >= 2:
        feed = get_rss(sr[1])
        if len(sr) >= 3:
            try:
                end = int(sr[2])
            except:
                await bot.say("I need a number, you said: {}".format(sr[2]))
        for i in get_entries(feed,start=0,end=end):
            await bot.say(i)


@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="with humans"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)