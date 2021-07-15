# Hybrid Neural-Regexp Anonymizer of entities
## Neural model
Uses Flair 0.8 to anonymize:
- PER
- DATE
- GPE
- LOC
- TIME

NOTE: These entities have a ~0.9 of both recall and accuracy.

## Regex model
Uses different regular expressions to manage other kind of (Spanish so far) entities, as:
- Phone numbers
- Emails
- NIE/NIF
- Social Id's
- Passports
...
  
NOTE: These entities have a LOW recall, since they are very document dependant. You must need to include new or fine-tune them.
To do that, use `esentities.py` or create another file for another language (`enentities.py`, ...)

## IMAGE BUILD TO UPLOAD TO DOCKER HUB
Just go to ./docker and execute:
`sudo docker-compose build`

This will create an image. 

To upload it to docker hub:

`sudo docker push docker.io/josejuanmartineziqvia/anonymizer:0.1`


## INSTALLATION

## Apertium (for translation)
### From docker hub

# Installation

`sudo docker pull docker.io/josejuanmartineziqvia/apertium`

`sudo docker run -d --name apertium -p "2737:2737" docker.io/josejuanmartineziqvia/apertium`

# Request

`http://{SERVER_IP}:2737/translate?langpair=cat|spa&q=Bon%20dia`

# Response

`{"responseData": {"translatedText": "Buenos días"}, "responseDetails": null, "responseStatus": 200}`

## DOCKER INSTALLATION
### From docker hub

### Install apertium first 

First, install and run Apertium [here](https://hub.docker.com/repository/docker/josejuanmartineziqvia/apertium)

### Install anonymizer

#### Pull the anonymizer image

`sudo docker pull docker.io/josejuanmartineziqvia/anonymizer:0.1`

#### Create a folder to store PDF files
`sudo mkdir anonymizer_docs`

`cd anonymizer_docs`

#### Create two folders: input (for original PDF to anonymizer) and output (to get the results)
`sudo mkdir input output`

#### Finally, instantiate a container using the image setting the input and output folders and connecting it to Apertium translation engine

From `anonymizer_docs` folder, where you should have `./input` and `./output` folders already created in previous steps, execute:

`sudo docker run -d --name anonymizer -p "9090:9090" --link "apertium" --expose "2737" -v "${PWD}/input:/opt/anonymizer/input" -v "${PWD}/output:/opt/anonymizer/output" docker.io/josejuanmartineziqvia/anonymizer:0.1`

### EXECUTION OF ANONYMIZATION

####Preparing PDF files 

Being in `anonymizer_docs` folder created before:

`sudo cp [path_to_example_pdf].pdf ./input/`

Copy all the pdfs you need to anonymize.

#### Request

You can launch the anonymization using a HTTP request, for example, from your browser or from a HTTP command line (curl) to the following url:

`http://162.44.148.238:9090/anonymizer/pdf/extract/translate/anonymize/bulk?from_lang=cat&to_lang=spa&host=http://apertium&port=2737`

IMPORTANT: First time it will take a while, since it will download several language models. But it's only the first time. To see the progress:

`sudo docker logs -f anonymizer`

#### Response
If you see in your browser:

`{'status': 'OK'}`

... that will mean that the process has successfully finished and you have the anonymized .txt results in `output` folder.

You can follow the procress using `sudo docker logs -f anonymizer`

Be patient, you are running 2 neural networks in a row inside a virtual environment with no GPU for X documents, so the process takes a while. Remember that the time for Linguamatics does not have anything to do with this and the performance is much higher in Production.


## DOCKER_COMPOSE INSTALLATION
### From docker hub
In `./`

`sudo docker-compose up -d`

This will take the docker-compose.yaml in the root folder and download the model from docker hub

### Construction mode
In `./docker/`

`sudo docker-compose up -d`

This will build and tag the docker image locally



