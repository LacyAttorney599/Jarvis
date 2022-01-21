FROM python:3.8

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
RUN pip install discord.py
# RUN pip install command
COPY . .

CMD [ "python3", "jarvis.py" ]
