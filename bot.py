import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = "25026211"
API_HASH = "0f9ed2fdeb8dcbd92c7b86f42472aa2a"
BOT_TOKEN = "6024171147:AAGdTW_zswDHZP3q_rwwggMzI1EF5QC21iA"
SESSION = "BACPVpi01043Tq8svRGrhgwJg5Hn2jHoO2P1od9rXCcq2yRp-rtBqPqgM9DPnJ4yZmAWucO0v4aS1Bo6y6T4atWBMZqIcFXTRpoufsNje5HmTQvY2cnRrhNrb6SQo_7zgemAIvzJ0ZB3VycEl24lMuRS28qo1JSqaEejjmKU7x153jTjbPokCgoWnpJDQt2exrjfpNngIsDnaFdenyyRKMx1aXG9Y5rbwi6HzYzDgRbaGRvhaje2cyy0TCYuPSjUwk9H5Nz7ZSuvsNsYCet17mHEr5UfXtg27N2lXbHbiwhFM9vsClDYMT2GvLB4BzSMvuq01TL9YCpZx-sMiec6fM0nAAAAAWqwQggA"
TIME = 60
GROUPS = [-1001942857176]
for grp in GROUPS:
    GROUPS.append(int(grp))
ADMINS = [6084903432]
for usr in ADMINS
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>"


User = Client(session_name=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(session_name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.message_id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
