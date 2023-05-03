class ErrorsController:
    def __init__(self, library):
        self.library = library

    async def on_error(self, event, args):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise

    def message_contains_exeption(self, content):
        if content == 'raise-exception':
            raise self.library.DiscordException
