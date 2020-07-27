import numpy as np

class room(object):
    '''
    An object which represents the temperature within an area, and the heat generation objects within this area

    Attributes:
    ----------
        x: float
            the length in the x direction of the room
        y: float
            the length of the room in the y direction
        temp: n x n numpy array, default = beginning temp of the room
            temperature at each smaller area in the room
        filled: n x n numpy array, default = none
            name of the object contained in each area
        sources: list of strings
            names of the heat sources in the room
        calc_points: list of strings
            names of the points of interest in the room
    '''
    
    def __init__(self,x,y,start_temp,n):
        self.x = np.linspace(0,x,n)
        self.y = np.linspace(0,y,n)
        self.temp = np.empty((n,n),dtype=float)
        self.filled = np.empty((n,n),dtype=str)
        self.filled[:][:] = None
        self.temp[:][:] = start_temp
        self.sources = []
        self.calc_points = []

    def __repr__(self):
        return print(self.temp)

    def add_source(self,n,*source):
        '''
        Adds a heat source to the room object

        Parameters:
        ----------
            n: int
                number of intervals that the x and y axis is split into
            *source: some number of source objects
                heat sources to be added
        '''

        for s in source:
            for i in range(n):
                for j in range(n): 
                    if (self.x[i] >= s.x0 and self.x[i] <= s.x1) and (self.y[j] >= s.y0 and self.y[j] <= s.y1):
                        self.temp[i][j] = s.temps[0]
                        self.filled[i][j] = 's_'+s.name
                        self.sources.append(s)

    def add_calc_point(self,n,*calc_points):
        '''
        Adds a calculation point to the room object

        Parameters:
        ----------
            n: int
                number of intervals that the x and y axis is split into
            *calc_points: some number of calc_point objects
                heat calculation points to be added
        '''
        for c in calc_points:
            for i in range(n):
                for j in range(n): 
                    if (self.x[i] >= c.x0 and self.x[i] <= c.x1) and (self.y[j] >= c.y0 and self.y[j] <= c.y1):
                        self.filled[i][j] = 'c_'+c.name
                        self.calc_points.append(c)


    def calc_point_avg(self,n,*calc_points):
        ''' 
        Returns a list of average temperatures within the calculation areas

            Parameters:
            -----------

            n:  int
                number of divisions in room object
            calc_points: list of calc_point objects
                some number of calculation points within the room object

            Notes:
            -----

            Averages of calc zones will be returned in the same order given

        '''
        num,tot = 0,0
        #averages = []

        for calc in calc_points:
            for i in range(n):
                for j in range(n):
                    if self.filled[i][j] == 'c_' + calc.name:
                        num += 1
                        tot += self.temp[i][j]

            calc.T_avg = tot/num
            #averages.append(tot/num)

        #return averages

class calc_point(object):
    ''' points at which the average temp is to be calculated over time

        attributes:
        ----------
        name: str
            reference name of the calc point
        x0: float
            starting x value of calc point
        x1: float
            ending x value of calc point
        y0: float
            starting y value of calc point
        y1: float
            ending y value of calc point
    
    '''
    def __init__(self,x0,x1,y0,y1,name):
        self.name = name
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.T_avg = 0

    def __repr__(self):
        return print(self.name)

class source(object):
    ''' points at which the average temp is to be calculated over time

        attributes:
        ----------
        name: str
            reference name of the heat source
        x0: float
            starting x value of heat source
        x1: float
            ending x value of heat source
        y0: float
            starting y value of heat source
        y1: float
            ending y value of heat source
        temp_fun: function handle
            returns temp of source at a given time
        temp: float
            temperature of source at a given time
    '''
    def __init__(self,name,x0,x1,y0,y1,temp_fun):
                
        self.name = name
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.temp_fun = temp_fun
        self.temp = 0.

    def __repr__(self):
        return print(self.name)