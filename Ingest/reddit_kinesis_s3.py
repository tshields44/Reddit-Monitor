import boto3
import requests
import json
import time


def firehose_comments():
    '''
    Reddit comments in json format inserted in S3 using Kinesis.
    '''

    firehose_client = boto3.client('firehose', region_name='us-east-1')

    url = 'https://apiv2.pushshift.io/reddit/comment/search'
    response = requests.get(url)
    json_comments = response.json()

    try:
        new = firehose_client.put_record(DeliveryStreamName= 'reddit_firehose',
                    Record= {'Data': json.dumps(json_comments['data']) + '\n'})
        

    except Exception:
        print("Did not work.")


def main():
    while True:
        try:
            firehose_comments()
        except Exception as e:
            print 'error reporting stats: ', e
        time.sleep(10)


if __name__=='__main__':
    main()
