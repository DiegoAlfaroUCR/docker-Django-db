# Version de python a usar
FROM python:3.11.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

COPY . /app

EXPOSE 8000

ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]