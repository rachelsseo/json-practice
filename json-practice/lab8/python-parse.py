#!/usr/bin/env python3

import json
import csv

def extract_and_write_to_csv(json_file): 
  
  with open(json_file, 'r') as file:
    data = json.load(file)

  with open('chacon.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)

    line_count = 0

    for item in data:
      if line_count >= 5:  # Stop after 5 lines
        break

      name = item.get('name', '')
      html_url = item.get('html_url', '')
      updated_at = item.get('updated_at', '')
      visibility = item.get('visibility', '')

      writer.writerow([name, html_url, updated_at, visibility])

      line_count += 1

json_file = '/Users/rachelseo/json-practice/data/schacon.repos.json'

extract_and_write_to_csv(json_file)

print("Data extraction and writing to chacon.csv completed.")
