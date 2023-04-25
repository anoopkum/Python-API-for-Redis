FROM python:3.9-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y --no-install-recommends install \
        gcc \
        libffi-dev \
        libpq-dev \
        libssl-dev \
        netcat \
    && rm -rf /var/lib/apt/lists/*

# create a working directory for the application
WORKDIR /app

# copy the requirements file and install dependencies
COPY app/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install python-multipart


# expose port 8000
EXPOSE 8000

# copy the application code
COPY app app

# set the default command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

