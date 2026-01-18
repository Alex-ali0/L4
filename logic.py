from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]["official-artwork"]["front_shiny"])
        else:
            return "https://upload.wikimedia.org/wikipedia/ru/7/77/Pikachu.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    def plus_age(self,age=1):
            plus = randint(1,3)
            age += plus
            # Определяем правильную форму слова
            last_two_digits = age % 100
            last_digit = age % 10
            
            if 11 <= last_two_digits <= 14:
                form = "лет"
            elif last_digit == 1:
                form = "год"
            elif last_digit in [2, 3, 4]:
                form = "года"
            else:
                form = "лет"
            return f"Ваш покемон вырос на {plus} {form}"\
            f"\nему {age} {form}"
            



    # Метод класса для получения информации 
    def info(self):
        if self.pokemon_number == 42 or self.pokemon_number ==666 or self.pokemon_number ==52 or self.pokemon_number ==67 or self.pokemon_number ==555 or self.pokemon_number ==444 or self.pokemon_number ==777 or self.pokemon_number ==888 or self.pokemon_number ==999 or self.pokemon_number ==1001:
            return "Поздравляю вам попался редкий покемон:"\
            f"Имя твоего покеомона: {self.name}"\
            f"\nНомер твоего покеомона: {self.pokemon_number}"
        else:
            return f"Имя твоего покеомона: {self.name}"\
            f"\nНомер твоего покеомона: {self.pokemon_number}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img






