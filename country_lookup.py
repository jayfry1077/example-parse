import requests
import os

COUNTRY_CODE_LOOKUP_URL = os.environ.get(
    'COUNTRY_CODE_LOOKUP_URL', 'https://www.travel-advisory.info/api')


def get_country_name(country_code=str):

    uppercase_country_code = country_code.upper()

    params = {'countrycode': uppercase_country_code}

    try:
        response = requests.get(COUNTRY_CODE_LOOKUP_URL, params=params).json()

        # Check if response was good
        if response['api_status']['reply']['code'] != 200:
            return f'Unable to find country with provided code {country_code}'

        # Check if our contry code was returned
        if uppercase_country_code not in response['data'].keys():
            return f'Invalid country code {country_code}'

        # Return country code data
        return response['data'][uppercase_country_code]['name']

    except:
        return f'Error while getting country code {country_code}'
