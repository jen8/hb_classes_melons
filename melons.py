"""This file should have our order classes in it."""
# PART 4 - random module used in get_base_price method in AbstractMelonOrder class
from random import choice 
from datetime import datetime

#creating get base price method in abstract melon order class
# import randchoice and it has to be between 5-9, which will be our base price
# return of this method willl be used for our get total method

#AbstractMelonOrder is the parent class/superclass 
class AbstractMelonOrder(object):
    #this method will run when an object is instantiated, it will require species
    #and quantity for arguments
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        #these set the initial attributes for species, quantity and shipped status
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0

    def check_rush_hour_time(self):
        #instantiating an object, taking the exact time/date of the moment
        time_order_placed = datetime.today()
        #finding the day of the week when the order was placed
        weekday_of_order = time_order_placed.weekday()
        #get the hour of when the order was placed
        hour_of_order = time_order_placed.hour

        #check if Monday - Friday
        if weekday_of_order in range(0,5):
            #check if between the hours of 8am - 11am
            if hour_of_order in range(8,11):
                #return yes in rush hour
                return True
        else:
            #return no, not in rush hour
            return False

    #method that finds a random integer from 5-9 and assigns it as the base price
    def get_base_price(self):
        # save our output of "check_rush_hour_time" method
        rush_hour_check = self.check_rush_hour_time()
        #getting a random base_price choice from $5-9
        base_price = choice(range(5,10))

        #if order placed during rush hour
        if rush_hour_check == True:
            #increment the base price by 4
            base_price += 4

        return base_price

    #method that finds the total price
    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        #checks if the species is Christmas Melon
        if self.species.lower() == "christmas melon":
            #if it is, increase the base price by 1.5x
            base_price = base_price * 1.5
        
        #calculates the total price for the melons
        total = (1 + self.tax) * self.qty * base_price
        return total

    #method changes the shipping status attribute to True
    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

#DomesticMelonOrder subclass of AbstractMelonOrder, inherits the attributes and methods
#from parent class
class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    #this method will run when an object is instantiated, it will require species
    #and quantity for arguments    
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        #also initializes the __init__ method from the parent class
        super(DomesticMelonOrder,self).__init__(species, qty)
        #set Domestic order class specific attributes to order for order_type and tax
        self.order_type = "domestic"
        self.tax = 0.08

#InternationalMelonOrder subclass of AbstractMelonOrder, inherits the attributes and methods
#from parent class
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    #this method will run when an object is instantiated, it will require species, quantity 
    #and country code for arguments  
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        #also initializes the __init__ method from the parent class
        super(InternationalMelonOrder,self).__init__(species, qty)
        #set International order class specific attributes to order for country code,
        #order_type and tax
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    #method that is specific to InternationalMelonOrder class and calculates total price

    def get_total(self):
        """Calculate price."""

        #saving the output of the parent class' get_total() to a variable
        total = super(InternationalMelonOrder,self).get_total()
        #checks if the number of melons is less than 10
        if self.qty < 10:
            #if it is, adds a flat fee of $3 to the total
            total = total + 3
        #otherwise just return total
        return total

    #method that is specific to InternationalMelonOrder class and returns country code    
    def get_country_code(self):
        """Return the country code."""
        return self.country_code

#GovernmentMelonOrder subclass of AbstractMelonOrder, inherits the attributes and methods
#from parent class
class GovernmentMelonOrder(AbstractMelonOrder):

    #this method will run when an object is instantiated, it will require species and 
    #quantity for arguments 
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        #also initializes the __init__ method from the parent class
        super(GovernmentMelonOrder,self).__init__(species, qty)
        #set Government order class specific attributes to order for passed_inspection 
        #status, order_type and tax
        self.order_type = "government"
        self.tax = 0
        self.passed_inspection = False

    #method that is specific to GovernmentMelonOrder class sets passed_inspection status
    #to true if passed argument = True
    def mark_inspection(self,passed):
        if passed == True:
            self.passed_inspection = True

