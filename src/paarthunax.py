import discord
from .events.messages import MessagesController
from .events.errors import ErrorsController
from .events.ready import OnReady
from .router.messages_router import MessagesRouter
la_chupa = " la chupa"
play_video = "$play video"
adios = "$adios"

adios = "adios"


hola = "hola"

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
            messages_router = MessagesRouter(message)
            if message.author == self.client.user:
                return
            
            await messages_router.use(la_chupa, self.MessagesController.sucks)
            await messages_router.use(play_video, self.MessagesController.play_video)
            await messages_router.use(hola, self.MessagesController.hola)
            await messages_router.use(adios, self.MessagesController.adios)

            self.ErrorsController.message_contains_exeption(content=message.content)

        @self.client.event
        async def on_error(event, *args, **kwargs):
            await self.ErrorsController.on_error(event, args)
