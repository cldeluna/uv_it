# /// script
# requires-python = "==3.11.12"
# dependencies = [
#     "requests",
# ]
# ///


import requests
import sys
import pprint

iso3letter = "CZE"

print("\nPython version:")
print(".".join(map(str, sys.version_info[:3])))
print(f"Virtual environment path: {sys.prefix}\n")

# REST call to restcountries.com API
response = requests.get('https://restcountries.com/v3.1/all')
countries = response.json()

print(f"\nNumber of countries: {len(countries)}\n")

common_name = countries[0]["name"]["common"]
print(f"\nCommon name of the first country: {common_name}\n")
cca3 = countries[0]["cca3"]
print(f"\nCCA3 of the first country: {cca3}\n")

for line in countries:
    if line["cca3"] == iso3letter:
        print(f"\nFound country with CCA3 code: {iso3letter} {line['name']['official']}\n")
        pprint.pprint(line)
        break
print()
print()
print("\nKeys of the first country dictionary:")
pprint.pprint(list(countries[0].keys()))