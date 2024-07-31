import discord

client = discord.Client()

# Initialize the emoji with a default value
auto_react_emoji = '☠'

user_token = input("Enter your user token: ")

user_id = None

async def get_user_id():
    # Fetch the user object using the token
    user = await client.fetch_user("@me")
    return user.id

@client.event
async def on_ready():
    global user_id
    user_id = await get_user_id()
    print(f'Logged in as {client.user}!')
    print(f'Enjoy auto reacting faggot')

@client.event
async def on_message(message):
    global auto_react_emoji

    if message.author.id == user_id and not message.author.bot:
        # Check if the message starts with !setemoji
        if message.content.startswith('!setemoji'):
            parts = message.content.split(' ', 1)
            if len(parts) == 2:
                auto_react_emoji = parts[1]
                await message.channel.send(f'Auto-react emoji set to: {auto_react_emoji}')
            else:
                await message.channel.send('Please provide an emoji. Usage: !setemoji <emoji>')
        else:
            # Add the auto-reaction emoji to the user's messages
            await message.add_reaction(auto_react_emoji)

client.run(user_token, bot=False)
