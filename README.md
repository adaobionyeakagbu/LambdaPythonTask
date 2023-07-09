
A client drops many files in the company's S3 bucket. We want to organize the files by day. Write a lambda script to trigger when a file lands in the S3 bucket and move it to a folder names YYYYMMDD/filename based on when the client created the file in the s3 bucket.


When adding your python script as a lambda function, delete the default created .py file in the function, add yours, then edit the handler to match the name of the .py you uploaded. Then create test event and test.
