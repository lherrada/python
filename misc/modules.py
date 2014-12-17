#!/usr/bin/python
import mypackage.module1.mod1
mypackage.module1.mod1.modulo1("LHM")

from mypackage.module1.mod1 import modulo1
modulo1("SHM")

from mypackage.module1 import mod1
mod1.modulo1("LeHM")

from mypackage.module2 import * 
mod2.modulo2("Mechita")
