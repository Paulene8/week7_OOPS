class People:
    def __init__(self, firstname, lastname, gender, status):    #initiating attributes to be used in the programme
        self.first_name = firstname
        self.lastname = lastname
        self.__gender = gender
        self.status = status

    def get_firstname(self):
        return self.first_name

    def set_firstname(self, new_lastname):
        self.first_name = new_lastname

    def get_lastname(self):
        return self.lastname.upper()    #Read lastname in uppercase

    def get_gender(self):
        return self.__gender  #HOW DO YOU MAKE IT "PRIVATE USING DUNDERS?"




    def get_status(self):
        return self.status


    def check_status(self, status):
        if self.status == "Employee":
            return True
        else:
            return False

