#Power curve output for a wind turbine using the input of wind speed and power data. The output is a plot of the power curve and a CSV file containing the wind speed.
# P=0.5 Cp * rho * A * v^3

# Constants
rated_power = 15 # Rated power of the wind turbine in MW
wind_speed_cut_in = 3 # Cut-in wind speed in m/s
wind_speed_rated = 11 # Rated wind speed in m/s
wind_speed_cut_out = 25 # Cut-out wind speed in m/s

# Inputs 
# This could be user input, but for now, we will use a fixed value for demonstration purposes.

"""wind_speed =input("Enter the wind speed in m/s: ")

# Values for the user
# 1.- Windspeed
try:
    wind_speed = float(wind_speed)
except ValueError:    
    print("Invalid input. Please enter a valid number. Remember to use a decimal point for fractional values. Ex: 7.5")


#2 Method of interpolation
try:
    interpolation_method = input("Enter the interpolation method (linear or cubic): ")
except ValueError:
    print("Invalid input. Please enter a valid option. linear or cubic.")   
    exit()
"""


def linear_interpolation(wind_speed, power):

    """ Linear interpolation is the standard method """

    linear_result = (wind_speed - wind_speed_cut_in) / (wind_speed_rated - wind_speed_cut_in)

    return linear_result

# Calculate the power output using cubic interpolation
def cubic_interpolation(wind_speed, power):
    """Calculate the power output using cubic interpolation."""

    cubic_result = wind_speed**3 / wind_speed_rated**3

    return cubic_result

def Power_output(interpolation_method, wind_speed, power):
    """Calculate the power output using the specified interpolation method."""

    if interpolation_method == 'cubic':
        power_output = cubic_interpolation(wind_speed, power)

        if wind_speed < wind_speed_cut_in:
                power_output = 0

        if wind_speed > wind_speed_cut_out:
                power_output = 0

        else:
            power_output = cubic_interpolation(wind_speed, power) * rated_power


    elif interpolation_method == 'linear':
        power_output = linear_interpolation(wind_speed, power)

        if wind_speed < wind_speed_cut_in:
                power_output = 0

        if wind_speed > wind_speed_cut_out:
                power_output = 0

        else:
            power_output = linear_interpolation(wind_speed, power) * rated_power

    return power_output

if __name__ == "__main__":


    power_output = Power_output(interpolation_method, wind_speed, rated_power)

    print("Power output at wind speed of", wind_speed, "m/s is", round(Power_output('linear', wind_speed, rated_power), 4), "MW using linear interpolation.")




    