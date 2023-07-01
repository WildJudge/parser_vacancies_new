import json
from abc import ABC, abstractmethod
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
