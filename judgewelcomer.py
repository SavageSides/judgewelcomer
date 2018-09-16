import discord
from discord.ext import commands

TOKEN  = 'NDkwOTY0MzE4NTY5ODg5ODIz.DoA9ww.HUOtsO4qGZdpS6xGxOjuVLUuu3c'

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print('Ready!')

@client.event
async def on_member_join(member):
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - >help"))
    server = member.server
    channel = discord.utils.get(server.channels, name='welcome')
    embed = discord.Embed(color=0xdaff00)
    embed.add_field(name=':inbox_tray: **{} Welcome**', value='Please read the rules of **{}**'.format(server.name), inline=False)
    embed.set_footer(text='Welcome!')
    await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - >help"))
    server = member.server
    channel = discord.utils.get(server.channels, name='welcome')
    embed = discord.Embed(color=0xdaff00)
    embed.add_field(name=':outbox_tray: **{}** Has left', value='He will be missed!', inline=True)
    embed.set_footer(text='Goodbye!')
    await client.send_message(channel, embed=embed)



client.run(TOKEN)
