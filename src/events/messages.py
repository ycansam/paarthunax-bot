from .errors import ErrorsController
from ..utils.message_utils import MessageUtils
la_chupa = " la chupa"


class MessagesController:
    def __init__(self, client):
        self.client = client

    async def sucks(self, message):

        if la_chupa in message.content.lower():
            name = MessageUtils.separate_name_from_message_with_post_cond(message=message.content, cond="chupa")
            await message.channel.send(name + ' la chupa bast 🎈🎉')
            return

        ErrorsController.message_contains_exeption(content=message.content)
