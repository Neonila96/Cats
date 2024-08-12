import requests


url_breeds = "https://catfact.ninja/breeds"


response_breeds = requests.get(url_breeds)

print(response_breeds.text)


print(response_breeds.status_code)


url_breeds_page_1 = "https://catfact.ninja/breeds?page=1"

response_breeds_page_1 = requests.get(url_breeds_page_1)


print(response_breeds_page_1.text)

print(response_breeds_page_1.status_code)



url_fact = "https://catfact.ninja/fact"

response_fact = requests.get(url_fact)


print(response_fact.text)

print(response_fact.status_code)

url_facts = "https://catfact.ninja/facts"

response_facts = requests.get(url_facts)

print(response_facts.text)

print(response_facts.status_code)
