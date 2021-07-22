import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print('Bot connected!')
    await bot.get_channel(772852314359726115).send('Connected!')

guilds = [772852314359726111]

@slash.slash(name="test", guild_ids=guilds)
async def _test(ctx):
    await ctx.send('testing')

@slash.slash(name="price", options=[create_option('symbol', description="what ticker?", option_type=3, required=True)], guild_ids=guilds)
async def _price(ctx, symbol: str):
    await ctx.send(get_price(symbol))

@bot.command()
async def countdown(ctx, count: int=5):
    for i in range(count, 0, -1):
        await ctx.send(i)

def get_price(symbol):
    import requests
    from pprint import pprint

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '29cb6142-265e-4850-acf0-6f7c05803c3f'
    }

    parameters = {
        'symbol': symbol
    }

    response = requests.get(url, headers=headers, params=parameters)

    data = response.json()

    try: 
        price = data.get('data').get(f'{str.upper(symbol)}').get('quote').get('USD').get('price')

        return f'${price:,.2f}'
    except:
        return ("Unable to get price")


@bot.command()
async def price(ctx, symbol: str):

    price = get_price(symbol)

    await ctx.send(price)


bot.run('ODY3NzM5OTc5ODg2NzU1ODYx.YPlf1Q.WjLC8N_0qJajElqMeZaUkFf2Ch8')