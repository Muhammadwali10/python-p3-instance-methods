#!/usr/bin/env python3

# Class body goes here
class Dog:
    # Instance method definition
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")


fido = Dog()
fido.bark()

snoopy = Dog()
snoopy.bark()


fido = Dog()
fido.sit()

snoopy = Dog()
snoopy.sit()
