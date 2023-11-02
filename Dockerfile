FROM python:3.11
#set enviroment variables
ENV PYTHONDONYWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r/tmp/requirements.txt
COPY . /srv/app
WORKDIR /srv/app
CMD ["python","manage.py","runserver","0.0.0.0:8000"]

