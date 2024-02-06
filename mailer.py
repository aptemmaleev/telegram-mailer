import asyncio
import aiogram

from aiogram import Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder

### TOKEN ###
BOT_TOKEN = "TOKEN"
### SPEED ###
MSG_PER_SECOND = 10
### MESSAGE ###
MSG = """
<b>Бобры 🦫 — трудолюбивые строители и удивительные создания! 🛠👷</b>

Хотите узнать больше об их плотинах, домиках и роли в природе? 🤔

<i>Загляните в чат-бот 💬 @ai_studgpt_bot и откройте для себя мир бобров! 🦫🌍</i>

#бобры #животные #природа
"""
### KEYBOARD MARKUP ###
kb = InlineKeyboardBuilder()
kb.button(text="Открыть чат", url="https://t.me/ai_studgpt_bot")
MARKUP = kb.as_markup()
### BOT ###
BOT = Bot(BOT_TOKEN, parse_mode="HTML")

good = 0
bad = 0
async def send_message(id):
    global good, bad, BOT, MSG, MARKUP
    try:
        await BOT.send_message(id, MSG, reply_markup=MARKUP)
        good += 1
        with open("good.txt", "a") as f:
            f.write(f"{id}\n")
    except Exception as e:
        bad += 1
        with open("bad.txt", "a") as f:
            f.write(f"{id}\n")

async def main():
    global good, bad, BOT, MSG, MARKUP

    # Clear files
    with open("good.txt", "w") as f:
        pass
    with open("bad.txt", "w") as f:
        pass

    # Loading IDS
    print("Loading IDs...")
    with open("ids.txt") as f:
        ids = [int(line.strip()) for line in f]
    print(f"Loaded {len(ids)} IDs!")

    # Sending messages
    print("Sending messages...")
    loop = asyncio.get_running_loop()
    i = 0
    for id in ids:
        i += 1
        loop.create_task(send_message(id))
        await asyncio.sleep(1 / MSG_PER_SECOND)
        if (i % 100 == 0):
            print(f"Sent {i}/{len(ids)} messages. Total good: {good}, Total bad: {bad}")
    await asyncio.sleep(1)
    print(f"Sent {i} messages. Good: {good}, Bad: {bad}")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.create_task(main())
    loop.run_forever()