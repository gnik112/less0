from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

api = "По условию задания ключ необходимо убрать перед отправкой на GitHub"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
all_products = get_all_products()

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True
)

kb_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
)

kb_inline2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Питание1', callback_data='product_buying'),
            InlineKeyboardButton(text='Питание2', callback_data='product_buying'),
            InlineKeyboardButton(text='Питание3', callback_data='product_buying'),
            InlineKeyboardButton(text='Питание4', callback_data='product_buying'),
        ]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет!", reply_markup=kb)


@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb_inline)


async def out_product(message, product):
    await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
    with open(f'files/0{product[0]}.webp', "rb") as pic:
        await message.answer_photo(pic)


@dp.message_handler(text=["Купить"])
async def get_buying_list(message):
    for i in all_products:
        await out_product(message, i)
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_inline2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст (лет):")
    await UserState.age.set()
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    mess = 'для мужчин: 10 х вес(кг) + 6.25 х рост(см) - 5 х возраст(г) + 5\n'
    mess += 'для женщин: 10 х вес(кг) + 6.25 х рост(см) - 5 х возраст(г) - 161'
    await call.message.answer(mess)
    await call.answer()


# Проверка, что число целое и положительное
def check_data(text):
    dt_int = 0
    if text.isdigit():
        dt_int = int(text)
    if dt_int > 0:
        return True
    return False


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if check_data(message.text):
        await state.update_data(age=message.text)
        await message.answer("Введите свой рост (см):")
        await UserState.growth.set()
    else:
        await message.answer("Возраст должен быть целым, положительным числом:")
        await UserState.age.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if check_data(message.text):
        await state.update_data(growth=message.text)
        await message.answer("Введите свой вес (кг):")
        await UserState.weight.set()
    else:
        await message.answer("Рост должен быть целым, положительным числом:")
        await UserState.growth.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if check_data(message.text):
        await state.update_data(weight=message.text)
        data = await state.get_data()
        weight = float(data['weight'])
        growth = float(data['growth'])
        age = float(data['age'])
        cl_man = '%.2f' % ((10 * weight) + (6.25 * growth) - (5 * age) + 5)
        cl_woman = '%.2f' % ((10 * weight) + (6.25 * growth) - (5 * age) - 161)
        mess = f"Норма калорий для мужчин: {cl_man}, для женщин: {cl_woman}"
        await message.answer(mess)
        await state.finish()
    else:
        await message.answer("Вес должен быть целым, положительным числом:")
        await UserState.weight.set()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
