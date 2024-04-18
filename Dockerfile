FROM --platform=linux/x86_64 python:latest
LABEL authors="roberto.aceves"
#se utiliza para decirle a Python que imprima la salida y los errores de forma inmediata, sin esperar a que se complete un búfer.
ENV PYTHONUNBUFFERED=1
#vamos a trabajar en el siguiente directorio
WORKDIR /app
#copiamos los archivos de mi proyecto al directorio de trabajo
COPY . /app
#instalamos las dependencias
RUN pip install --upgrade pip

COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#RUN python manage.py makemigrations && python manage.py migrate

#docker build -t /*tag*/ .
#docker run -p 8000:8000 /*tag*/