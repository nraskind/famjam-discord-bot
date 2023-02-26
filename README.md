# Fam Jam Discord Bot
## Background
Implemented a discord bot for my familys Fam Jam discord server. To begin, I followed the steps outlined in this tutorial: [[How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python/)]. It don't do much but it's lernin

## Running the bot locally

### 1. Install dependencies
- Install python
    - This project was created using python version 3.10.10
- Install pip
    - This project was created using pip version 23.0.1
- Install python modules using `requirements.txt`
    ```bash
    $ pwd
    /.../famjam-discord-bot/ # Project root
    $ pip install -r requirements.txt
    ```
### 2. Add the bot token
Create a .env file and add the discord token
```bash
$ pwd
/.../famjam-discord-bot/ # Project root
$ echo "DISCORD_TOKEN=<FIXME_GET_FROM_NAUM>" >> .env
```
Replace the placeholder `DISCORD_TOKEN=<FIXME_GET_FROM_NAUM>` in `.env` with the correct token

### 3. Start the bot
Execute `discord_bot.py` to start the bot
```bash
$ pwd
/.../famjam-discord-bot/ # Project root
$ python discord_bot.py
...
Fam Jammer#8602 has connected to Discord
```