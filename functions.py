from classes import*

def TTrans_step(room,temp,fill):
    new_temps = np.copy(room.temp)
    
    for i in range(np.shape(room.temp)[0]):
        for j in range(np.shape(room.temp)[1]):
            if room.filled[i][j][0] != 's':
                new_temps[i][j] = surround_temp(room,i,j)

    room.temp = new_temps

def surround_temp(room,i,j):
    '''return the average temperature of the current area and the surrounding areas

        parameters:
        ----------
            room: room object
                contains temperature information about a given area
            i: int
                x location of the current 'particle' in the room
            j: int
                y location of the current 'particle' in the room

        returns:
        -------
            tot/n: int
                avg - total surrounding temp / number of surrounding measurements

    '''
    
    n,tot = 0,0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            #check if indexing out of bounds of array
            try: 
                tot += room.temp[i+x][j+y]
                n += 1
            except IndexError:
                pass
    return tot/n
                    


            
def new_temp(T0,T_surround,delta_t,height=2):
    ''' finding the new temperature of one partition in the room

        parameters:
        ----------
            T0: float
                initial temperature of the area
            T_surround: float
                average temperature of the neighboring area segments
            delta_t: float
                unit change in time
            height: float, default = 2
                height of the room
    '''

    delta_t *= 3600
    rho = air_density_calculator(T0)
    h = 15 # convective heat transfer coefficient (W/m^2K)
    spec_heat_cap = 1005 # specific heat capacity of air around 30C (J/kg*K)
    coef = (delta_t*h)/(rho*height*spec_heat_cap)

    return coef*(T_surround-T0)-T0

def air_density_calculator(temp):
    ''' calculates the air density at P = 1 atm for a given temperature of air

        Parameters:
        ----------
            temps:  float
                air temperature at a point in the room
    '''

    pressure = 101375 # atmospheric pressure (pa)
    M = 0.0289654 # molar mass of dry air kg/mol
    T = temp + 273.15 # absolute temp (K)
    R = 8.3145 # gas constant (J/mol*K)
    return (pressure*M)/(R*T)

def update_temps(room,time):
    ''' updates the temperatures of all heat sources at a given time

        parameters:
        ----------
            room: room object
                contains temperature information about a given area
            time: float
                time elapsed from beginning of simulation
    '''

    for src in room.sources:
        src.temp = src.temp_fun(time)

def temp_fun_heater1(time):
    ''' function of temperature over time for heat source heater1

        parameters:
        ----------
            time: float
                time elapsed from beginning of simulation
    '''

    return 30 + 0*time

if __name__ == '__main__':

    n = 100
    room = room(10,5,20,n)
    heater = source('heater1',1,1.5,0,0.2,temp_fun_heater1)
    bed = calc_point(0,2,2,3,'my_bed')

    room.add_calc_point(n,bed)
    room.add_source(n,heater)