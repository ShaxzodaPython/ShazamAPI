import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7179265374:AAG7895a_UoqJTyPYUAvkQud3xxjaIW6-hQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Hi!\nI'm Shazam!\nPowered by aiogram.
        /artists
        /albums
        /songs
        /tracks
    """)

@dp.message_handler(commands=['artists'])
async def send_artist(message: types.Message):
    artists = requests.get(f'http://127.0.0.1:8000/artist/')
    for artist in artists.json():
        await message.reply(f"""
            First name: {artist['first_name']}
            Last name: {artist['last_name']}
            """)

@dp.message_handler(commands=['albums'])
async def send_album(message: types.Message):
    albums = requests.get(f'http://127.0.0.1:8000/album/')
    for album in albums.json():
        await message.reply(f"""
            Title: {album['title']}
            Artist: 
                First name: {album['artist']['first_name']}
                Last name: {album['artist']['last_name']}
            
            """)


@dp.message_handler(commands=['tracks'])
async def send_track(message: types.Message):
    tracks = requests.get(f'http://127.0.0.1:8000/track/')
    for track in tracks.json():
        await message.reply(f"""
            Id: {track['id']}
            Name: {track['name']}
            """)

@dp.message_handler(commands=['songs'])
async def send_songs(message: types.Message):
    songs = requests.get(f'http://127.0.0.1:8000/song/')
    for song in songs.json():
        await message.reply(f"""
            Title: {song['title'].title()}
            Image: {song['image']}
            Album: 
                Title: {song['album']['title'].title()}
                Artist: 
                    First name: {song['artist']['first_name']}
                    Last name: {song['artist']['last_name']}
            Track: 
                Id: {song['track']['id']}
                Name: {song['track']['name']}
            Artist: 
                First name: {song['artist']['first_name']}
                Last name: {song['artist']['last_name']}
            """)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)