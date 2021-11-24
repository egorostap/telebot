import sqlite3

#bot
import telebot

bot = telebot.TeleBot("2116329079:AAFgVBURPKMmEAd-diNNMNi6NE1eYBKnFrs")

@bot.message_handler(commands=['start'])
def start(message):
    # connect db and create table
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
        )""")
    connect.commit()

    # check
    people_id = message.chat.id
    cursor.execute(f"""SELECT id FROM login_id WHERE id = {people_id}""")
    data = cursor.fetchone()
    print(data)
    if data is None:
        # add values
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Такой пользователь уже есть')



@bot.message_handler(commands=['delete'])
def delete(message):

    # connect db
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    # delete id from table
    people_id = message.chat.id
    cursor.execute(f"""DELETE FROM login_id WHERE id = {people_id}""")
    connect.commit()

#polling
bot.polling()