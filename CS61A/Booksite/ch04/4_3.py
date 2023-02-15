# 4.3.4   Interpreting SQL


def demo_1():
    """
    >>> from collections import namedtuple
    >>> CitiesRow = namedtuple("Row", ["latitude", "longitude", "name"])
    >>> cities = [CitiesRow(38, 122, "Berkeley"),
    ...               CitiesRow(42,  71, "Cambridge"),
    ...               CitiesRow(43,  93, "Minneapolis")]
    ... 
    >>> cities
    [Row(latitude=38, longitude=122, name='Berkeley'), Row(latitude=42, longitude=71, name='Cambridge'), Row(latitude=43, longitude=93, name='Minneapolis')]
    >>> 
    >>> DistancesRow = namedtuple("Row", ["name", "distance"])
    >>> def select(cities_row):
    ...         latitude, longitude, name = cities_row
    ...         return DistancesRow(name, 60*abs(latitude-38))
    ...
    >>> distances = list(map(select, cities))
    >>> for row in distances:
    ...         print(row)
    ...
    Row(name='Berkeley', distance=0)
    Row(name='Cambridge', distance=240)
    Row(name='Minneapolis', distance=300)
    >>>
    >>> from sql_interpreter import Select
    >>> env = {"cities": cities}
    >>> select = Select("name, 60*abs(latitude-38) as distance","cities", "name != 'Berkeley'", "-longitude")
    >>> for row in select.execute(env):
    ...     print(row)
    ...
    Row(name='Minneapolis', distance=300)
    Row(name='Cambridge', distance=240)
    >>>
    >>> env["distances"] = list(select.execute(env))
    >>> joined = Select("cities.name as name, distance, longitude", "cities, distances",
    ...                "cities.name == distances.name", None)
    ...
    >>> for row in joined.execute(env):
    ...     print(row)
    ...
    Row(name='Cambridge', distance=240, longitude=71)
    Row(name='Minneapolis', distance=300, longitude=93)
    """
    pass
