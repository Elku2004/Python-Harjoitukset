import json

tallennus_data = {"Nimi": "Inception",
              "Vuosi": 2010,
              "Näyttelijät": ["Leonardo DiCaprio", "Elliot Page"]}

with open("tuntitehtavat/tallennus.json", "w") as tiedosto:
    json.dump(tallennus_data, tiedosto)
with open("tuntitehtavat/tallennus.json", "r") as tiedosto:
    data_luettu = json.load(tiedosto)
print(f"Nimi: {data_luettu["Nimi"]}, Vuosi: {data_luettu["Vuosi"]}, Näyttelijät: {data_luettu["Näyttelijät"]}")
