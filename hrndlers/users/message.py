import html
import random
from aiogram import types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from stetes.stetes import user

async def start_command(message: types.Message, state: FSMContext):
    await message.answer(f'<b>{html.escape(message.from_user.full_name)},</b> привет\n\n'
                         f'Бот загадай чсло от 1 до 10, попробуй угодать')
    await state.set_state(user.namber)
    
async def state_nambers(message: types.Message, state: FSMContext):
    random_message = random.randint(1,10)
    user_message = message.text
    if user_message.isdigit():
        if 10 >= int(user_message) >= 1:
            if int(user_message) == random_message:
                await message.answer('Вы угодали, Миша любит Сашку')
                await state.clear()
            else:
                await message.answer(f'Пробуй еще раз, мое сило {random_message}')  
        else:
            await message.answer('Число не в диапазоне') 
            
    else:
        await message.answer('Введи пожалуйста число') 
    
    
    
def register_user_messages(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
    dp.message.register(state_nambers, user.namber)