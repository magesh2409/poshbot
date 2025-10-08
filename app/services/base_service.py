from abc import ABC, abstractmethod

class BaseService(ABC):

    @abstractmethod
    def chat_completion(self, message):
        pass

