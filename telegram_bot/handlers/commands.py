from aiogram import Router,F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message,CallbackQuery,FSInputFile
import handlers.keyboards as KB
from database.request import * 

router = Router()

@router.message(CommandStart())
async def start(message:Message):
    await message.answer("Hello I`m bot ceo helper",reply_markup=KB.kb)

@router.message(Command(commands=['help']))
async def help(message:Message):
    await message.answer("For help call 911")


@router.message(F.text == 'Departments')
async def departments(message:Message):
    await message.answer("Choice department",reply_markup= await KB.departments_kb())


@router.message(F.text == 'rab')
async def workers(message:Message):
    await message.answer("Choice Worker",reply_markup= await KB.workers_kb())




@router.callback_query(F.data.startswith('department_'))
async def department(callback:CallbackQuery):
    await callback.message.delete()
    department_id = callback.data.split('_')[1]
    await callback.message.answer(
        "Люди работающие в этом отделе:", 
        reply_markup= await KB.rab_kb(department_id)
        )
    

@router.callback_query(F.data == 'back_1')
async def back_1(callback:CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Выберите депатамент", reply_markup= await KB.departments_kb())

 
@router.callback_query(F.data.startswith('rab_'))
async def rab(callback:CallbackQuery):
    await callback.message.delete()
    rab_id = callback.data.split('_')[1]
    rab = await get_rab(rab_id)
    await callback.message.answer(
        f"""
        Информация о работнике:\n
        Имя и фамилие{rab.first_name} {rab.last_name}\n
        Возраст: {rab.age}\n
        Почта: {rab.email}\n
        ЗП: {rab.salary}\n
        Номер: {rab.phone}\n
        адресс: {rab.address}\n
        """.strip()
        )

@router.callback_query(F.data == 'back_2')
async def back_2(callback:CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Выберите rab", reply_markup= await KB.rab_kb())
    

# from handlers.keyboards import create_paginator

# @router.message(Text(equals="/kb_additional_buttons"))
# async def kb_additional_buttons(message: Message):
#     paginator = create_paginator()

#     await message.answer(
#         text="Keyboard pagination with additional buttons",
#         reply_markup=paginator.as_markup(),
#     )

@router.callback_query(KB.Pagination.filter(F.action_(['next','prev'])))
async def pagination(callback:CallbackQuery,callback_data:KB.Pagination):
    page_number = int(callback_data.page)

    result = await get_worker()
    if callback_data.action == 'next':
        if page_number < len(result) - 1:
            page_number += 1
        else:
            page = page_number 
            await callback.message.answer(f'Last page')

    elif callback_data.action == 'prev':
        if page_number > 0:
            page_number -= 1
        else:
            page = 0
            await callback.message.answer(F'First page')

