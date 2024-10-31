from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = "По условию задания ключ необходимо убрать перед отправкой на GitHub"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler(text=["Calories"])
async def set_age(message):
    await message.answer("Введите свой возраст (лет):")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_weight(message, state):
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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
