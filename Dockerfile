FROM python:3.10-slim

COPY . .

RUN chmod +x entrypoint.sh

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
