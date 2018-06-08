import requests
import os


class Postmon:

    def __init__(self):
        self.__host = os.getenv('POSTMON_HOST', '')

    def get_address(self, zip_code):
        print('Getting address with zip_code: {}'.format(zip_code))

        url = '{}/v1/cep/{}'.format(self.__host, zip_code)

        response = requests.get(url)
        response.raise_for_status()

        return response.json()
