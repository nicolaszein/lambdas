import json
from postmon import Postmon


def handle(event, context):
    zip_code = event.get('queryStringParameters', {}).get('zip_code')
    postmon = Postmon()

    try:
        address = postmon.get_address(zip_code=zip_code)
    except Exception as e:
        try:
            status_code = e.response.status_code
        except AttributeError:
            status_code = 500

        return {
            'statusCode': status_code,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'message': f'Error {e} trying to get address!'
            })
        }

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(address)
    }
