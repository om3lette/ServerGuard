from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineQueryResultsButton, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram import F

from src.buttons.builders import players_markup_builder
from src.buttons.schemas.button_callbacks import PaginationNav
from src.buttons.services.PaginatorFactory import PaginatorExitStatus
from src.handlers import connection_handler
from src.response_messages import QUERY_NOT_ENABLED_ERROR_MESSAGE

buttons_router: Router = Router()

@buttons_router.callback_query(F.data == "skip")
async def handle_navigation(call: CallbackQuery):
    await call.answer()

@buttons_router.callback_query(PaginationNav.filter())
async def handle_navigation(call: CallbackQuery, callback_data: PaginationNav):
    [is_alive, players_query] = await connection_handler.execute(call.message, connection_handler.query_server)
    if not is_alive:
        return
    if players_query is None:
        await call.message.reply(QUERY_NOT_ENABLED_ERROR_MESSAGE, parse_mode=ParseMode.MARKDOWN_V2)
        return
    new_markup, exit_status = players_markup_builder.build(players_query.players.names, callback_data.page)
    if exit_status == PaginatorExitStatus.ALREADY_UP_TO_DATE:
        await call.answer()
        return
    await call.message.edit_reply_markup(reply_markup=new_markup)
