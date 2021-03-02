from os import environ, listdir
from discord import Intents
from discord.ext import commands

__import__("dotenv").load_dotenv()
#Added by Running Child
#Start
with open("./cogs/statuses.txt","r") as status:
    startup_status=status.readline()
    type=startup_status.split(";")[0]
    activity=startup_status.split(";")[1]
    if type.lower()=="online":
	    status=discord.Status.online
	elif type.lower()=="idle":
		status=discord.Status.idle
	elif type.lower()=="busy" or type.lower()=="dnd" or type.lower()=="do_not_disturb":
		status=discord.Status.dnd
	elif type.lower()=="offline" or type.lower()=="invisible":
		status=discord.Status.invisible
bot = commands.Bot(command_prefix="py/", case_insensitive=True, intents=Intents.all(),status=status , activity=discord.Game(activity))

for cog in filter(lambda c: c.endswith(".py"), listdir("cogs/")):
    bot.load_extension(f"cogs.{cog[:-3]}")

admins_list=[662334026098409480,339660347499872256,286591003794604034]

@client.command()
async def load(ctx, extension):
    if ctx.message.author.id in admins_list:
        try:
            client.load_extension(f'cogs.{extension.lower()}')
            await ctx.send(extension + ' loaded.')
        except:
            await ctx.send("Something went wrong. Please,check terminal for getting more detailed info.")
    else:
        await ctx.send("You are not my master.")

@client.command()
async def unload(ctx, extension):
    if ctx.message.author.id in admins_list:
        try:
            client.unload_extension(f'cogs.{extension.lower()}')
            await ctx.send(extension+' unloaded. Feel free to edit this! =]')
        except:
            await ctx.send("Something went wrong. Please,check terminal for getting more detailed info.")
    else:
        await ctx.send("You are not my master.")


@client.command()
async def reload(ctx,cog):
    if ctx.message.author.id in admins_list:
        try:
            client.unload_extension(f'cogs.{cog.lower()}')
            client.load_extension(f"cogs.{cog.lower()}")
            await ctx.send(f"Reload of {cog.lower()} done.")
        except:
            await ctx.send("Something went wrong. Please,check terminal for getting more detailed info.")
    else:
        await ctx.send("You are not my master.")

#End


bot.run(environ["TOKEN"])