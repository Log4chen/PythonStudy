def func(x):
    return x + 1

def test_answer():
    print('test_answer')
    assert func(3) == 4
    assert func(3) == 5