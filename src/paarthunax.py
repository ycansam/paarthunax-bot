import discord
from .events.messages import MessagesController
from .events.errors import ErrorsController
from .events.ready import OnReady
la_chupa = " la chupa"
play_video = "$play video"
adios = "$adios"

class Paarthunax:
    def __init__(self, TOKEN, GUILD):
        self.TOKEN = TOKEN
        self.GUILD = GUILD
        self.init_paarthunax()
        self.init_controllers()

    def init_paarthunax(self):
        self.intents = discord.Intents.all()
        self.client = discord.Client(intents=self.intents)

    def init_controllers(self):
        self.MessagesController = MessagesController(self.client, discord)
        self.ErrorsController = ErrorsController(discord)
        self.OnReady = OnReady(self.client, discord)

    def start(self):
        self.register_event_handlers()
        self.client.run(self.TOKEN)

    def register_event_handlers(self):
        @self.client.event
        async def on_ready():
            await self.OnReady.count_guild_members(self.GUILD)

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            if la_chupa in message.content.lower():
                await self.MessagesController.sucks(message)

            if play_video in message.content.lower():
                await self.MessagesController.play_video(message)

            if adios in message.content.lower():
                await self.MessagesController.adios(message)

            ErrorsController.message_contains_exeption(content=message.content)

        @self.client.event
        async def on_error(event, *args, **kwargs):
            await self.ErrorsController.on_error(event, args)
