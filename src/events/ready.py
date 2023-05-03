class OnReady:
    
    def __init__(self, client, library):
        self.library = library
        self.client = client

    async def count_guild_members(self, guild_name):
        guild = self.library.utils.get(self.client.guilds, name=guild_name)
        members = '\n - '.join([member.name for member in guild.members])
        print(f"Guild Members:\n - {members}")
