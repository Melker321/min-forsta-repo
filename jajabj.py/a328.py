import requests

country_name = input("Skriv ditt land: ")

response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')
country = response.json()

# Hämta rätt data från API-svaret
capital = country[0]['capital'][0]  # Capital är en lista
name = country[0]['name']['common']  # 'name' är en ordlista, vi hämtar 'common'
population = country[0]['population']  # Population är ett heltal
languages = ", ".join(country[0]['languages'].values())  # 'languages' är en ordlista, vi hämtar värdena

# Skriv ut informationen
print(f"Namn: {name} \nHuvudstad: {capital}\nBefolkning: {population}\nSpråk: {languages}")
