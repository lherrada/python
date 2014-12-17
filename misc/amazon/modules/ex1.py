#!/usr/bin/python

#It works!!!
import pack1.pack2.utilities
pack1.pack2.utilities.friends("Eliza")

#It works
from pack1.pack2 import utilities
utilities.friends("Eliza")

from pack1.pack2.utilities import friends
friends("Luisillo")

from .pack1 import relative

