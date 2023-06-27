import requests

url = "https://drug-info-and-price-history.p.rapidapi.com/1/druginfo"

querystring = {"drug":"rivaroxaban"}

headers = {
	"X-RapidAPI-Key": "8ddd0af7ddmshc23c8aa002b0fcep132a15jsnd0be49b48bf0",
	"X-RapidAPI-Host": "drug-info-and-price-history.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)