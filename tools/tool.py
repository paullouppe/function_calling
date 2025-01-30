from abc import ABC, abstractmethod

class Base_Tool(ABC):
    @property
    @abstractmethod
    def config(self):
        """This property must be implemented in subclasses"""
        pass

    @property
    @abstractmethod
    def wrap_output(self):
        return False
    
    @property
    @abstractmethod
    def function_name(self):
        """This property must be implemented in subclasses"""
        pass

    @abstractmethod
    def call(self):
        """This method must be implemented in subclasses"""
        pass


class Example_Tool(Base_Tool):
    def __init__(self):
        self._config = {}
        self._wrap_output = False

    @property
    def config(self):
        return self._config
    
    @property
    def wrap_output(self):
        return self._wrap_output
    
    def call(self):
        return "Example_Tool called successfully"