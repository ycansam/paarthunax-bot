import os
from dotenv import load_dotenv
from src.paarthunax import Paarthunax

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

def main():
    paarthunax = Paarthunax(TOKEN, GUILD)
    paarthunax.start()

if __name__ == '__main__':
    main()