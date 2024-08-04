ERRORCODE = -1

class hardwareSet:

    def __init__(self):
        self.__capacity=0
        self.__availability = 0
        self.__checkedOut = 0

    def initialize_capacity(self,qty):
        self.__capacity = qty
        self.__availability = qty
    
    def get_availability(self):
        return self.__availability
    
    def get_capacity(self):
        return self.__capacity
    
    def get_checkout(self):
        return self.__checkedOut

    def check_out(self, qty):
        if self.__availability >= qty:
            self.__checkedOut += qty
            self.__availability -= qty
            return 0
        else:
            self.__checkedOut += self.__availability
            self.__availability = 0
            return ERRORCODE
        
    def check_in(self, qty):
        try:
            if self.__checkedOut >= qty:
                self.__checkedOut -= qty
                return 0
            else:
                return ERRORCODE
        except :
            return ERRORCODE