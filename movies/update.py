import json
import logging
import uuid

from movie_model import MovieModel
from utils.response import response


def update(event, context):
    data = json.loads(event['body'])

    try:
        found_movie = MovieModel.get(hash_key=event['path']['id'])
    except DoesNotExist:
        return response(404, {'error_message': 'Movie was not found'})

    print(event)
    logging.info(data)

    if 'title' in data.keys() and data['title']:
        found_movie.title = data['title']
    if 'release_year' in data.keys() and data['release_year']:
        found_movie.release_year = data['release_year']
    if 'release_format' in data.keys() and data['release_format']:
        found_movie.release_format = data['release_format']
    if 'rating' in data.keys() and data['rating']:
        found_movie.release_year = data['rating']
    if 'length' in data.keys() and data['length']:
        found_movie.length = data['length']

    # write the update to the database
    found_movie.save()

    # create a response
    return response(201, dict(found_movie))
