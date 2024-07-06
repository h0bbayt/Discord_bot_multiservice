import discord
import threading
import asyncio

botToken = ""


class MainBotService(discord.Bot):
    debug = False

    def __init__(self, token, *args, **options):
        super().__init__(*args, **options)
        asyncio.run(self.start(token))


    async def on_connect(self):
        (await self.fetch_channel())



if __name__ == "__main__":
    pass
