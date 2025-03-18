# Используем Python 3.11
FROM python:3.12

# Указываем рабочую директорию
WORKDIR /app

# Копируем весь код проекта
COPY . /app

# Обновляем pip и устанавливаем poetry
RUN pip install --upgrade pip poetry

# Устанавливаем зависимости
RUN poetry install --no-root

# Запускаем тесты при старте контейнера
CMD ["poetry", "--browser=chrome"]