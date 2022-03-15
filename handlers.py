from asyncio import sleep

from main import bot, dp

from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
# from config import admin_id

import marks


# link_danat = "https://www.donationalerts.com/r/my_brain_is_broken"


@dp.message_handler(content_types=["text", "sticker", "pinned_message", "photo", "animation", "audio", "video"])
async def echo(message: Message):

    if message.text == '/start':
        await bot.send_photo(chat_id=message.chat.id, caption='''Привет!
Я бот-автоответчик 🤖 

Если хочешь что-то узнать, просто тыкай на кнопки:''', photo="https://vk.com/photo-90329167_457292068?access_key=a668225288a7512a49", reply_markup=marks.mainMenu)

    elif message.text == '😋тарифы😋':
        await message.answer( text='''👧Тариф «Школьницы»
Что сюда входит?
Сливы школьниц (от 13-и лет), их домашние фото, видео соло и с партнерами, сливы переписок, адреса страниц ВК и Инстаграм
Сколько стоит?
350 RUB

💦Тариф «Вписки»
Что сюда входит?
Сливы со вписок, фото и видео горячих девочек, у которых на уме сами знаете что)
Сколько стоит?
250 RUB

😲Тариф «Всё вместе»
Что сюда входит?
Тариф «Школьницы» и тариф «Вписки»
Сколько стоит?
500 RUB (экономите 100 RUB😉)''',

            reply_markup=marks.mainMenu)

    elif message.text == '👀гарантии и пруфы👀':
        await message.answer(text='''Замените запятую на точку:''', reply_markup=marks.mainMenu)
        await message.answer(text='''https://telegra,ph/-03-11-2005''', reply_markup=marks.mainMenu)

    elif message.text == '🚩как получить доступ?🚩':
        await message.answer(text=f'''Чтобы получить доступ к приватке, оплатите её с помощью киви или карты.

⚠️Не оставляйте никаких комментариев к платежу, иначе он не засчитается!

Реквизиты банковской карты: {"5599 0020 1224 5819"}
Ссылка для QIWI: {"http://qiwi.com/p/79207767676"}

❗️После этого выберите пункт с подтверждением оплаты (чтобы нам пришло уведомление) и следуйте инструкции.''', reply_markup=marks.mainMenu)
    elif message.content_type == 'photo':
        await bot.send_message(chat_id=message.chat.id, text="Ожидайте мы проверим ваше сообщение и ответим в ближайшее время, слишком много заявок👀")

    elif message.text == '😋я оплатил, что дальше?😋':
        await message.answer(text='''Огромное спасибо, что помогаете нам разиваться!

Чтобы получить доступ к каналу(ам), отправьте сюда скриншот/чек оплаты и время по МСК, когда был совершен перевод.

Мы получим уведомление, проверим оплату (в среднем это занимает около 30 минут) и в этом диалоге отправим вам ссылку(и).''', reply_markup=marks.mainMenu)

    # else:
    #     await message.answer(text="", reply_markup=marks.mainMenu)


