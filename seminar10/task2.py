import logging
import os
from fractions import Fraction

from dotenv import load_dotenv
from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

logger = logging.getLogger(__name__)

(
    SECOND_NUMBER,
    OPERATOR,
    HANDLE_ANSWER,
    BEGIN_AGAIN,
) = range(4)


def isComplex(value):
    return (
        isinstance(complex(value), complex) 
        and (complex(value).imag != 0)
    )


def isRational(value):
    return (
        len(value.split("/")) == 2
    )


def calculate(
    first_number,
    second_number,
    operator,
    number_type
    ):
    operator_function = {
        "-": lambda x, y: x - y,
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    operation = operator_function[operator]
    if number_type == 1:
        return operation(
            complex(first_number),
            complex(second_number)
        )
    first_number_parts = first_number.split("/")
    second_number_parts = second_number.split("/")
    return operation(
        Fraction(int(first_number_parts[0]), int(first_number_parts[1])),
        Fraction(int(second_number_parts[0]), int(second_number_parts[1]))
    )


def start(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Калькулятор комплексных и рациональных чисел\nВведите первое число",
    )

    return SECOND_NUMBER


def handle_second_number(update, context):
    context.user_data["first_number"] = update.message.text
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Введите второе число",
    )

    return OPERATOR


def handle_operator(update, context):
    context.user_data["second_number"] = update.message.text
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Введите действие (+, -, *, /)",
    )

    return HANDLE_ANSWER


def handle_answer(update, context):
    first_number = context.user_data["first_number"]
    second_number = context.user_data["second_number"]
    
    if isComplex(first_number) and isComplex(second_number):
        message_text = str(calculate(
            first_number,
            second_number,
            update.message.text,
            1
        ))
    elif isRational(first_number) and isRational(second_number):
        message_text = str(calculate(
            first_number,
            second_number,
            update.message.text,
            2
        ))
    else:
        message_text = "Введены не комплексные или не рациональные числа"
    
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=message_text,
    )

    return BEGIN_AGAIN


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    load_dotenv()

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    telegram_token = os.getenv("TELEGRAM_TOKEN")
    
    updater = Updater(telegram_token)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SECOND_NUMBER: [
                MessageHandler(Filters.text, handle_second_number),
            ],
            OPERATOR: [
                MessageHandler(Filters.text, handle_operator),
            ],
            HANDLE_ANSWER: [
                MessageHandler(Filters.text, handle_answer),
            ],
            BEGIN_AGAIN: [
                MessageHandler(Filters.text, start),
            ],
        },
        fallbacks=[CommandHandler("exit", exit)],
    )

    dp.add_handler(conv_handler)
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
