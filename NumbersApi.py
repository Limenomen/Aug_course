import requests


class NumbersApi():

    def get_number_fact(self, number):
        response = requests.get(f"{self.default_url}{number}/trivia")
        return response.text

    def get_random_number_fact(self, number):
        response = requests.get(f"{self.default_url}random/trivia")
        return response.text

    def __init__(self):
        self.default_url = "http://numbersapi.com/"

