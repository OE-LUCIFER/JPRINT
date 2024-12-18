from jprinter import jp
from jprinter import jprint

def name(r):
    jp(r)
    return r

def name2(r):
    jprint(r)
    return r
    
x = 10
jp("Hello, world!", prefix="DEBUG -> ")
name("vortex")
name2("vortex2")
jp(x)
jp(x, "hello")
jp(123)

