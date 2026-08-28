"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)
    


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    first, second, *remaining = each_wagons_id
    new_first , *new_remaining = remaining
    *correct_list, = new_first, *missing_wagons, *new_remaining, first, second
    return correct_list


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stops = []
    for stop in kwargs:
        stops.append(kwargs[stop])

    updated_routes = {**route, "stops": stops}
    return updated_routes


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    return {**route, **more_route_information}
    


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    first_row, second_row, third_row = wagons_rows
    updated_wagons = []
    for idx,row in enumerate(wagons_rows):
        updated_wagons.append([first_row[idx], second_row[idx], third_row[idx]])
    return updated_wagons