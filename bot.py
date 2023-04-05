import discord
from discord.ext import commands
from textblob import TextBlob
from datetime import datetime, timedelta

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def sentiment(ctx):
    # Check if the user has the admin role
    admin_role_id = 1083737606778527744
    admin_role = discord.utils.get(ctx.guild.roles, id=admin_role_id)
    if admin_role not in ctx.author.roles:
        await ctx.send("Sorry, you don't have permission to use this command.")
        return

    # Get the list of channels to check
    channels_to_exclude = [1083737606778527744, 2222227606778527744]  # role IDs to exclude
    channels = [channel for channel in ctx.guild.channels if channel.type == discord.ChannelType.text and channel.id not in channels_to_exclude]

    # Calculate the start and end dates
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=10)

    # Display a message indicating that the bot is working
    await ctx.send("I'm calculating the average of the past 10 days.")

    # Iterate through all the channels and calculate the sentiment
    total_polarity = 0
    total_subjectivity = 0
    message_count = 0
    for channel in channels:
        async for message in channel.history(after=start_date, before=end_date):
            if message.author.id not in channels_to_exclude:
                blob = TextBlob(message.content)
                total_polarity += blob.sentiment.polarity
                total_subjectivity += blob.sentiment.subjectivity
                message_count += 1

    # Calculate the average sentiment
    if message_count == 0:
        await ctx.send("No messages found in the past 10 days.")
    else:
        average_polarity = total_polarity / message_count
        average_subjectivity = total_subjectivity / message_count
        await ctx.send(f"The average sentiment of the last 10 days on the server is {average_polarity:.2f} (polarity) and {average_subjectivity:.2f} (subjectivity).")
bot.run('YOURTOKEN')
