from pytest import raises
from elfs_main import list_of_children, calculate_working_elfs, calculate_work_time, format_time, TooMuchL4ElfsError, NotEnoughElvesError, WrongAmountOfElfsError
from io import StringIO


def test_get_kids_from_file_handler():
    file_handler = StringIO('Kacper\nRobi\nKrzysztof')
    children_list = list_of_children(file_handler)
    assert children_list == ['Kacper', 'Robi', 'Krzysztof']


def test_calculate_working_elfs():
    assert calculate_working_elfs(3, 1) == 2


def test_calculate_working_elfs_error():
    with raises(TooMuchL4ElfsError):
        calculate_working_elfs(1, 3)


def test_calculate_working_elfs_error2():
    with raises(WrongAmountOfElfsError):
        calculate_working_elfs(-1, 0)


def test_calculate_work_time():
    assert calculate_work_time(1, 0, 2) == 60


def test_calculate_work_time2():
    assert calculate_work_time(1, 1, 3) == 60


def test_calculate_work_time3():
    assert calculate_work_time(1, 2, 3) == 60


def test_calculate_work_time4():
    assert calculate_work_time(1, 3, 3) == 90


def test_calculate_work_time5():
    assert calculate_work_time(5, 2, 10) == 90


def test_calculate_work_time6():
    assert calculate_work_time(5, 2, 6) == 120


def test_calculate_work_time7():
    assert calculate_work_time(1, 1, 10) == 60


def test_calculate_work_time8():
    assert calculate_work_time(0, 4, 4) == 30


def test_calculate_work_time9():
    assert calculate_work_time(0, 4, 2) == 60


def test_calculate_work_time10():
    assert calculate_work_time(0, 0, 0) == 0

def test_calculate_work_time11():
    minutes = calculate_work_time(6, 3, 3)
    assert minutes == 360
    assert format_time(minutes)

def test_calculate_work_time_error():
    with raises(NotEnoughElvesError):
        calculate_work_time(1, 3, 1)


def test_calculate_work_time_error2():
    with raises(NotEnoughElvesError):
        calculate_work_time(1, 1, 0)


def test_format_time_only_minutes():
    assert format_time(40) == (0, 0, 40)


def test_format_time_only_hours():
    assert format_time(120) == (0, 2, 0)


def test_format_time_only_days():
    assert format_time(2880) == (2, 0, 0)


def test_format_time():
    assert format_time(2943) == (2, 1, 3)


def test_format_time2():
    assert format_time(154) == (0, 2, 34)
