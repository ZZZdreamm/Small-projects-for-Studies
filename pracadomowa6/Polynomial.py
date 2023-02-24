class Polynomial:
    def __init__(self, polynomial_parameters = None):
        """
        Constructor of Polynomial:
        
        :polynomial_parameters: list of tuples made of (power,factor)
        """
        self._polynomial_parameters = {}
        if(polynomial_parameters is None):
            pass
        else:
            for power, factor in polynomial_parameters:
                self.set_parameters(power,factor)
    

    def set_parameters(self, power, factor):
        if(power in self._polynomial_parameters.keys() or power < 0 or factor == 0):
            raise ValueError("You created wrong polynomial")
        else:
            self._polynomial_parameters[power] = factor 

    def __str__(self) -> str:
        string_polynomial = ''
        first_element = True
        sorted_polynomial = sorted(self._polynomial_parameters, reverse=True)
        for power in sorted_polynomial:
            factor = self._polynomial_parameters[power]
            if (not first_element and factor > 1):
                factor = f'+{factor}'
            elif (factor == 1 and first_element == False):
                factor = f'+'
            elif (factor == -1):
                factor = f'-'
            elif(first_element == True and factor == 1):
                factor = ''

            
            if(power == 1):
                string_polynomial += f'{factor}x'
            elif (power == 0):
                if(factor == '+'):
                    string_polynomial += f'+1'
                elif(factor == '-'):
                    string_polynomial += f'-1'
                else:
                    string_polynomial += f'{factor}'
            else:
                string_polynomial += f'{factor}x^{power}'
            first_element = False
        return string_polynomial

    
    def degree(self) -> int:
        """Returns degree of polynomial"""
        greatest_power = 0
        for power in self._polynomial_parameters:
            if(power > greatest_power):
                greatest_power = power
        if(self._polynomial_parameters == {}):
            greatest_power = None
        return greatest_power

    
    def coefficient(self, power_of_factor) -> int:
        """Returns factor of given power"""
        if(power_of_factor in self._polynomial_parameters):
            factor = self._polynomial_parameters[power_of_factor]
        else:
            factor = 0
        return factor


    def value(self, value_of_x):
        """Returns value of polynomial with certain value of X"""
        polynomial_value = 0
        for power in self._polynomial_parameters:
            factor = self._polynomial_parameters[power]
            polynomial_value += factor*(value_of_x**power)
        return polynomial_value

    
    def __add__(self,second_polynomial):
        """Adds polynomial given as argument to first polynomial"""
        parameters1 = self._polynomial_parameters
        parameters2 = second_polynomial._polynomial_parameters
        powers1 = list(parameters1.keys())
        powers2 = list(parameters2.keys())
        all_powers = set(powers1 + powers2)
        new_polynomial = Polynomial()
        for power in all_powers:
            if power not in powers1:
                new_polynomial.set_parameters(power,parameters2[power])
            elif power not in powers2:
                new_polynomial.set_parameters(power,parameters1[power])
            else:
                if( (parameters1[power] + parameters2[power]) != 0):
                    new_polynomial.set_parameters(power, (parameters1[power] + parameters2[power]))  
        return new_polynomial



    def __sub__ (self,second_polynomial):
        """Substracts polynomial given as argument from first polynomial"""
        parameters1 = self._polynomial_parameters
        parameters2 = second_polynomial._polynomial_parameters
        powers1 = list(parameters1.keys())
        powers2 = list(parameters2.keys())
        all_powers = set(powers1 + powers2)
        new_polynomial = Polynomial()
        for power in all_powers:
            if power not in powers1:
                new_polynomial.set_parameters(power,-parameters2[power])
            elif power not in powers2:
                new_polynomial.set_parameters(power,parameters1[power])
            else:
                if( (parameters1[power] - parameters2[power]) != 0):
                    new_polynomial.set_parameters(power, (parameters1[power] - parameters2[power]))  
        return new_polynomial

