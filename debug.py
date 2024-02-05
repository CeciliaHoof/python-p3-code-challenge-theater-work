import ipdb

from lib.audition import Audition
from lib.role import Role

r_1 = Role("Bryce")
r_2 = Role("Danika")

a_1 = Audition(r_1, "Sarah", "LA", "555-555-5555")
a_2 = Audition(r_2, "Sarah", "LA", "555-555-5555")
a_3 = Audition(r_1, "Cari", "LA", "555-555-5555")
a_4 = Audition(r_2, "Cari", "LA", "555-555-5555")

a_3.call_back()
a_1.call_back()

ipdb.set_trace()
