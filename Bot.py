from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='token', parse_mode='html')

faker = Faker()

# Keyboard
card_type_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# First Line
card_type_keyboard.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)
# Second Line
card_type_keyboard.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id, 
        text='Welcome, choose the card you want\nSelect card type:', 
        reply_markup=card_type_keyboard,
    )

@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'
    elif message.text == 'Maestro':
        card_type = 'maestro'
    elif message.text == 'JCB':
        card_type = 'jcb'
    else:
        
        bot.send_message(
            chat_id=message.chat.id,
            text='Please select the card option you want',
        )
        return

    card_number = faker.credit_card_number(card_type)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Your testing card is {card_type}:\n<code>{card_number}</code>'
    )

def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
    
    Auth:@QA-Sam
