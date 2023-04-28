FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /TPFWhitelistbot/Whitelist-doc/app/static
ENV DATABASE_USERNAME=root
ENV DATABASE_PASSWORD=TODO
ENV DATABASE_HOST=TODO
ENV DATABASE_NAME=tpf_bot
COPY ./requirements.txt /TPFWhitelistbot/Whitelist-doc/requirements.txt
RUN pip install -r /TPFWhitelistbot/Whitelist-doc/requirements.txt