import boto3
from datetime import datetime
import json

def lambda_handler(event, context):

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(event['S3Bucket'])
    key = event['S3Key']
    obj = list(bucket.objects.filter(Prefix=key))
    json_file = obj[0].get()['Body'].read().decode('utf-8')
    json_input = json.loads(json_file)

    conn = boto3.client('emr')
    cluster_id = conn.run_job_flow(
        Name= json_input["Name"]+datetime.today().strftime('%Y%m%d'),
        LogUri= json_input["LogUri"],
        ReleaseLabel= json_input["ReleaseLabel"],
        Instances= json_input["Instances"],
        Applications= json_input["Applications"],
        VisibleToAllUsers= json_input["VisibleToAllUsers"],
        JobFlowRole= json_input["JobFlowRole"],
        ServiceRole= json_input["ServiceRole"],
        ScaleDownBehavior= json_input["ScaleDownBehavior"],
        EbsRootVolumeSize= json_input["EbsRootVolumeSize"],
        Tags= json_input["Tags"]
        # Steps= json_input["Steps"]    # Can optionally input initial steps to include in the EMR cluster.
    )
    return cluster_id
