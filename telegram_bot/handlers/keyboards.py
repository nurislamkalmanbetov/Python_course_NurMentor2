from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from database.request import * 
from database.models import *

from aiogram.filters.callback_data import CallbackData



kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Departments')],
    [KeyboardButton(text='rab')]],
    resize_keyboard=True,input_field_placeholder='Выберите действие', one_time_keyboard=True)

async def departments_kb():
    departments = await get_departments()
    kb = InlineKeyboardBuilder()
    for depp in departments:
        kb.add(InlineKeyboardButton(text = depp.name,
            callback_data=f'department_{depp.id}'))
    return kb.adjust(2).as_markup()


async def workers_kb():
    workers= await get_worker()
    kb = InlineKeyboardBuilder()
    for worker in workers:
        kb.add(InlineKeyboardButton(text = f'{worker.first_name} {worker.last_name}',
            callback_data=f'rab_{worker.id}'))
        
    kb.add(InlineKeyboardButton(text='назад', callback_data='back_2')) # Кнопка Назад 

    return kb.adjust(2).as_markup()



# async def rab_kb(department_id):
#     rab = await get_rabs(department_id)
#     kb = InlineKeyboardBuilder()
#     for rabs in rab:
#         kb.add(InlineKeyboardButton(text = f'{rabs.first_name} {rabs.last_name}',
#             callback_data=f'rab_{rabs.id}'))
        
#     kb.add(InlineKeyboardButton(text='назад', callback_data='back_1')) # Кнопка Назад 

#     return kb.adjust(2).as_markup() # adjust(2) - кнопки выходят по 2

async def rab_kb(department_id, rab_id_to_delete=None):
    if rab_id_to_delete:
        await get_rab2(rab_id_to_delete)

    rab = await get_rabs(department_id)
    kb = InlineKeyboardBuilder()
    
    for rabs in rab:
        kb.add(InlineKeyboardButton(text=f'{rabs.first_name} {rabs.last_name}', callback_data=f'rab_{rabs.id}'))
        
    kb.add(InlineKeyboardButton(text='назад', callback_data='back_1'))  # Кнопка Назад 
    return kb.adjust(2).as_markup()  # adjust(2) - кнопки выходят по 2


# class Pagination(CallbackData, prefix="pagination"):
#     page: int
#     action: str
    
#     def paginator(page: int = 0):
#         pg_builder = InlineKeyboardBuilder()
#         pg_builder.row(InlineKeyboardButton(text='◀️',
#         callback_data=Pagination(page=page, action='prev').pack()),
#                        InlineKeyboardButton(text='▶️',
#         callback_data=Pagination(page=page, action='next').pack()),
#         width=2)

#         return pg_builder.as_markup() # as_markup - будет как кнопка
    
# from aiogram_widgets.pagination import KeyboardPaginator
# from aiogram.types import InlineKeyboardButton

# def create_paginator():
#     buttons = [
#         InlineKeyboardButton(text=f"Button {i}", callback_data=f"button_{i}")
#         for i in range(1, 1001)
#     ]
#     additional_buttons = [
#         [
#             InlineKeyboardButton(text="Go back 🔙", callback_data="go_back"),
#         ]
#     ]

#     paginator = KeyboardPaginator(
#         data=buttons,
#         additional_buttons=additional_buttons,    
#         per_page=20, 
#         per_row=2
#     )

#     return paginator
