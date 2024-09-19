#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-09-19
"""
import os
import json

marker = 'marker'

def add_ocr_result(day, cat, content, all_words):

    new_entry = {
        "day": day,
        "cat": cat, 
        "content": content,
        "all_words": all_words
    }

    try:
        with open("Data\data.json", "r") as json_file:
            data = json.load(json_file) 
    except FileNotFoundError:
        data = []

    data.append(new_entry)

    with open("Data\data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

print("Data saved to data.json")

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    day = 30
    cat = "vocab"
    content = [{"text": "text", "bounding_box": [1, 2, 3, 4]}]
    all_words = ["cat", "dog", "bird"]
    add_ocr_result(day, cat, content, all_words)

if __name__ == '__main__':
    main()