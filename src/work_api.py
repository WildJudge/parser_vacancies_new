from abc import ABC, abstractmethod

import requests as requests
import os


class WorkApi(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class HeadHunter(WorkApi):
    """Класс для работы с API HeadHunter"""

    url = 'https://api.hh.ru/vacancies'

    def __init__(self, text, per_page, city):
        self.text = text
        self.per_page = per_page
        self.area = city

    def get_info(self):
        """
        Получает список вакансий
        :return: list
        """
        response = requests.get(self.url, params=self.__dict__)
        info = response.json()['items']
        return info


class SuperJob(WorkApi):
    """Класс для работы с API SuperJob"""

    API_KEY = {'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')}
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, text, t=None, c=None):
        self.keyword = text
        self.t = t
        self.c = c

    def get_info(self):
        """
        Получает список вакансий
        :return: list
        """
        response = requests.get(self.url, headers=self.API_KEY, params=self.__dict__)
        info = response.json()['objects']
        return info
