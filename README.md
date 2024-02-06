# Telegram Mailer

### Установка
```sh
git clone https://github.com/bloggery/telegram-mailer
cd telegram-mailer
pip install -r requirements.txt
```

### Настройка
В файл `ids.txt` поместить идентификаторы юзеров телеге (каждый на новой строке).

Сообщение для рассылки настраивается в mailer.py (в т.ч. можно добавить кнопки под сообщением):
```py
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
```

### Запуск рассылки
```sh
python mailer.py
```
