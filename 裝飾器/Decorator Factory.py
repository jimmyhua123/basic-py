from types import MappingProxyType


def myDeco(cb):
    def run():
        print('hello here')
        cb()
    return run

@myDeco
def test():
    print("hello again")

test()
