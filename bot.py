import discord; from discord.ext import commands
bot = discord.Bot(command_prefix='$', activity="https://github.com/hokuine", status=discord.Status.online, intents=discord.Intents.all())
@bot.command(name="payments")
async def p(a):
    await a.send(embed=discord.Embed(title="payments below").add_field(name="paypal", value="yourpp@domain").add_field(name="ltc", value="addy"))
