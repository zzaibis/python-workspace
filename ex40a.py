class MyStuff(object):
    def __init__(self) -> None:
        self.tangerine = 'Some Text'
    
    def apple(self):
        print('I am a classy apple')


thing = MyStuff()
thing.apple()
print(thing.tangerine)