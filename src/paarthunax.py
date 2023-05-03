import discord
from .events.messages import MessagesController
from .events.errors import ErrorsController


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
        self.MessagesController = MessagesController(self.client)
        self.ErrorsController = ErrorsController(library=discord)

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
            await self.MessagesController.on_message(message=message)

        @self.client.event
        async def on_error(event, *args, **kwargs):
            await self.ErrorsController.on_error(event, args)
