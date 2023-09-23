from abc import ABC ,abstractmethod
class Dialogo(ABC):
    @abstractmethod 
    def saludar():
        pass
    @abstractmethod
    def despedirse():
        pass
    @abstractmethod
    def perdon():
        pass
    @abstractmethod
    def pedirCafe():
        pass
    @abstractmethod
    def cuantoCuesta():
        pass
    @abstractmethod
    def dondeQueda():
        pass