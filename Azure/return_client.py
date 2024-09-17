#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-09-17
"""
# Standard Library
import os
# Third-Party
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
# Local/Own
from AUTH.get_keys import get_keys

marker = 'marker'

def client():
    '''
    Authenticates your credentials and creates a client.
    '''
    subscription_key, endpoint = get_keys()
    computervision_client = ComputerVisionClient(
        endpoint, CognitiveServicesCredentials(subscription_key))

    return computervision_client
    

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    print(client())


if __name__ == '__main__':
    main()