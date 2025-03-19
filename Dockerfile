# Базовый образ с Python
FROM python:3.12

# Обновляем pip и устанавливаем poetry
RUN pip install --upgrade pip poetry

# Указываем рабочую директорию
WORKDIR /app

# Копируем только файлы зависимостей (без тестов!)
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && install --no-root

# Контейнер в ожидании команд
CMD ["/bin/bash"]