import json
import logging
import uuid

from movie_model import MovieModel
from utils.response import response


def create(event, context):
    data = json.loads(event['body'])
    print(event)
    logging.info(data)
    if 'title' not in data:
        logging.error('Validation Failed')
        return response(422, {'error_message': 'Couldn\'t create the movie'})

    if not data['title']:
        logging.error('Validation Failed - text was empty. %s', data)
        return response(422, {'error_message': 'Couldn\'t create the movie. As title was empty'})

    movie = MovieModel(id=str(uuid.uuid1()),
                       title = data['title'],
                       release_format = data['release_format'],
                       length = data['length'],
                       release_year = data['release_year'],
                       rating = data['rating'])

    # write the movie to the database
    movie.save()

    # create a response
    return response(201, dict(movie))
