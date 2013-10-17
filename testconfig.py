#!/usr/bin/python

from Configuration import Configuration

c = Configuration("myconfig.txt", {"home": "Here", "text": "This is a test"})

c.set_new_param("One more")
c["other"] = "This is good!"

print("The param home = " + c.home)
print("The param name = " + c.name)
print("The param country = " + c["country"])
print("The param text = " + c.get_text())

print("-------")

for k in c:
    print(k + " = " + c[k])
    
print("-------")

print(str(c))

print("-------")

if 'new_param' in c:
    print("Found new_param")
if 'old_param' not in c:
    print("Not found old_param")
