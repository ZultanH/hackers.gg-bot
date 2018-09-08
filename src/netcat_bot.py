import discord
import asyncio
from discord.ext import commands
import botutils
import netcat

bot = commands.Bot(command_prefix = '!', pm_help = True, description = "A custom discord bot specialised for use with the hackers.gg api")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


class SpecificChannelOnly(commands.CheckFailure):
    pass


def is_correct_channel():
    def predicate(ctx):
        if ctx.message.server.id == '312252633794740225' and ctx.message.channel.id != '386931353855328266':
            raise SpecificChannelOnly("Incorrect Command Usage")
        return True
    return commands.check(predicate)

@bot.command(pass_context = True, description = "Checks if the bot is still running. Will return 'pong' on complete")
@is_correct_channel()
async def ping(ctx):
    await bot.send_message(ctx.message.channel, botutils.Reply(ctx, "pong"))
    
@bot.command(pass_context = True, name = "ncpoints", description = "Allows you to see how many points this user has from solving challenges")
@is_correct_channel()
async def NetCat(ctx):
    if ctx.message.mentions and ctx.message.mentions[0]:
        try:
            cls = netcat.netcat(ctx.message.mentions[0].id)
            await bot.send_message(ctx.message.channel, "[NetCat API] ~ User {} has {} points.".format(cls.username, cls.points))
            
        except ValueError as e:
            await bot.send_message(ctx.message.channel, "[NetCat API] ~ {}".format(e))
            return

@bot.command(pass_context = True, name = 'ncrank', description = "Allows you to see what rank this user has on the website")
@is_correct_channel()
async def NetCatRank(ctx):
    if ctx.message.mentions and ctx.message.mentions[0]:
        try:
            cls = netcat.netcat(ctx.message.mentions[0].id)
            await bot.send_message(ctx.message.channel, "[NetCat API] ~ User {}'s rank is {}".format(cls.username, cls.rank))
            
        except ValueError as e:
            await bot.send_message(ctx.message.channel, "[NetCat API] ~ {}".format(e))
            return
        
@bot.command(pass_context = True, name = 'ncchallenges', description = "Allows you to see what challenges this user has completed")
@is_correct_channel()
async def NetCatChallenges(ctx):
    if ctx.message.mentions and ctx.message.mentions[0]:
        try:
            cls = netcat.netcat(ctx.message.mentions[0].id)
            challengelist = ""

            for challenge in cls.complete_challenges:
                challengelist += challenge + "\n"

            await bot.send_message(ctx.message.channel, "[NetCat API] ~ User {} has completed {} challenges:\n{}".format(cls.username, len(cls.complete_challenges), challengelist))
            
        except ValueError as e:
            await bot.send_message(ctx.message.channel, "[NetCat API] ~ {}".format(e))
            return
        
bot.run('')
