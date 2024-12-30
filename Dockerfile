FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    netcat-openbsd \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY espera.sh /espera.sh
RUN chmod +x /espera.sh


CMD ["/espera.sh", "db", "3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
