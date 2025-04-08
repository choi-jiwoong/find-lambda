import boto3

TARGET_URL = 'TARGET_URL'
REGION = 'us-east-1'

def find_lambda_by_url(target_url):
    lambda_client = boto3.client('lambda', region_name=REGION)

    paginator = lambda_client.get_paginator('list_functions')
    for page in paginator.paginate():
        for function in page['Functions']:
            function_name = function['FunctionName']
            try:
                url_config = lambda_client.get_function_url_config(FunctionName=function_name)
                function_url = url_config.get('FunctionUrl')
                if function_url == target_url:
                    print(f'✅ Match found! Function name: {function_name}')
                    return function_name
            except lambda_client.exceptions.ResourceNotFoundException:
                # Function URL not configured for this Lambda
                continue

    print('❌ No matching Lambda function found.')
    return None

if __name__ == '__main__':
    find_lambda_by_url(TARGET_URL)