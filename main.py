import argparse
from country_lookup import get_country_name

parser = argparse.ArgumentParser()
parser.add_argument('lookup')
parser.add_argument('--country_code', help='Takes in the country code')

args = parser.parse_args()

if __name__ == '__main__':

    if args.lookup:
        try:
            country_name = get_country_name(args.country_code)
            print(country_name)
        except Exception as e:
            print(e)
