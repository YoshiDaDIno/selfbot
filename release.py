import discord
from discord.ext import commands
import subprocess
import pyfiglet
import time
import io, requests, json

client = commands.Bot(command_prefix=".", self_bot=True)

token = ""


def yeah(cmd):
    subprocess.call(cmd, shell=True)


def ui():
    print()
    result = pyfiglet.figlet_format("Jordan's")
    print(result)
    result2 = pyfiglet.figlet_format("Selfbot")
    print(result2)
    print()


ui()


@client.event
async def on_ready():
    print("[-] User: {0} [-]".format(client.user))


@client.command()
async def h(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="List of all commands:", url="http://jordy.wtf", color=0x00abff)
    embed.add_field(name="[1] .d (amt)", value="Deletes your messages, leave amount blank to delete all.", inline=True)
    embed.add_field(name="[2] .purge (amt)", value="Deletes everyones messages, leave amount blank to delete all.",
                    inline=True)
    embed.add_field(name="[3] .createchannels (text)", value="Creates text channels following the text given.",
                    inline=True)
    embed.add_field(name="[4] .deletechannels", value="Deletes all text channels.", inline=True)
    embed.add_field(name="[5] .nuke", value="Bans all users from the discord and deletes all channels.", inline=True)
    embed.add_field(name="[6] .ascii (text)", value="Outputs input into ascii text.", inline=True)
    embed.add_field(name="[7] .ban (user) (reason)", value="Bans the mentioned user from the discord.", inline=True)
    embed.add_field(name="[8] .kick (user) (reason)", value="Kicks the mentioned user from the discord.", inline=True)
    embed.add_field(name="[9] .mute (user)", value="Mutes user in voice channels.", inline=True)
    embed.add_field(name="[10] .unmute (user)", value="Unmutes user in voice channels.", inline=True)
    embed.add_field(name="[11] .nick (name)", value="Will change your nickname to the input.", inline=True)
    embed.add_field(name="[12] .av (user)", value="Outputs the avatar of the mentioned user.", inline=True)
    embed.add_field(name="[13] .spamdm (user) (amt) (text)", value="Spam's mentioned user X amount of times.",
                    inline=True)
    embed.add_field(name="[14] .spam (text)", value="Sends each character from the input separately.", inline=True)
    embed.add_field(name="[15] .repeat (amt) (text)", value="Repeats the same line X amount of times.", inline=True)
    embed.add_field(name="[16] .quote (ID)", value="Sends an embed quoting the message by ID.", inline=True)
    embed.add_field(name="[17] .role (user) (role)", value="Adds or removes the role to the mentioned user.",
                    inline=True)
    embed.add_field(name="[18] .dmnuke", value="Purges DM's with all friends.", inline=True)
    embed.add_field(name="[19] .dog", value="Outputs a random dog picture.", inline=True)
    embed.add_field(name="[21] .ui (user)", value="Outputs information for the mentioned user.", inline=True)
    embed.add_field(name="[21] .close", value="Closes the selfbot", inline=True)
    embed.set_footer(text="SelfBot made by jordan")
    await ctx.send(embed=embed)


'Command - (1) .D - Delete Messages'


@client.command()
async def d(ctx, amt=9998):
    c = 0
    await ctx.message.delete()
    mymessage = await ctx.send(":bomb:")
    time.sleep(1)
    await mymessage.edit(content=":boom:")
    async for msg in ctx.message.channel.history(limit=amt + 2):
        if msg.author == client.user:
            try:
                await msg.delete()
                c = c + 1
            except Exception as x:
                pass
    message = await ctx.send("Deleted %d messages successfully!" % c)
    time.sleep(3)
    await message.delete()


'Command - (2) .Purge'


@client.command()
async def purge(ctx, amt=9998):
    c = 0
    await ctx.message.delete()
    async for msg in ctx.message.channel.history(limit=int(amt + 1)):
        try:
            await msg.delete()
            c = c + 1
        except Exception as x:
            pass
    message = await ctx.send("Deleted %d messages successfully!" % c)
    time.sleep(3)
    await message.delete()


'Command - (3) .CreateChannels'


@client.command()
async def createchannels(ctx, amt=None):
    await ctx.message.delete()
    if amt is not None:
        for i in amt:
            await ctx.guild.create_text_channel(i)
        await ctx.send(":white_check_mark: Channels Created.")
    else:
        await ctx.send(":negative_squared_cross_mark: You need to input text that will be used to create channels!")


'Command - (4) .DeleteChannels'


@client.command()
async def deletechannels(ctx):
    for channel in ctx.guild.text_channels:
        try:
            await channel.delete()
        except:
            print(f"The channel: {channel} could not be deleted!")
    await ctx.guild.create_text_channel("bump")


'Command - (5) .Nuke'


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.text_channels:
        await channel.delete()
    await ctx.guild.create_text_channel("lol")
    for member in ctx.guild.members:
        if member != client.user:
            await ctx.send("Kicked user: %s" % str(member))
            await ctx.message.guild.kick(member, reason="nigger")
    await ctx.send("Successfully nuked the server!")


'Command - (6) .ASCII'


@client.command()
async def ascii(ctx, *, message: str = None):
    f = pyfiglet.Figlet(font='big')
    if message is not None:
        try:
            await ctx.message.edit(content=f'```http\n{f.renderText(message)}```')
        except discord.HTTPException:
            await ctx.message.delete()
            message = await ctx.send(":negative_squared_cross_mark: Message too large!")
            time.sleep(3)
            await message.delete()
    else:
        message = await ctx.send(":negative_squared_cross_mark: You need to input text to be converted!")
        time.sleep(3)
        await message.delete()


'Command - (7) .Ban'


@client.command()
async def ban(ctx, user: discord.Member = None, *, reason=None):
    await ctx.message.delete()
    if user is not None:
        if reason is not None:
            try:
                await ctx.message.guild.ban(user, reason=reason)
                message = await ctx.send(":white_check_mark: Banned user: `%s` for: `%s`." % (str(user), reason))
            except:
                message = await ctx.send(":negative_squared_cross_mark: %s can not be banned." % str(user))
        else:
            message = await ctx.send(":negative_squared_cross_mark: Please state a reason!")
    else:
        message = await ctx.send(":negative_squared_cross_mark: Please mention a user!")
    time.sleep(3)
    await message.delete()


'Command - (8) .Kick'


@client.command()
async def kick(ctx, user: discord.Member = None, *, reason=None):
    await ctx.message.delete()
    if user is not None:
        if reason is not None:
            await ctx.message.guild.kick(user, reason=reason)
            message = await ctx.send(":white_check_mark: Kicked user: `%s` for: `%s`." % (str(user), reason))
        else:
            message = await ctx.send(":negative_squared_cross_mark: Please state a reason!")
    else:
        message = await ctx.send(":negative_squared_cross_mark: Please mention a user!")
    time.sleep(3)
    await message.delete()


'Command - (9) .Mute'


@client.command()
async def mute(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is not None:
        await user.edit(mute=True)
        message = await ctx.send("Muted user: `%s`." % str(user))
    else:
        message = await ctx.send(":negative_squared_cross_mark: Please mention a user!")
    time.sleep(3)
    await message.delete()


'Command - (10) .Unmute TODO - Change mute command to check if muted'


@client.command()
async def unmute(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is not None:
        await user.edit(mute=False)
        message = await ctx.send("Unmuted user: `%s`." % str(user))
    else:
        message = await ctx.send(":negative_squared_cross_mark: Please mention a user!")
    time.sleep(3)
    await message.delete()


'Command - (11) .Nick'


@client.command()
async def nick(ctx, nickname=None, user: discord.Member = None):
    await ctx.message.delete()
    if user is not None:
        if nickname != 'reset':
            message = await ctx.send("`%s's` nickname has been set to: `%s`." % (user, nickname))
            await user.edit(nick=nickname)
        else:
            message = await ctx.send("%s's nickname has been reset." % user)
            await user.edit(nick=None)
    else:
        user = ctx.message.author
        await user.edit(nick=nickname)
        if nickname is not None:
            message = await ctx.send("Your nickname has been set to: `%s.`" % nickname)
        else:
            message = await ctx.send("Your nickname has been reset.")
    time.sleep(5)
    await message.delete()


'Command - (12) .Av'


@client.command()
async def av(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.message.author
    url = user.avatar_url
    embedded = discord.Embed(title="Avatar of %s" % str(user))
    embedded.set_image(url=url)
    if url:
        await ctx.send(embed=embedded)


'Command - (13) .SpamDM'


@client.command()
async def spamdm(ctx, user: discord.Member = None, amt=10, *, spam=None):
    await ctx.message.delete()
    if user is not None:
        if spam is not None:
            message = await ctx.send("[%d] Sending the message: `%s` to: `%s`" % (amt, spam, user))
            channel = await user.create_dm()
            for i in range(int(amt)):
                inc = i + 1
                await channel.send("[%d/%d] %s" % (inc, amt, spam))
        else:
            message = await ctx.send(":negative_squared_cross_mark: Please specify a message!")
    else:
        message = await ctx.send(":negative_squared_cross_mark: Please mention a user!")
    time.sleep(3)
    await message.delete()


'Command - (14) .Spam'


@client.command()
async def spam(ctx, *, message=None):
    if message is not None:
        await ctx.message.delete()
        message = str(message).replace(' ', '')
        for i in message:
            await ctx.send(i)
    else:
        message = await ctx.send(":negative_squared_cross_mark: You need to input a message to spam!")
        time.sleep(3)
        await message.delete()


'Command - (15) .Repeat'


@client.command()
async def repeat(ctx, *, message=None, amt=9):
    await ctx.message.delete()
    if message is not None:
        for x in range(int(amt)):
            inc = x + 1
            await ctx.send("[%d/%d] %s" % (inc, amt, message))


'Command - (16) .Quote'


@client.command()
async def quote(ctx, msgid=None):
    await ctx.message.delete()
    if msgid is not None:
        async for message in ctx.message.channel.history(limit=500):
            if message.id == int(msgid):
                mess = message
        if mess is not None:
            em = discord.Embed(description=mess.clean_content, timestamp=mess.created_at, colour=0x00abff)
            em.set_author(name=mess.author.display_name, icon_url=mess.author.avatar_url)
        await ctx.send(embed=em)
    else:
        message = await ctx.send(":negative_squared_cross_mark: Please specify a message using the message ID!")
        time.sleep(3)
        await message.delete()


'Command - (17) .Role'


@client.command()
async def role(ctx, user: discord.Member = None, role: discord.Role = None):
    if user is not None:
        if role is not None:
            if role in user.roles:
                message = await ctx.send(f":white_check_mark: {user.name} already had that role, removing it now.")
                await user.remove_roles(role)
            else:
                await user.add_roles(role)
                message = await ctx.send(f":white_check_mark: {user.name} has been given a role called: {role.name}")
        else:
            message = await ctx.send(":negative_squared_cross_mark: Please specify a role!")
    else:
        message = await ctx.send(":negative_squared_cross_mark: Please mention a user!")
    time.sleep(3)
    await message.delete()


'Command - (18) .Close'


@client.command()
async def close(ctx):
    await ctx.message.delete()
    await ctx.send("Closing...")
    exit()


'Command - (19) .DMNuke'


@client.command()
async def dmnuke(ctx):
    await ctx.message.delete()
    for user in client.user.friends:
        print(user)
        channel = await user.create_dm()
        async for msg in channel.history(limit=9999):
            if msg.author == client.user:
                try:
                    await msg.delete()
                    print('Message Deleted')
                except Exception as x:
                    pass
    for user in client.user.blocked:
        print(user)
        channel = await user.create_dm()
        async for msg in channel.history(limit=9999):
            if msg.author == client.user:
                try:
                    await msg.delete()
                    print('Message Deleted')
                except Exception as x:
                    pass
    await ctx.send('Deleted all DMs')


@client.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get('http://shibe.online/api/shibes')
    dog = str(r.json()).replace("[", "").replace("'", "").replace("]", "")
    embedded = discord.Embed()
    embedded.set_image(url=dog)
    mymessage = await ctx.send(embed=embedded)
    time.sleep(5)
    await mymessage.delete()


@client.command()
async def advice(ctx):
    await ctx.message.delete()
    r = requests.get('https://api.adviceslip.com/advice')
    await ctx.send(r.json()['slip']['advice'])


'https://github.com/appu1232/Discord-Selfbot/blob/master/cogs/misc.py for avatar stealer - setavatar TODO'


@client.command()
async def setavatar(ctx, user: discord.Member):
    """
    Set an avatar from a URL or user.
    Usage: [p]setavatar <url_to_image> or [p]setavatar <user> to copy that user's avi
    Image URL must be a .png, a .jpg, or a .gif (nitro only)
    """
    if user:
        url = user.avatar_url_as(static_format='png')
    else:
        url = msg
    response = requests.get(url, stream=True)
    img = io.BytesIO()
    for block in response.iter_content(1024):
        if not block:
            break

        img.write(block)

    if url:
        img.seek(0)
        imgbytes = img.read()
        img.close()
        with open('settings/avatars.json', 'r+') as fp:
            opt = json.load(fp)
            if opt['password']:
                if opt['password'] == "":
                    await ctx.send(
                        self.bot.bot_prefix + "You have not set your password yet in `settings/avatars.json` Please do so and try again")
                else:
                    pw = opt['password']
                    try:
                        await user.edit(avatar=imgbytes, password=pw)
                        await ctx.send("Your avatar has been set to the specified image.")
                    except discord.errors.HTTPException:
                        await ctx.send("You are being rate limited!")
            else:
                await ctx.send(
                    "You have not set your password yet in `settings/avatars.json` Please do so and try again")
    else:
        await ctx.send(self.bot.bot_prefix + 'Could not find image.')


'TODO - List, doesnt list all'


@client.command()
async def list(ctx):
    members = ''
    c = 0
    for member in ctx.guild.members:
        members = members + "\n" + str(member)
        c = c + 1
    await ctx.send("There are " + str(c) + " members\n" + members)


@client.command()
async def mc(ctx, ign='Professed'):
    await ctx.message.delete()
    await ctx.send("https://plancke.io/hypixel/player/stats/" + ign)


@client.command()
async def ui(ctx, *, name=""):
    """Get user info. Ex: [p]info @user"""
    if ctx.invoked_subcommand is None:
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                user = ctx.guild.get_member(int(name))
            if not user:
                user = self.bot.get_user(int(name))
            if not user:
                await ctx.send(self.bot.bot_prefix + 'Could not find user.')
                return
        else:
            user = ctx.message.author
        avi = user.avatar_url

        if isinstance(user, discord.Member):
            role = user.top_role.name
            if role == "@everyone":
                role = "N/A"
            voice_state = None if not user.voice else user.voice.channel
            em = discord.Embed(timestamp=ctx.message.created_at, colour=0x708DD0)
            em.add_field(name='User ID', value=user.id, inline=True)
            if isinstance(user, discord.Member):
                em.add_field(name='Nick', value=user.nick, inline=True)
                em.add_field(name='In Voice', value=voice_state, inline=True)
                em.add_field(name='Game', value=user.activity, inline=True)
                em.add_field(name='Highest Role', value=role, inline=True)
            em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
            if isinstance(user, discord.Member):
                em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
            em.set_thumbnail(url=avi)
            em.set_author(name=user,
                          icon_url='https://cdn.discordapp.com/avatars/214920338968936448/c1a9d59edf66ab047d1c997e9fa45fa3.webp?size=1024')
            await ctx.send(embed=em)
        await ctx.message.delete()


client.run(token, bot=False)