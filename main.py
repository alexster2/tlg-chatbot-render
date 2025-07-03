import telebot
from openai import OpenAI

# 🔐 Ключи
BOT_TOKEN = "7466104380:AAGQLUWKMn8u5bKj2nXbLitVIWl2b6SNcaI"
OPENAI_API_KEY = "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"

# Клиент OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_text = message.text
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты инженер по сборке НКУ. Отвечай строго по делу, с ГОСТами."},
                {"role": "user", "content": user_text}
            ]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Ошибка: {e}"

    bot.send_message(message.chat.id, reply)

print("Бот работает!")
bot.polling()
