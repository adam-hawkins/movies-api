from pynamodb.exceptions import DoesNotExist
from movie_model import MovieModel
from utils.response import response


def get(event, context):
    try:
        found_movie = MovieModel.get(hash_key=event['path']['id'])
    except DoesNotExist:
        return response(404, {'error_message': 'Movie was not found'})

    # create a response
    return response(200, dict(found_movie))
