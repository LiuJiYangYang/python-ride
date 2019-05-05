
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000',base=10))

int2=functools.partial(int,base=2)
print(int2)
max2=functools.partial(max,10)
max2(5,6,7)

args=(10,5,6,7)
print(max(*args))

import functools

int('12345', base=8)
int2 = functools.partial(int, base=8)

max2 = functools.partial(max, 10)
max2(5, 6, 7)



