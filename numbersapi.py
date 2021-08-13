import requests


class NumbersApi():

    def get_number_fact(self, number):
        try:
            response = requests.get(f"{self.default_url}{number}/trivia")
            return response.text
        except Exception as e:
            return str(e)

    def get_random_number_fact(self):
        try:
            response = requests.get(f"{self.default_url}random/trivia")
            return response.text
        except Exception as e:
            return str(e)

    def __init__(self):
        self.default_url = "http://numbersapi.com/"

