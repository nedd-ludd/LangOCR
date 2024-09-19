#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-09-17
"""  # Standard Library
import os
import time
# Third-Party
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
# Local/Own
from Azure.return_client import client

# image_path = r".\test_case\Image(49).jpg"
image_path = r"C:\Users\natha\Desktop\LangOCR\test_case\Image (49).jpg"
marker = 'marker'


def hello_world(client):
    '''
    OCR: Read File using the Read API, extract text - remote
    This example will extract text in an image, then print results, line by line.
    This API call can also extract handwriting style text (not shown).
    '''

    # Call API with URL and raw response (allows you to get the operation location)
    # read_response = client.read(read_image_url,  raw=True)
    with open(image_path, "rb") as image_stream:
        # Call the API
        read_response = client.read_in_stream(image_stream, raw=True)
    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results
    while True:
        read_result = client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Print the detected text, line by line
    

    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text)
                print(line.bounding_box)
    else:
        print(read_result.status)
    '''
    END - Read File - remote
    '''

    print("End of Computer Vision quickstart.")


def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    hello_world(client())


if __name__ == '__main__':
    main()
