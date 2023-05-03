import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
class Paarthunax:
    def __init__(self, TOKEN, GUILD):
        self.TOKEN = TOKEN
        self.GUILD = GUILD
        self.intents = discord.Intents.all()
        self.client = discord.Client(intents=self.intents)

    def start(self):
        self.register_event_handlers()
        self.client.run(self.TOKEN)

    def register_event_handlers(self):
        @self.client.event
        async def on_ready():
            guild = discord.utils.get(self.client.guilds, name=self.GUILD)
            members = '\n - '.join([member.name for member in guild.members])
            # print(f'Guild Members:\n - {members}')

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            if 'sergi la chupa' in message.content.lower():
                await message.channel.send('Sergi la chupa bast! 🎈🎉')
            elif message.content == 'raise-exception':
                raise discord.DiscordException

        @self.client.event
        async def on_error(event, *args, **kwargs):
            with open('err.log', 'a') as f:
                if event == 'on_message':
                    f.write(f'Unhandled message: {args[0]}\n')
                else:
                    raise


paarthunax = Paarthunax(TOKEN, GUILD)
paarthunax.start()
