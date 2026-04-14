from ..utils import distance
import xarray as xr
import ddeq


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: "Point", p2: "Point") -> None:
        self.p1 = p1
        self.p2 = p2

    def length(self) -> float:
        return distance(self.p1, self.p2)


def any_funtion(x: int) -> int:
    """Ad a function with a lot of typoos in the name and docstring"""
    if x == 0:
        return 0
    return x * 2


def use_xarray(data_path: str) -> xr.Dataset:
    return xr.open_dataset(data_path)


def use_ddeq(r: float):
    return ddeq.misc.create_disk(r)
