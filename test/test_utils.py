from time import strftime, localtime, sleep

from nephelaiio.utils import config


def test_config():
    time_string_a = strftime(config['utils']['time_format'], localtime())
    sleep(1)
    time_string_b = strftime(config['utils']['time_format'], localtime())
    assert time_string_a != ''
    assert time_string_b != ''
    assert time_string_a != time_string_b
