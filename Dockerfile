FROM python:3.11.3-alpine as first_build

ENV APP_PATH=/app

WORKDIR $APP_PATH
COPY . .

RUN apk update && apk add python3 py3-pip && ln -sf python3 /usr/bin/python && \
    pip3 install --no-cache --upgrade pip

RUN pip install wheel poetry && \
    poetry lock && \
    poetry export --without-hashes -f requirements.txt -o requirements.txt && \
    rm poetry.lock

FROM python:3.11.3-alpine

ENV APP_PATH=/app
WORKDIR $APP_PATH
ENV APP_USER=IRango

COPY --from=first_build /app $APP_PATH

RUN adduser $APP_USER -D && \
    chown -R $APP_USER:$APP_USER $APP_PATH

RUN apk add --update --no-cache \
    linux-headers \
    gcc \
    python3 \
    python3-dev  \
    py3-pip\
    && \
    ln -sf python3 /usr/bin/python && \
    pip3 install --no-cache --upgrade pip && \
    chmod 777 $APP_PATH/entrypoint.sh

RUN pip3 install -r $APP_PATH/requirements.txt

ENTRYPOINT $APP_PATH/entrypoint.sh
