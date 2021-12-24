# DCOM COMMUNICATION SYSTEM

This is a web-based application that aids intra-organizational  communication easier and efficient. The application images are found [here](https://hub.docker.com/repository/docker/otidola101/datacom/) in docker hub

## Implementation

This application is built with different technologies

### Technologies:
- Django Python Framework
- Postgresql Database
- Material Bootstrap CSS
- HTML

## Installations
The application dependencies are bound to the virtual environment so the steps to start up are:

- start the virtual env by running ". virtual/bin/activate"
- Run python manage.py runserver 8000 

## Software Testing
- The file that contains test cases is located in Pawame/intranet/tests.py
- To runs test for some of the application's cases you run python manage.py tests

## Running Docker Images

#### steps

- Run "docker pull otidola101/datacom:web"
- Run  "docker images" to see if the image has downloaded successfully, this will expose the image ID
- To run the image run "docker run -i -t <image-id>"
- Finally to run the web service run "docker-compose up --build" this will expose a routable address to use in the browses.

## Contributors



| Names                | Registration No |
| -------------------- | --------------- |
| DANIEL EVANS KARANI  | SCII/01374/2018 |
| ANTONY ODOYO         | SCII/00839/2019 |
| MARY MBUTU           | SCII/00816/2019 |
| KHADIJAH HASSAN      | SCII/05037P/2020|
| CINDY TALIA          | SCII/00823/2019 |