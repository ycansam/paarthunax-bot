from .errors import ErrorsController
from ..utils.message_utils import MessageUtils


class MessagesController:
    def __init__(self, client, library):
        self.client = client
        self.library = library

    async def sucks(self, message):
        print('sucking')
        name = MessageUtils.separate_name_from_message_with_post_cond(
            message=message.content, cond="chupa")
        await message.channel.send(name + ' la chupa bastisim 🎈🎉')

    async def play_video(self, message):
        print('playing video')
        voice_client = message.author.voice.channel
        
        source = self.library.FFmpegPCMAudio('./hola.mp4')
        voice_client.play(source)

    async def adios(self, message):
        print('adios')
        await message.channel.send('adios')

