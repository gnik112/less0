from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = "По условию задания ключ необходимо убрать перед отправкой на GitHub"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ]
    ], resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет!", reply_markup=kb)


@dp.message_handler(text=["Рассчитать"])
async def set_age(message):
    await message.answer("Введите свой возраст (лет):")
    await UserState.age.set()


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
        cl_man = '%.2f' % ((10 * weight) + (6.25 * growth) + (5 * age) + 5)
        cl_woman = '%.2f' % ((10 * weight) + (6.25 * growth) + (5 * age) - 161)
        mess = f"Норма калорий для мужчин: {cl_man}, для женщин: {cl_woman}"
        await message.answer(mess)
        await state.finish()
    else:
        await message.answer("Вес должен быть целым, положительным числом:")
        await UserState.weight.set()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
