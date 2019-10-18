import json
import boto3

def lambda_handler(event, context):
    job_flow_id = event['JobFlowId']
    print("Job flow ID:", job_flow_id)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(event['S3Bucket'])
    key = event['S3Key']
    obj = list(bucket.objects.filter(Prefix=key))
    json_file = obj[0].get()['Body'].read().decode('utf-8')
    json_input = json.loads(json_file)

    connection = boto3.client('emr')
    step_response = connection.add_job_flow_steps(JobFlowId=job_flow_id, Steps=json_input)
    step_ids = step_response['StepIds']
    print("Step IDs:", step_ids)

    event['StepId'] = step_ids[0]

    return event
