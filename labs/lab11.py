'''
Created on 11/4/2019
@author:   Robert Schaedler III
Pledge:    I pledge my honor that i have abided by the Stevens Honor System.

CS115 - Lab 11
'''
import math

class QuadraticEquation:
    ''' A representation quadratic equation.'''

    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError(
                'Coefficient \'a\' cannot be 0 in a quadratic equation.')
        else:
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(c)

    @property
    def a(self):
        ''' Returns a'''
        return self.__a
    
    @property
    def b(self):
        ''' Returns b'''
        return self.__b
    
    @property
    def c(self):
        ''' Returns c'''
        return self.__c

    def discriminant(self):
        ''' Returns the discriminant of a quadratic'''
        return self.__b ** 2 - 4 * self.__a * self.__c
        
    def root1(self):
        ''' Returns the first root of the quadratic.'''
        return None if self.discriminant() < 0 else (-self.b + math.sqrt(self.discriminant())) / (2.0 * self.__a)

    def root2(self):
        ''' Returns the second root of the quadratic.'''
        return None if self.discriminant() < 0 else (-self.b - math.sqrt(self.discriminant())) / (2.0 * self.__a)

    def __str__(self):
        ''' Returns the string representation of the quadratic'''
        s = ''
        if math.fabs(self.__a) != 1:
            s = s + str(self.__a) + 'x^2'
        elif int(self.__a) == -1:
            s = s + '-x^2'
        else:
            s = s + 'x^2'
        if self.__b != 0:
            if self.__b < 0:
                s += ' - '
            else:
                s += ' + '
            if math.fabs(self.__b) != 1:
                s += str(math.fabs(self.__b))
            s += 'x'
        if self.__c != 0:
            if self.__c < 0:
                s += ' - '
            else:
                s += ' + '
            s += str(math.fabs(self.__c))
        return s + " = 0"
