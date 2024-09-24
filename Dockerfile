# Используем образ на основе Debian
FROM python:3.12.4-slim-bullseye

# Устанавливаем системные зависимости для Playwright и других инструментов
RUN apt-get update && apt-get install -y openjdk-11-jdk && apt-get install -y --no-install-recommends \
    curl gcc g++ libffi-dev libssl-dev make \
    chromium ca-certificates fonts-liberation libnss3 \
    libatk1.0-0 libatk-bridge2.0-0 libdrm2 libxcomposite1 libxdamage1 \
    libxrandr2 libgbm1 libasound2 libpangocairo-1.0-0 libpango-1.0-0 \
    libcups2 libxkbcommon0 libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Обновляем pip, setuptools и wheel
RUN pip install --upgrade pip setuptools wheel

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости Python (pytest, allure, playwright и другие)
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем браузеры
RUN playwright install

# Устанавливаем Allure
RUN curl -o allure.tgz -L https://github.com/allure-framework/allure2/releases/download/2.20.0/allure-2.20.0.tgz \
    && tar -zxvf allure.tgz -C /opt/ \
    && ln -s /opt/allure-2.20.0/bin/allure /usr/bin/allure

# Копируем код проекта в контейнер
WORKDIR /app

ENV DOCKER_CONTAINER=true


