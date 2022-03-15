from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnTarifs = KeyboardButton("😋тарифы😋")
btnGarantii = KeyboardButton("👀гарантии и пруфы👀")
btnDostyp = KeyboardButton("🚩как получить доступ?🚩")
btnNext = KeyboardButton("😋я оплатил, что дальше?😋")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTarifs, btnGarantii, btnDostyp, btnNext)
