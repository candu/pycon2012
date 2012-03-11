def bar(self):
    self.x += 1
    return self.x

Foo = type('Foo', (object,), {'bar' : bar, 'x': 0})

foo = Foo()
for i in range(3):
    print foo.bar()

def baz(self):
    self.x -= 1
    return self.x

import new
foo_baz = new.instancemethod(baz, foo, Foo)
for i in range(3):
    print foo_baz()
