#!/usr/bin/python
"""
    discord_bot.py was created by Naum Raskind on February 25, 2023
"""
import os
import discord
from dotenv import load_dotenv


class FamJamClient(discord.Client):
    """Represents Fam Jammer bot

    1. The permissions for fam jammer are configured in the developer portal: https://discord.com/developers/applications/1079108221018574958/bot
    2. To expand the class and listen to more events:
        - add event listeners in FAM_JAM_INTENTS: https://discordpy.readthedocs.io/en/stable/api.html#intents
        - override existing event handlers in discord.Client: https://discordpy.readthedocs.io/en/stable/api.html#discord.Client
    3. To add emojis, find them here and copy paste: https://emojipedia.org/
    """
    #: These are the events that discord will send the bot. At the moment this only includes messages sent within the server
    FAM_JAM_INTENTS = discord.Intents(guild_messages=True)
    #: Discord uses "guild" and "server" interchangeably. Guild name is the name of the server
    FAM_JAM_GUILD_NAME = "Fam Jam"

    def __init__(self) -> None:
        """Construct a Fam Jam bot and set its token"""
        super().__init__(intents=self.FAM_JAM_INTENTS)
        self.token = self.get_token()

    async def on_ready(self) -> None:
        """Log that the bot has connected to the fam jam server"""
        print(f'{self.user} has connected to Discord')

    async def on_message(self, message: discord.Message) -> None:
        """React with the 🔥 emoji on all of Naums messages"""
        if message.author.name == "Naum.Raskind":
            await message.add_reaction("🔥")

    def run(self) -> None:
        """Start the bot and begin listening for messages"""
        super().run(self.token)

    def get_token(self) -> str:
        """Retrieve the bot token from the .env file

        The bot token can not be viewed after it is generated. If the bot token is lost then you will need
        to go to https://discord.com/developers/applications/1079108221018574958/bot and regenerate it.
        """
        load_dotenv()
        return os.getenv('DISCORD_TOKEN')


def main():
    """Create famjammer and begin listening to messages"""
    famjammer = FamJamClient()
    famjammer.run()


if __name__ == "__main__":
    main()
