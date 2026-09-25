#Power curve output for a wind turbine using the input of wind speed and power data. The output is a plot of the power curve and a CSV file containing the wind speed.
# P=0.5 Cp * rho * A * v^3

#Inputs: 
rated_power = 15 # Rated power of the wind turbine in MW
cut_in_speed = 3 # Cut-in wind speed in m/s
rated_wind_speed = 11 # Rated wind speed in m/s
cut_out_speed = 25 # Cut-out wind speed in m/s

def power(wind_speed, power):
    """Power formula for a wind turbine."""
    P = 0.5 * Cp * rho * A * wind_speed**3

return P



def Power_output(interpolation_method, wind_speed, power):
    """Calculate the power output using the specified interpolation method."""

    if interpolation_method == 'cubic':
        power_output = cubic_interpolation(wind_speed, power)
    elif interpolation_method == 'linear':
        power_output = linear_interpolation(wind_speed, power)

return power_output


# Done
def linear_interpolation(wind_speed, power):

""" Linear interpolation is the standard method """

linear_result = wind_speed - wind_speed_in / wind_speed_rated - wind_speed_in

return linear_result

# Calculate the power output using cubic interpolation
# Done
def cubic_interpolation(wind_speed, power):
"""Calculate the power output using cubic interpolation."""

cubic_result = wind_speed**3 / wind_speed_rated**3

return cubic_result

    