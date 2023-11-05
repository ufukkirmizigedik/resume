FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /app
WORKDIR /app
ENV VIRTUAL_ENV /opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
