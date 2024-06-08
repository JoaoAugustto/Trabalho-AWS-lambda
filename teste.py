import json

def lambda_handler(event, context):

    if 'body' not in event:
        return {
            'statusCode': 400,
            'body': 'Corpo da requisição não encontrado'
        }
    
    body = json.loads(event['body'])
    
    required_fields = ['oneValue', 'anotherValue', 'operation']
    for field in required_fields:
        if field not in body or body[field] is None:
            return {
                'statusCode': 400,
                'body': f'{field} não pode ser vazio ou nulo'
            }
    

    for field in ['oneValue', 'anotherValue']:
        if not isinstance(body[field], (int, float)):
            return {
                'statusCode': 400,
                'body': f'{field} precisa ser numérico'
            }
    

    valid_operations = {'soma', 'subtracao', 'multipliccaor', 'dividir'}
    if body['operation'] not in valid_operations:
        return {
            'statusCode': 400,
            'body': 'operation precisa ser: subtracao, soma, multipliccaor ou dividir'
        }
    

    response = 0
    if body['operation'] == 'soma':
        response = body['oneValue'] + body['anotherValue']
    elif body['operation'] == 'subtracao':
        response = body['oneValue'] - body['anotherValue']
    elif body['operation'] == 'multipliccaor':
        response = body['oneValue'] * body['anotherValue']
    elif body['operation'] == 'dividir':
        if body['anotherValue'] == 0:
            return {
                'statusCode': 400,
                'body': 'anotherValue não pode ser zero'
            }
        response = body['oneValue'] / body['anotherValue']
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
