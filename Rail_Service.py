from abc import ABC,abstractmethod
class RailService(ABC):

    @abstractmethod
    def add_Railticket(self):
        pass
    @abstractmethod
    def delete_Railticket(self):
        pass
    @abstractmethod
    def list_Railticket(self):
        pass
    @abstractmethod
    def search_Railticket(self):
        pass
    @abstractmethod
    def max_price_ticket(self):
        pass
    @abstractmethod
    def min_price_ticket(self):
        pass
    