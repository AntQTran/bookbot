#!/usr/bin/env python3
import requests

url = input("enter URL: ")

file_name = input("enter file name: ")

res = requests.get(url)
res.raise_for_status()

with open(f"books/{file_name}.txt", 'w', encoding='utf-8') as f:
    f.write(res.text)

print(f"Finished downloading from {url}.")
