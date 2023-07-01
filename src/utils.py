import json
from abc import ABC, abstractmethod
from pprint import pprint

import requests as requests


class WorkApi(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Vacancies(ABC):

    @abstractmethod
    def __init__(self):
        pass


class WriteInfo(ABC):
    pass


class HaedHunter(WorkApi):
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, text, per_page, city):
        self.test = text
        self.per_page = per_page
        self.area = city

    def get_info(self):
        response = requests.get(self.url, params=self.__dict__)
        info = response.json()['items']
        return info
