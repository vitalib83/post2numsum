# Post2numsum

In this project i create an API script that get 2 numbers by POST and return their sum.
In order to return sum i use external CURL command by POST method.
pack this script to docker as well use CI/CD Jenkins tool to build Pipline.

## Stack that used:

    1.Python

    2.Flask

    3.Docker

    4.Git

    5.Jenkins

## Flask

Flask is a web application framework written in Python

## Installation


Download and install [Docker](https://docs.docker.com/desktop/install/windows-install) to run CLI commands

## Usage

   1.Download Dockerfile and main.py file to local machine
 
   2.Run 
   ```bash
docker build -t post-2-sum .
```
   3.We check now image ID
   ```bash
docker images
```
   Example:
   
   ![image](https://user-images.githubusercontent.com/51639685/212790542-221e89cc-c091-43f5-b9c0-1224e3dc063c.png)

   4.Next step we run the Docker
   ```bash
docker run -p 5000:5000 ImageID
```
   5.After docker running
   
   ![image](https://user-images.githubusercontent.com/51639685/212790897-e218af3a-5c6c-43da-b808-e5b115472c92.png)
   
    i. We will send POST request

    
 curl -X POST -H "Content-Type: application/json" -d '{"num1": 8, "num2": 9}' http://127.0.0.1:5000/sum  
```
    ii.and see this -
    
    
{          
  "sum": 17
} 
```

# Summry
  
  In this project i use simple POST method to send json request to API in order to get sum of 2 numbers in next version all docker steps will be built in
  one Python script.
