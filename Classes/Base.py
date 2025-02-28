from abc import ABC, ABCMeta, abstractmethod

# 3. Abstraction
class AbstractTravelService(ABC):
    # Every hotel/flight or service have ids, names etc.
    def __init__(self, service_id, availability, price, service_name):
        self.__service_id = service_id
        self.__availability = availability
        self.__price = price
        self.__service_name = service_name
    
    # getter methods:
    def get_service_id(self): 
        return self.__service_id
    def get_avilability(self): 
        return self.__availability
    def get_price(self): 
        return self.__price
    def get_service_name(self): 
        return self.__service_name                          
      
    # setter methods: 
    def set_service_id(self, service_id): 
        self.__service_id = service_id
    def set_avilability(self, avilability): 
        self.__availability = avilability     
    def set_price(self, price): 
        self.__price = price
    def set_service_name(self, service_name): 
        self.__service_name = service_name

    # Abstract Methods:
    @abstractmethod
    def calculate_cost():
        pass
    @abstractmethod
    def get_details():
        pass
    @abstractmethod
    def book_service():
        pass

# 7. Metaclass
class ServiceMeta(ABCMeta):
    registry = {}

# 1.
class TravelService(AbstractTravelService, metaclass = ServiceMeta):
    # Total number of hotel/flight services created.
    __total_services = 0 
    
    def __init__(self, service_id, availability, price, service_name):
        super().__init__(service_id, availability, price, service_name)

        # total services is bound to class not object
        # Increase when service is created
        TravelService.__total_services += 1 

    # 4.
    # Class Method
    @classmethod
    def get_total_service(cls):
        print(f"Total number of travel services available: {cls.__total_services}")
        return cls.__total_services
    
    # Static Method
    @staticmethod
    def is_valid_service_id(service_id):
        return isinstance(service_id, int) and service_id > 0

    # 5. Magic Methods
    def __str__(self):
        return f"{self.get_service_name()} (ID: {self.get_service_id()}, Price: {self.get_price()}, Available: {self.get_avilability()})"

    def __repr__(self):
        return f"TravelService({self.get_service_id()}, {self.get_avilability()}, {self.get_price()}, '{self.get_service_name()}')"
    
    # Compare objects
    def __eq__(self, other):
        return self.get_service_id() == other.get_service_id()
        
print("Base.py is called.")