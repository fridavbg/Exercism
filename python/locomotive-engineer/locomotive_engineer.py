"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def flatten(lst):
    """
    Function to flatten a list
    """
    all_wagons = []

    for id in lst:
        if isinstance(id, list):
            all_wagons.extend(flatten(id))
        else:
            all_wagons.append(id)
    return all_wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    all_wagons = []

    first_two_wagons = each_wagons_id[0:2]
    first_wagon = each_wagons_id[2]
    remaining_wagons = each_wagons_id[3:len(each_wagons_id)]
    all_wagons.append(first_wagon)
    all_wagons.append(missing_wagons)
    all_wagons.append(remaining_wagons)
    all_wagons.append(first_two_wagons)

    return flatten(all_wagons)

def add_missing_stops():
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    pass


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    pass


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    pass

# print('1: [1, 7, 12, 3, 14, 8, 5]')
# print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))


print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))
print('2 : [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]')
