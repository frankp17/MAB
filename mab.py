from optparse import TitledHelpFormatter
import yfinance as yf
import discord
from discord import embeds, Color
from discord.ext import tasks, commands
import requests
import json 
import pandas as pd
from emoji import emojize
from etherscan import Etherscan
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
from colorama import Fore, Back, Style
from urllib.request import Request, urlopen
import time
import asyncio
import random

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    NftPriceLoop.start()

@tasks.loop(seconds = 30)
async def NftPriceLoop():
  today = datetime.now()
  d1 = today.strftime("%b %d")
  currenttime = today.strftime("%I:%M %p EST")
  currenttime = currenttime.lstrip('0')
  
  channel = client.get_channel(946862359731916850)

  url_bayc = "https://api.opensea.io/api/v1/collection/boredapeyachtclub/stats"
  response_bayc = requests.request("GET", url_bayc)
  try:
    floor_bayc = response_bayc.json()
  except ValueError:
    asyncio.sleep(5)
    floor_bayc = response_bayc.json()
  x_bayc = pd.DataFrame.from_dict(floor_bayc)
  y_bayc = (x_bayc.T)
  BAYCfloor = y_bayc[['floor_price']]
  BAYCfloor = BAYCfloor.iat[0,0]
  BAYCchange = y_bayc[['one_day_change']]
  BAYCchange = BAYCchange.iat[0,0]
  BAYCsales = y_bayc[['one_day_sales']]
  BAYCsales = BAYCsales.iat[0,0]
  BAYCvol = y_bayc[['one_day_volume']]
  BAYCvol = BAYCvol.iat[0,0]
  bayc_marketcap = y_bayc[['market_cap']]
  bayc_marketcap = bayc_marketcap.iat[0,0]
  bayc_marketcap = round(float(bayc_marketcap), 0)
  BAYCfloor = round(float(BAYCfloor), 0)
  BAYCsales = round(float(BAYCsales), 0)
  BAYCvol = round(float(BAYCvol), 2)
  BAYCfloor = str(BAYCfloor)
  BAYCsales = int(BAYCsales)
  BAYCsales = str(BAYCsales)
  BAYCvol = float(BAYCvol)
  BAYCchange = float(BAYCchange)
  bayc_marketcap = float(bayc_marketcap)

  url_mayc = "https://api.opensea.io/api/v1/collection/mutant-ape-yacht-club/stats"
  response_mayc = requests.request("GET", url_mayc)
  try:
    floor_mayc = response_mayc.json()
  except ValueError:
    asyncio.sleep(5)
    floor_mayc = response_mayc.json()
  x_mayc = pd.DataFrame.from_dict(floor_mayc)
  y_mayc = (x_mayc.T)
  MAYCfloor = y_mayc[['floor_price']]
  MAYCfloor = MAYCfloor.iat[0,0]
  MAYCchange = y_mayc[['one_day_change']]
  MAYCchange = MAYCchange.iat[0,0]
  MAYCsales = y_mayc[['one_day_sales']]
  MAYCsales = MAYCsales.iat[0,0]
  MAYCvol = y_mayc[['one_day_volume']]
  MAYCvol = MAYCvol.iat[0,0]
  mayc_marketcap = y_mayc[['market_cap']]
  mayc_marketcap = mayc_marketcap.iat[0,0]
  mayc_marketcap = round(float(mayc_marketcap), 0)
  
  MAYCfloor = round(float(MAYCfloor), 2)
  MAYCsales = round(float(MAYCsales), 0)
  MAYCvol = round(float(MAYCvol), 2)
  MAYCfloor = str(MAYCfloor)
  MAYCsales = int(MAYCsales)
  MAYCsales = str(MAYCsales)
  MAYCvol = float(MAYCvol)
  MAYCchange = float(MAYCchange)
  mayc_marketcap = float(mayc_marketcap)

  url_a = "https://api.opensea.io/api/v1/collection/azuki/stats"
  response_a = requests.request("GET", url_a)
  try:
    floor_a = response_a.json()
  except ValueError:
    asyncio.sleep(5)
    floor_a = response_a.json()
  x_a = pd.DataFrame.from_dict(floor_a)
  y_a = (x_a.T)
  afloor = y_a[['floor_price']]
  afloor = afloor.iat[0,0]
  achange = y_a[['one_day_change']]
  achange = achange.iat[0,0]
  asales = y_a[['one_day_sales']]
  asales = asales.iat[0,0]
  avol = y_a[['one_day_volume']]
  avol = avol.iat[0,0]
  a_marketcap = y_a[['market_cap']]
  a_marketcap = a_marketcap.iat[0,0]
  a_marketcap = round(float(a_marketcap), 0)
  afloor = round(float(afloor), 2)
  asales = round(float(asales), 0)
  avol = round(float(avol), 2)
  afloor = str(afloor)
  asales = int(asales)
  asales = str(asales)
  avol = float(avol)
  achange = float(achange)
  a_marketcap = float(a_marketcap)

  url_h = "https://api.opensea.io/api/v1/collection/hapeprime/stats"
  response_h = requests.request("GET", url_h)
  try:
    floor_h = response_h.json()
  except ValueError:
    asyncio.sleep(5)
    floor_h = response_h.json()
  x_h = pd.DataFrame.from_dict(floor_h)
  y_h = (x_h.T)
  hfloor = y_h[['floor_price']]
  hfloor = hfloor.iat[0,0]
  hchange = y_h[['one_day_change']]
  hchange = hchange.iat[0,0]
  hsales = y_h[['one_day_sales']]
  hsales = hsales.iat[0,0]
  hvol = y_h[['one_day_volume']]
  hvol = hvol.iat[0,0]
  h_marketcap = y_h[['market_cap']]
  h_marketcap = h_marketcap.iat[0,0]
  h_marketcap = round(float(h_marketcap), 0)
  hfloor = round(float(hfloor), 2)
  hsales = round(float(hsales), 0)
  hvol = round(float(hvol), 2)
  hfloor = str(hfloor)
  hsales = int(hsales)
  hsales = str(hsales)
  hvol = float(hvol)
  hchange = float(hchange)
  h_marketcap = float(h_marketcap)

  url_c = "https://api.opensea.io/api/v1/collection/clonex/stats"
  response_c = requests.request("GET", url_c)
  try:
    floor_c = response_c.json()
  except ValueError:
    asyncio.sleep(5)
    floor_c = response_c.json()
  x_c = pd.DataFrame.from_dict(floor_c)
  y_c = (x_c.T)
  cfloor = y_c[['floor_price']]
  cfloor = cfloor.iat[0,0]
  cchange = y_c[['one_day_change']]
  cchange = cchange.iat[0,0]
  csales = y_c[['one_day_sales']]
  csales = csales.iat[0,0]
  cvol = y_c[['one_day_volume']]
  cvol = cvol.iat[0,0]
  c_marketcap = y_c[['market_cap']]
  c_marketcap = c_marketcap.iat[0,0]
  c_marketcap = round(float(c_marketcap), 0)
  cfloor = round(float(cfloor), 2)
  csales = round(float(csales), 0)
  cvol = round(float(cvol), 2)
  cfloor = str(cfloor)
  csales = int(csales)
  csales = str(csales)
  cvol = float(cvol)
  cchange = float(cchange)
  c_marketcap = float(c_marketcap)

  url_sand = "https://api.opensea.io/api/v1/collection/sandbox/stats"
  response_sand = requests.request("GET", url_sand)
  try:
    floor_sand = response_sand.json()
  except ValueError:
    asyncio.sleep(5)
    floor_sand = response_sand.json()
  x_sand = pd.DataFrame.from_dict(floor_sand)
  y_sand = (x_sand.T)
  sandfloor = y_sand[['floor_price']]
  sandfloor = sandfloor.iat[0,0]
  sandchange = y_sand[['one_day_change']]
  sandchange = sandchange.iat[0,0]
  sandsales = y_sand[['one_day_sales']]
  sandsales = sandsales.iat[0,0]
  sandvol = y_sand[['one_day_volume']]
  sandvol = sandvol.iat[0,0]
  sand_marketcap = y_sand[['market_cap']]
  sand_marketcap = sand_marketcap.iat[0,0]
  sand_marketcap = round(float(sand_marketcap), 0)
  sandfloor = round(float(sandfloor), 2)
  sandsales = round(float(sandsales), 0)
  sandvol = round(float(sandvol), 2)
  sandfloor = str(sandfloor)
  sandsales = int(sandsales)
  sandsales = str(sandsales)
  sandvol = float(sandvol)
  sandchange = float(sandchange)
  sand_marketcap = float(sand_marketcap)
  
  myMsg = discord.Embed(title = '**NFT PRICES**', url = 'https://opensea.io/rankings?sortBy=total_volume', description = 
  f'{d1} | {currenttime}' + '\n\n' +
  '[**Bored Ape Yacht Club**](https://opensea.io/collection/boredapeyachtclub)' + '\n'
  'Floor Price: ' + BAYCfloor + ' ' + 'ETH' + '\n' + 
  'One-Day-Change: ' + "{0:.2%}".format(BAYCchange) + '\n' + 
  'One-Day-Sales: ' + BAYCsales + '\n' + 
  'One-Day-Vol: ' + '{:,}'.format(BAYCvol) + ' ' + 'ETH' + '\n' + 
  'Market Cap: ' + '{:,}'.format(bayc_marketcap) + ' ' + 'ETH' + '\n\n' +
  '[**Mutant Ape Yacht Club**](https://opensea.io/collection/mutant-ape-yacht-club)' + '\n' + 
  'Floor Price: ' + MAYCfloor + ' ' + 'ETH' + '\n' + 
  'One-Day-Change: ' + "{0:.2%}".format(MAYCchange) + '\n' + 
  'One-Day-Sales: ' + MAYCsales + '\n' + 
  'One-Day-Vol: ' + '{:,}'.format(MAYCvol) + ' ' + 'ETH' + '\n' + 
  'Market Cap: ' + '{:,}'.format(mayc_marketcap) + ' ' + 'ETH' + '\n\n' + 
  '[**Azuki**](https://opensea.io/collection/azuki)' + '\n' +
  'Floor Price: ' + afloor + ' ' + 'ETH' + '\n' +
  'One-Day-Change: ' + "{0:.2%}".format(achange) + '\n' + 
  'One-Day-Sales: ' + asales + '\n' + 
  'One-Day-Vol: ' + '{:,}'.format(avol) + ' ' + 'ETH' + '\n' + 
  'Market Cap: ' + '{:,}'.format(a_marketcap) + ' ' + 'ETH' + '\n\n' + 
  '[**HAPE Prime**](https://opensea.io/collection/hapeprime)' + '\n' +
  'Floor Price: ' + hfloor + ' ' + 'ETH' + '\n' + 
  'One-Day-Change: ' + "{0:.2%}".format(hchange) + '\n' + 
  'One-Day-Sales: ' + hsales + '\n' + 
  'One-Day-Vol: ' + '{:,}'.format(hvol) + ' ' + 'ETH' + '\n' + 
  'Market Cap: ' + '{:,}'.format(h_marketcap) + ' ' + 'ETH' + '\n\n' + 
  '[**Clone X**](https://opensea.io/collection/clonex)' + '\n' + 
  'Floor Price: ' + cfloor + ' ' + 'ETH' + '\n' + 
  'One-Day-Change: ' + "{0:.2%}".format(cchange) + '\n' + 
  'One-Day-Sales: ' + csales + '\n' + 
  'One-Day-Vol: ' + '{:,}'.format(cvol) + ' ' + 'ETH' + '\n' + 
  'Market Cap: ' + '{:,}'.format(c_marketcap) + ' ' + 'ETH' + '\n\n' + 
  '[**The Sandbox**](https://opensea.io/collection/sandbox)' + '\n' + 
  'Floor Price: ' + sandfloor + ' ' + 'ETH' + '\n' + 
  'One-Day-Change: ' + "{0:.2%}".format(sandchange) + '\n' + 
  'One-Day-Sales: ' + sandsales + '\n' + 
  'One-Day-Vol: ' + '{:,}'.format(sandvol) + ' ' + 'ETH' + '\n' + 
  'Market Cap: ' + '{:,}'.format(sand_marketcap) + ' ' + 'ETH' + '\n\n')
  msg_id = 946869711621197875
  lastmsg = await channel.fetch_message(msg_id)
  await lastmsg.edit(embed=myMsg)

client.run(TOKEN)