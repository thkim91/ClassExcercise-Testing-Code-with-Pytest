def cal_number_of_seconds(time_period, unit):
    unit_list = ['second', 'minute', 'hour', 'day', 'week', 'month', 'year']
    if unit in unit_list:
        if unit == 'second':
            return time_period
        elif unit == 'minute':
            return time_period * 60
        elif unit == 'hour':
            return time_period * 60 * 60
        elif unit == 'day':
            return time_period * 60 * 60 * 24
        elif unit == 'week':
            return time_period * 60 * 60 * 24 * 7
        elif unit == 'month':
            return time_period * 60 * 60 * 24 * 30
        elif unit == 'year':
            return time_period * 60 * 60 * 24 * 365

    else:
        return "sorry, we do not accept your unit"
