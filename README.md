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

## Installation
### From docker hub
In `./`

`sudo docker-compose up -d`

This will take the docker-compose.yaml in the root folder and download the model from docker hub

### Construction mode
In `./docker/`

`sudo docker-compose up -d`

This will build and tag the docker image locally


  



