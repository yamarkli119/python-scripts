import json
import csv


codes = {"country": [
          {
              "countryCode": "AD",
              "countryName": "Andorra",
              "continentName": "Europe"
          },
          {
              "countryCode": "AE",
              "countryName": "United Arab Emirates",
              "continentName": "Asia"
          },
          {
              "countryCode": "AF",
              "countryName": "Afghanistan",
              "continentName": "Asia"
          },
]
}


def get_data():
    with open("33_country_codes.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    countryCodes = []
    countries = []
    continents = []
    for country in data["country"]:
        countryCodes.append(country["countryCode"])
        countries.append(country["countryName"])
        continents.append(country["continentName"])
        return countryCodes, countries, continents



def saveCSV(countryCodes, countries, continents):
    with open("mycsv.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["country code", "country name", "continent name"])
        for i in range(len(countries)):
            writer.writerow([countryCodes[i], countries[i], continents[i]])
countryCodes, countries, continents = get_data()
saveCSV(countryCodes, countries, continents)

for country in codes["country"]:
#   print(country["countryCode"], country["countryName"], country["continentName"])
    countryCodes.append(country["countryCode"])
    countries.append(country["countryName"])
    continents.append(country["continentName"])

