#Start
import discord
from discord.ext import commands
from time import sleep
import os
from os import system, name

admins_list=[662334026098409480,339660347499872256,286591003794604034]
class Appearance(commands.Cog):

	def __init__(self, client):
		self.client = client
	@commands.command()
	async def status(self, ctx,type, *, activity):
		if ctx.message.author.id in admins_list:
			if type.lower()=="online":
				status=discord.Status.online
				await ctx.send("Status successfully changed.")
			elif type.lower()=="idle":
				status=discord.Status.idle
				await ctx.send("Status successfully changed.")
			elif type.lower()=="busy" or type.lower()=="dnd" or type.lower()=="do_not_disturb":
				status=discord.Status.dnd
				await ctx.send("Status successfully changed.")
			elif type.lower()=="offline" or type.lower()=="invisible":
				status=discord.Status.invisible
				await ctx.send("Status successfully changed.")
			else:
				await ctx.send("Usage:\npy/status <type> <text>")
			await self.client.change_presence(status=status , activity=discord.Game(activity))
			with open('./cogs/statuses.txt', 'r+') as statuses:
				statuses.truncate(0)
				statuses.write(f"{type};{activity}")
		else:
			await ctx.send('U are not my master.')

	@status_cmd.error
	async def status_cmd_error(ctx,error):
		 if isinstance(error, commands.errors.MissingRequiredArgument):
			 with open('./cogs/statuses.txt', 'r') as statuses:
				 await ctx.send(statuses.read())


def setup(client):
	client.add_cog(Appearance(client))
#End