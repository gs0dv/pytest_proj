from utils import arrs


def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(array_fixture, end=1) == [1]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(array_fixture, -2) == [3, 4]
    assert arrs.my_slice(array_fixture, -3, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, -30, 3) == [1, 2, 3]