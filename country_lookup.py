import requests
import os

COUNTRY_CODE_LOOKUP_URL = os.environ.get(
    'COUNTRY_CODE_LOOKUP_URL', 'https://www.travel-advisory.info/api')


def get_country_name(country_code=str):

    uppercase_country_code = country_code.upper()

    params = {'countrycode': uppercase_country_code}

    try:
        response = requests.get(COUNTRY_CODE_LOOKUP_URL, params=params).json()

        if response['api_status']['reply']['code'] != 200:
            return f'Unable to find country with provided code {country_code}'

        return response['data'][uppercase_country_code]['name']

    except Exception as e:
        raise f'Error while getting country code {e}'
