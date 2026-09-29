#Power curve output for a wind turbine using the input of wind speed and power data. 
# P=0.5 Cp * rho * A * v^3


def power_output (wind_speed, rated_power=15, wind_speed_cut_in=3, wind_speed_rated=11, wind_speed_cut_out=25, interpolation_method='linear'):

    """Error handling for the interpolation method and calculation of the power output based on the wind speed and the specified interpolation method."""

    if interpolation_method not in ['linear', 'cubic']:
        raise ValueError("Invalid interpolation method. Please choose 'linear' or 'cubic'.")

    # Calculate power out of range wind speeds 
    if wind_speed < wind_speed_cut_in:
        return 0

    if wind_speed >= wind_speed_cut_out:
        return 0

    # Nominal power output 
    if wind_speed >= wind_speed_rated:
        return rated_power

    #Interpolation method 
    if interpolation_method == 'cubic':
        power_output = (wind_speed**3 / wind_speed_rated**3) * rated_power

    elif interpolation_method == 'linear':
        power_output = ((wind_speed - wind_speed_cut_in) / (wind_speed_rated - wind_speed_cut_in)) * rated_power

    return power_output



if __name__ == "__main__":
    wind_speed = 7.54  # Example wind speed in m/s
    interpolation_method = 'linear'  # Choose between 'linear' or 'cubic'

    result = power_output(wind_speed, interpolation_method=interpolation_method)

    print("Power output at wind speed of", wind_speed, "m/s is", round(result, 3), "MW using", interpolation_method, "interpolation.")




    