FROM python:3

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
RUN pip install discord
COPY . .

CMD [ "python3", "bot_discord_clementB.py" ]
