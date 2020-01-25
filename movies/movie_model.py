import os
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class MovieModel(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE']
        if 'ENV' in os.environ:
            host = 'http://localhost:8000'
        else:
            region = 'us-east-1'
            host = 'https://dynamodb.us-east-1.amazonaws.com'

    movie_id = UnicodeAttribute(hash_key=True, null=False)
    title = UnicodeAttribute(null=False) # 1 - 50 chars
    release_format = UnicodeAttribute(null=False) #only VHS, DVD, ans Streaming acceptable
    length = NumberAttribute(default=60) # length in minutes between 0-500
    release_year = NumberAttribute(default=1980) # between 1800 and 2100, possibly not exceeding $current_year
    rating = NumberAttribute(default=1) # between 1 and 5

    def save(self, conditional_operator=None, **expected_values):
        '''save the movie to the dynamo table'''
        self.updatedAt = datetime.now()
        super(MovieModel, self).save()
