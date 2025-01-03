PING_SUCCESS_MESSAGE: str = "Статус сервера: ✅\nЗадержка: {latency}мс ⌛"
PING_ERROR_MESSAGE: str = "Попытка №{attempt_number} ❌\nПовтор через {time_before_retry} секунд ⌛"
PING_HANGUP_MESSAGE: str = "Статус сервера: 😵\nВызываю админов:\n{admins}"
PING_HANGUP_ADMIN_MESSAGE: str = "Статус сервера: 😵 ️\nТребуется ручная проверка 🔧\nСервер: {server_address} 🖥️"

PLAYERS_NUMBER_MESSAGE: str = "Игроков на сервере: {current_number}/{capacity}📶"
PLAYERS_ONLINE_MESSAGE: str = "Игроки на сервере 🎮:\n{players}"

QUERY_NOT_ENABLED_ERROR_MESSAGE: str = "Неудалось выполнить запрос 😞\nНеобходимо включить 'query' в файле server.properties сервера!"
NO_PLAYERS_ONLINE_MESSAGE: str = "Тут никого нет 😭"
NO_ADMINS_FOUND_MESSAGE: str = "Админы для сервера не указаны 😢"
