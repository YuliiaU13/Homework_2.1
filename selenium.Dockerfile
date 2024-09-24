# Використовуємо офіційний образ Python версії 3.9
FROM python:3.11.9-slim

# Копіюємо файли з локальної директорії в контейнер
COPY . /app

# Встановлюємо залежності для Chrome та Selenium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libgbm-dev \
    libxkbcommon0 \
    libxshmfence1 \
    libxrandr2 \
    libxcursor1 \
    libxinerama1 \
    xvfb \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdrm2 \
    libgbm1 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    fonts-liberation \
    libappindicator3-1 \
    libu2f-udev \
    libnss3-tools \
    libxtst6 \
    libxss1 \
    libx11-xcb1 \
    libxcb1 \
    libvulkan1 \
    libdbus-1-3 \
    libxkbcommon-x11-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Google Chrome з .deb
RUN dpkg -i /app/google-chrome-stable_114.0.5735.90-1_amd64.deb \
    && apt-get -f install -y

# ChromeDriver для 114
RUN CHROME_VERSION=114.0.5735 \
    && DRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION) \
    && wget -N https://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm chromedriver_linux64.zip \
    && chmod +x /usr/local/bin/chromedriver



RUN chmod -R 777 /app

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt


# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["pytest", "-m", "nova_poshta or allure_qauto"]
