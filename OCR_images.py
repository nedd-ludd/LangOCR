#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-09-17
"""
import os
# TODO: import json
marker = 'marker'
def func():
    pass

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)

    # for file in C:\Users\natha\Desktop\LangOCR\Scans
    # azure OCR call
    # get page and type from call
    # add results to C:\Users\natha\Desktop\LangOCR\OCR_Data\words_master.json

    func()

if __name__ == '__main__':
    main()