import pytest


def f():
    raise RuntimeError(1)

def test_mytest():

    with pytest.raises(RuntimeError) as res: # RaisesContext
        f()
    print('\r\n=============: ' + str(res._excinfo.__contains__(RuntimeError)))

def g(i: int):
    if(i == 1):
        raise TypeError('type error')
    else:
        raise ValueError('value error')

# python 3.11后支持 ExceptionGroup
# def test_exception_in_group():
#     with pytest.raises(ExceptionGroup) as err:
#         g(1)
#     assert err.group_contains(TypeError)
#     assert not err.group_contains(ValueError)

