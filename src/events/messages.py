from .errors import ErrorsController

class MessagesController:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if 'hola' in message.content.lower():
            await message.channel.send('hola 🎈🎉')
            return

        ErrorsController.message_contains_exeption(content=message.content)
