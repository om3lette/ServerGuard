# ServerGuard
## Функционал
- [x] Просмотр статуса сервера (офлайн/онлайн)
- [x] Просмотр количества игроков на сервере
- [x] Просмотр имен игроков на сервере
- [x] Оповещение админов о падении сервера в случае офлайн статуса
## Как запустить
1. Склонировать репозиторий
```bash
git clone https://github.com/om3lette/ServerGuard.git
```
2. Установите зависимости 
```commandline
pip install -r requirements.txt
```
3. Укажите переменные окружения в `Dockerfile` или `.env`
4. Запустите локально
### Python
#### Windows
```
python -m src.main
```
#### Linux
```commandline
python3 -m src.main
```
### Docker
```commandline
sudo docker build -t server-guard .
sudo docker run -d --rm --name server-guard \
-e SERVER_ADDRESS "<YOUR_VALUE>" \
-e BOT_TOKER "<YOUR_TOKEN>" \
-e ADMINS "<OPTIONAL>" \
-e ADMIN_IDS "<OPTIONAL>" \
-e RCON_PASSWORD "<OPTIONAL>"
server-guard
```
Также можно собирать изображение напрямую из репозитория
```
sudo docker build -t server-guard https://github.com/om3lette/ServerGuard.git
```