from time import strftime, localtime


def current_time(strftime_format):
    return strftime(strftime_format, localtime())
