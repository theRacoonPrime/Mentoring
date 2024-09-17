import config
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import openai

# Инициализация OpenAI API
openai.api_key = config.OPENAI_API_KEY

# Функция обработки сообщений
async def handle_message(update: Update, context):
    user_message = update.message.text
    response = get_openai_response(user_message)
    await update.message.reply_text(response)

# Функция для общения с GPT
def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Используем новую модель
        messages=[{"role": "user", "content": prompt}],  # Формат сообщений для новой модели
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()  # Доступ к содержимому ответа

# Основная функция для запуска бота
def main():
    application = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()

    # Обрабатываем текстовые сообщения
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()




