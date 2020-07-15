from classes import*

def TTrans_step(temp,fill):
    pass

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

def update_temps(time):
    ''' updates the temperatures of all heat sources at a given time

        parameters:
        ----------
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

'''def greater_than_index(time,source_times):
    for t in range(source_times):
        if t == len(source_times):
            return -1
        if (time >= source_times[t] and time < source_times[t+1]):
            return t
    raise KeyError
'''