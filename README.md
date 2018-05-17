# Infinity-3.1
Code for remotely controlling Rover using Joystick.

This project is based on the Martian rover curiosity. It takes the help of rocker-bogie mechanism  to go over large obstacles with stability. A simple circuit controlled by Raspberry Pi is used. The Rover is remotely controlled using Joystick.

A client-server model is implemented to establish wireless communication between the Joystick and raspberry pi. The server code (server_final.py) is implemented on R Pi. Flask, a python framework is used as a back-end framework that handles the server side. On the client side Requests, a python library is used to send HTTP requests to the server. The client side code (client.py) reads data from the joystick and accordingly sends requests to the server to run the Rover.


### Prerequisites
* Python 2.7
* Other requirements are listed in requirements.txt file and can be installed by running the following command: <br>
    `pip install -r requirements.txt`


### Installation
* Fork this project to your GitHub account.
* After forking, clone the repository using the following command: <br>
    `git clone https://github.com/amateur-astronomy-club/Infinity-3.1.git`


### Running <br>
1] Make the required connections <br>
2] Enable SSH on the Raspberry Pi <br>
3] Login to Raspberry Pi. For example with `ssh pi@your_raspberry_pi_ip` <br>
4] Move the server_final.py file on R Pi <br>
5] Connect the joystick to the system <br>
6] Change the ip address given in client.py file with the ip address of your R pi <br>
7] Run the server_final.py file on R Pi using the following command: `python server_final.py` <br>
8] While the server_final.py is running on R Pi, open a new terminal on your system and run the client.py file using the following command: `python client.py`




