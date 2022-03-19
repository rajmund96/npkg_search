FROM python:3.9

ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /requirements.txt
WORKDIR /app
RUN pip install -r /requirements.txt

# Copy the application files into the image
COPY . /app/

# Expose port 8000 on the container
EXPOSE 8000
