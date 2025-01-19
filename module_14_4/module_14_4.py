from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
import asyncio
import crud_functions

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
keyboard.add(button_calculate, button_info, button_buy)

inline_keyboard = InlineKeyboardMarkup(row_width=2)
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

buying_keyboard = InlineKeyboardMarkup(row_width=2)
button_product1 = InlineKeyboardButton('Видеокарта', callback_data='product_buying')
button_product2 = InlineKeyboardButton('Процессор', callback_data='product_buying')
button_product3 = InlineKeyboardButton('Оперативная память', callback_data='product_buying')
button_product4 = InlineKeyboardButton('Материнская плата', callback_data='product_buying')
buying_keyboard.add(button_product1, button_product2, button_product3, button_product4)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью.\n'
        'Выберите действие на клавиатуре ниже:',
        reply_markup=keyboard
    )

@dp.message_handler(Text(equals="Рассчитать", ignore_case=True))
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

@dp.callback_query_handler(Text(equals='formulas'))
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('10 × вес (кг) + 6.25 × рост (см) – 5 × возраст (г) + 5 (мужчины) / -161 (женщины)')

@dp.callback_query_handler(Text(equals='calories'))
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    age = data['age']
    growth = data['growth']
    weight = data['weight']
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий {calories:.2f}')
    await state.finish()

@dp.message_handler(text='Информация')
async def info(message: types.Message):
    await message.answer('Я могу помочь рассчитать вашу норму калорий. Нажмите "Рассчитать", чтобы начать.')

@dp.message_handler(Text(equals="Купить", ignore_case=True))
async def get_buying_list(message: types.Message):
    products = crud_functions.get_all_products()
    image_paths = {
        'Видеокарта': 'images/img1.png',
        'Процессор': 'images/img2.png',
        'Оперативная память': 'images/img3.png',
        'Материнская плата': 'images/img4.png'
    }
    for product in products:
        try:
            image_path = image_paths.get(product[1], None)
            if image_path:
                with open(image_path, 'rb') as photo:
                    await message.answer_photo(
                        photo,
                        caption=f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}'
                    )
            else:
                await message.answer_photo(
                    product[4],
                    caption=f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}'
                )
        except Exception as e:
            print(f"Ошибка при отправке изображения: {e}")
            await message.answer(
                f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}\n'
                f'Изображение недоступно.'
            )
    await message.answer('Выберите продукт для покупки:', reply_markup=buying_keyboard)

@dp.callback_query_handler(Text(equals='product_buying'))
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    crud_functions.initiate_db()
    crud_functions.add_product('Видеокарта', 'NVIDIA Geforce RTX 5090', 2000, 'https://cdn-icons-png.flaticon.com/512/2004/2004611.png')
    crud_functions.add_product('Процессор', 'Ryzen 7 9800x3d', 500, 'https://cdn-icons-png.flaticon.com/512/3716/3716484.png')
    crud_functions.add_product('Оперативная память', 'ADATA XPG Lancer Blade 32gb 6000 MHZ (2x16)', 100, 'https://cdn-icons-png.flaticon.com/512/2764/2764252.png')
    crud_functions.add_product('Материнская плата', 'ASUS TUF B650-Plus', 250, 'https://cdn-icons-png.flaticon.com/512/2287/2287895.png')
    executor.start_polling(dp, skip_updates=True)
