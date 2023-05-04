class MessagesRouter:
    def __init__(self, message):
        self.message = message

    async def use(self, endpoint, function):
        if endpoint in self.message.content.lower():
            await function(self.message)
