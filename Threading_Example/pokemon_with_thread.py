from threading import Thread
from pokemon import Pokemon
import requests
import time

class Fight(Thread):
    def __init__(self, pokemon1, pokemon2):
        super().__init__()
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

        def

    def run(self):
        while self.pokemon1.can > 0 and self.pokemon2.can > 0:
            self.pokemon1.hasar_ver(self.pokemon2)

            if self.pokemon2.can > 0:
                self.pokemon2.hasar_ver(self.pokemon1)

        if self.pokemon1.can > 0:
            self.winner = self.pokemon1
        else:
            self.winner = self.pokemon2

class PokemonGetThread(Thread):
    is_completed = False
    def __init__(self,pokemon_uri,pokemon):
        super().__init__()
        self.pokemon = pokemon
        self.pokemon_url = pokemon_uri
        self.pokemon_nesnesi = None

    def is_completed_thread(self):
        return self.is_completed

    def get_pokemon(self):
        return self.pokemon_nesnesi

    def run(self):
        pokemonjson = requests.get(self.pokemon_url).json()
        yetenekler = []

        for yetenek in pokemonjson['abilities']:
            if yetenek["ability"] != None and yetenek["ability"]["name"] != None:
                abilities.append(yetenek["ability"]["name"])

        self.pokemon_nesnesi = Pokemon(
            pokemonjson['name'],
            pokemonjson['weight'],
            pokemonjson['heigth']
            yetenekler
        )
        for biri in pd['stats']:
            statName = biri['stat']['name']

            if statName == "speed":
                pokemonNesnesi.hiz = biri['base_stat']
            elif statName == "defense":
                pokemonNesnesi.savunma = biri['base_stat']
            elif statName == "attack":
                pokemonNesnesi.saldiri = biri['base_stat'] / 10
            elif statName == "hp":
                pokemonNesnesi.can = biri['base_stat']

        self.is_completed = True


class Pokemonlar(Thread):
    def run(self):


        apiUrl = "http://pokeapi.co/api/v2/"
        pokemonListesi = requests.get(apiUrl + "pokemon/").json().get('results')
        pokemonlarThread = []
        for i in pokemonListesi:
            pokemonThread = PokemonGetThread(i.get('url'),i.get("name"))
            pokemonThread.start()
            pokemonlarThread.append({"pokemon":i.get('name'),"thread":pokemonThread})

        all_completed = False

        while all_completed is False:
            all_completed = True
            for i in pokemonlarThread:

                print("%s is_completed : %s " %(i.get("pokemon"),i.get("thread").is_completed_thread()))

                if i.get("thread").is_completed_thread() is False:
                    all_completed = False
            time.sleep(5)

if __name__ == '__main__':
    p = Pokemonlar()
    p.start()
