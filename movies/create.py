import json
import logging
import uuid

from movies.movie_model import MovieModel
from movies.utils.response import response


def create(event, context):
    data = json.loads(event['body'])
    print(event)
    logging.info(data)
    if 'name' not in data:
        logging.error('Validation Failed')
        return response(422, {'error_message': 'Couldn\'t create the movie'})

    if not data['name']:
        logging.error('Validation Failed - text was empty. %s', data)
        return response(422, {'error_message': 'Couldn\'t create the movie. As name was empty'})

    movie = MovieModel(id=str(uuid.uuid1()),
                       name=data['name'],
                       tagline=data['tagline'],
                       location=data['location'])

    # write the movie to the database
    movie.save()

    # create a response
    return response(201, dict(movie))
