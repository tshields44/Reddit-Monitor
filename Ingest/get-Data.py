import os


def ingest_Dec_2016():
    '''Takes all reddit comments from December 2016
    & pushes it to s3'''

    i = 1
    while i < 31:
        if i < 10:
            os.system('wget -c http://files.pushshift.io/reddit/staging/RC_2016-12-0%s.gz'%i)
            os.system('gzip -d RC_2016-12-0%s'%i)
            os.system('aws s3 cp RC_2016-12-0%s s3://historical-reddit-comments'%i)
            os.system('rm RC_2016-12-0%s'%i)

            i = i + 1

        elif i >= 10:
            os.system('wget -c http://files.pushshift.io/reddit/staging/RC_2016-12-%s.gz'%i)
            os.system('gzip -d RC_2016-12-%s'%i)
            os.system('aws s3 cp RC_2016-12-%s s3://historical-reddit-comments'%i)
            os.system('rm RC_2016-12-%s'%i)

            i = i + 1

def ingest_Jan_2017():
    '''Takes all reddit comments from January 2017
    & pushes it to s3'''

    i = 1
    while i < 31:
        if i < 10:
            os.system('wget -c http://files.pushshift.io/reddit/staging/RC_2017-01-0%s.gz'%i)
            os.system('gzip -d RC_2017-01-0%s'%i)
            os.system('aws s3 cp RC_2017-01-0%s s3://historical-reddit-comments'%i)
            os.system('rm RC_2017-01-0%s'%i)

            i = i + 1

        elif i >= 10:
            os.system('wget -c http://files.pushshift.io/reddit/staging/RC_2017-01-%s.gz'%i)
            os.system('gzip -d RC_2017-01-12-%s'%i)
            os.system('aws s3 cp RC_2017-01-%s s3://historical-reddit-comments'%i)
            os.system('rm RC_2017-01-%s'%i)

            i = i + 1




if __name__ == '__main__':
    ingest_Dec_2016()
    ingest_Jan_2017()
