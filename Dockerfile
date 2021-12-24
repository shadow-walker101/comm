
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# ADD ./init.sql /docker-entrypoint-initdb.d/
# ENTRYPOINT ["docker-entrypoint.sh"]
# EXPOSE 5432
# CMD ["postgres"]