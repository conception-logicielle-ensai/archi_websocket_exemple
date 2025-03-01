FROM ubuntu:22.04
WORKDIR /app
RUN apt-get update && apt-get install -y python3-pip && ln -s /usr/bin/python3 /usr/bin/python
COPY . .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "main.py"]