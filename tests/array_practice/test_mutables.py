from arrays_practice import MutableArray


def test_mutable_array():
    array = MutableArray()
    array += [2, 2, 2, 2, 1, 1, 1, 1]

    assert array.capacity() == 16
    assert not array.is_empty()

    array.remove(1)
    assert array.capacity() == 8
    array.remove(2)
    assert array.capacity() == 2

    array.append(1)
    assert array[0] == 1

    array.insert(0, 123)
    assert (array[0], array[1]) == (123, 1)
    assert array.at(0) == 123
    assert array.at(1) == 1

    array.prepend("string")
    assert array[0] == "string"
    assert array[1] == 1

    array.delete(0)
    assert array[0] == 1

    array.push(1)
    assert (array[0], array[1]) == (1, 1)
    assert array.find(1) == 0

    assert array.size() == 2
    assert array.pop() == 1
    assert array.size() == 1
    assert array[0] == 1


