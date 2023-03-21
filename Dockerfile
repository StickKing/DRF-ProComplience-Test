FROM python:3
# Определяем значения переменных среды
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Указываю рабочую директорию
WORKDIR /code
# Копируем файл зависимостей к контейнер
COPY requirements.txt /code/
# Устанавливаем необходимые библиотеки
RUN pip install -r requirements.txt
COPY . /code/
