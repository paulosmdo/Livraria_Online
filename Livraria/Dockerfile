FROM python:3.12.11-trixie
LABEL mantainer="paulosmdo"

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
		netcat-openbsd \
	&& rm -rf /var/lib/apt/lists/*


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

RUN sed -i 's/\r$//' run_server.sh && chmod +x run_server.sh

EXPOSE 8000

CMD ["./run_server.sh"]
#CMD ["tail", "-f", "/dev/null"]

# CMD ["run_server.sh"]
