# syntax=docker/dockerfile:1
FROM python:3.12-slim as builder

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --upgrade pip && pip install --user -r requirements.txt

FROM python:3.12-slim as runtime

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "smrcwebpage.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
