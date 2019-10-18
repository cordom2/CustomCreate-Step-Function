import boto3

def lambda_handler(event, context):
    connection = boto3.client('emr')
    step_info = connection.describe_step(
        ClusterId=event['JobFlowId'],
        StepId=event['StepId']
    )
    event['StepStatus'] = step_info['Step']['Status']['State']
    return event