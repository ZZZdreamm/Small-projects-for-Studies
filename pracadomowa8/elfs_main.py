import sys
import argparse
from datetime import timedelta

MINUTES_IN_DAY = 1440
MINUTES_IN_HOUR = 60
MINUTES_TO_MAKE_PRESENT = 60
MINUTES_TO_MAKE_STICK = 30


class TooMuchL4ElfsError(Exception):
    def __init__(self):
        super().__init__('There cannot be more elfs on eLf4 than elfs')


class NotEnoughElvesError(Exception):
    def __init__(self):
        super().__init__('There is not enough elves to make presents for good kids')


class WrongAmountOfElfsError(Exception):
    def __init__(self):
        super().__init__('There has to be at least one elf working')


def list_of_children(file_handle):
    children = [row.strip() for row in file_handle]
    return children


def calculate_work_time(presents, sticks, available_elfs):
    minutes_working = 0
    if ((presents != 0 and available_elfs < 2) or ((presents != 0 or sticks != 0) and available_elfs == 0)):
        raise NotEnoughElvesError()
    presents_to_do = presents
    sticks_to_do = sticks
    all_items_to_do = presents_to_do + sticks_to_do
    while all_items_to_do > 0:
        presents_done = min(available_elfs // 2, presents_to_do)
        presents_elfs = presents_done * 2
        elfs_for_sticks = available_elfs - presents_elfs
        sticks_done = min((elfs_for_sticks) * 2, sticks_to_do)
        presents_to_do -= presents_done
        sticks_to_do -= sticks_done

        if (presents_done != 0 or sticks_done > elfs_for_sticks):
            minutes_working += MINUTES_TO_MAKE_PRESENT
        else:
            minutes_working += MINUTES_TO_MAKE_STICK
        all_items_to_do = presents_to_do + sticks_to_do

    return minutes_working


def format_time(all_minutes):
    days = all_minutes // MINUTES_IN_DAY
    hours = (all_minutes % MINUTES_IN_DAY) // MINUTES_IN_HOUR
    minutes = (all_minutes % MINUTES_IN_DAY) % MINUTES_IN_HOUR
    return (days, hours, minutes)


def calculate_working_elfs(village_elfs, elf4_elfs):
    if (village_elfs < 0 or elf4_elfs < 0):
        raise WrongAmountOfElfsError()
    if (elf4_elfs > village_elfs):
        raise TooMuchL4ElfsError()
    return village_elfs - elf4_elfs


def return_time_string(days, hours, minutes):
    return_string = f'Time needed to prepare Christmas: {days} days, {hours} hours and {minutes} minutes'
    return return_string


def main(arguments):

    parser = argparse.ArgumentParser()
    parser.add_argument('good_children_list', type=str)
    parser.add_argument('bad_children_list', type=str)
    parser.add_argument('village_elfs_number', type=int)
    parser.add_argument('--elf4-elfs-number', type=int, default=0)
    args = parser.parse_args(arguments[1:])

    with open(args.good_children_list, 'r') as file_handle:
        good_children = list_of_children(file_handle)

    with open(args.bad_children_list, 'r') as file_handle:
        bad_children = list_of_children(file_handle)

    village_elfs = args.village_elfs_number
    elf4_elfs = args.elf4_elfs_number

    number_presents = len(good_children)
    number_sticks = len(bad_children)

    working_elfs = calculate_working_elfs(village_elfs, elf4_elfs)
    work_time = calculate_work_time(
        number_presents, number_sticks, working_elfs)
    days, hours, minutes = format_time(work_time)

    print(return_time_string(days, hours, minutes))
    return (number_presents, number_sticks, days, hours, minutes)


if __name__ == "__main__":
    main(sys.argv)