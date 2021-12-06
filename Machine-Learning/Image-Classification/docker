FROM python:2.7.13-jessie

EXPOSE 5000

RUN apt-get install -y git wget
RUN pip install tensorflow flask
RUN git clone --depth=1 https://github.com/tensorflow/models.git
RUN wget http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz
COPY main.py /

CMD ["python", "main.py"]