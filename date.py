'''
Created on 11/18/2019
@author:   Robert Schaedler III
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 10 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year as the calling object(self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,whether or not they int the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        ''' Changes the calling object to represent one calendar day after the date it originally represented.'''
        if self.day + 1 > DAYS_IN_MONTH[self.month]:
            self.day = 1
            # Month will change
            if self.month + 1 == 13:
                # Year will change
                self.year += 1
            next_m = self.month + 1
            self.month = next_m if next_m < 13 else 1
        else:
            self.day += 1

    def yesterday(self):
        ''' Changes the calling object to represent one calendar day before the date it originally represented.'''
        pass

    def addNDays(self, N):
        ''' Adds N days to the calling object.'''
        for i in range(0, N):
            print(self)
            self.tomorrow()
        print(self)
    
    def subNDays(self, N):
        ''' Subtracts N days from the calling object.'''
        for i in range(0, N):
            print(self)
            self.yesterday()
        print(self)
    
    def isBefore(self, d2):
        ''' Returns true if the calling object is a calendar date before a given date object. False otherwise.'''
        pass

    def isAfter(self, d2):
        ''' Returns true if the calling obejct is a calendar date after a given date object. False otherwise.'''
        return not self.isBefore(d2)
    
    def diff(self, d2):
        ''' Returns an integer number of days between the calling object and a given object. '''
        pass

    def dow(self):
        ''' Returns the day of the week of the calling obeject as a string.'''
        pass
    