class valueTooHighError(Exception):
    pass

class valueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

def test_value(x):
    if x> 100:
        raise valueTooHighError('value is too high')

try:
    test_value(200)
except valueTooHighError as e:
    print(e)