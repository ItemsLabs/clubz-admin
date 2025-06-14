FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . /app/
EXPOSE 10000
RUN chmod +x /app/deploy/docker/start.sh
ENTRYPOINT ["/app/deploy/docker/start.sh"]
# ENTRYPOINT ["/bin/bash"]
