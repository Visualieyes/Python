Part 1: Introduction
This lab will provide you with the fundamentals of building a image classification service using TensorFlow.

Objectives
Learn more about these technologies:

{TensorFlow
Python Flask
Docker
Postman}


TensorFlow:
TensorFlow is an open source software library for high performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices. Originally developed by researchers and engineers from the Google Brain team within Google’s AI organization, it comes with strong support for machine learning and deep learning and the flexible numerical computation core is used across many other scientific domains.

Docker for Developers:
Docker unlocks the potential of your organization by giving developers and IT the freedom to build, manage and secure business-critical applications without the fear of technology or infrastructure lock-in.

Python Flask framework:
Flask is a microframework for Python to build RESTful micro-service. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

Postman:
Postman is a powerful HTTP client for testing web services.




Part 2: Building a image classification microservice with Tensorflow
In this section, you will learn how to build a microservice using Python flask framework and TensorFlow.



Part 3: Dockerize your service
Dockerize your new micro service.


Prerequisite
- docker


Build docker image
< docker build . -t tfimg >




Part 4: Test your sevice
In this section, you will test your new TensorFlow based image classification service.

Prerequisite
- postman

Start micro service in a docker container
< docker run -d --rm -p 5000:5000 tfimg >

^ This will start a micro service on port 5000, your image classification service is ready now!



Send request
Create a POST request in postman, url set to http://0.0.0.0:5000/images
Specify form-data type in Body
Add a file key, choose an image file from you laptop
Click the Send button