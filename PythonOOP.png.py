# Hi! My name is Tyairah Flowers
# Date: July 20, 2025
# I am learning how to use Python to create flowers using Object-Oriented Programming (OOP)
# This code shows how to make pretend flowers that can grow and bloom:)

# Making a flower blueprint (called a class)
class Flower:
    # This part helps us make a flower and give it a name
    def __init__(self, name):
        self.name = name  # This is the flower's name (like Hibiscus or Lavender)

    # This is what the flower does when it grows
    def grow(self):
        print(self.name + " is growing.")

    # This is what the flower does when it blooms (opens up)
    def bloom(self):
        print(self.name + " is blooming.")


# Let's make 2 flowers using our blueprint!

hibiscus = Flower("Hibiscus")    # Making a flower named Hibiscus
lavender = Flower("Lavender")    # Making a flower named Lavender

# Now let’s tell them to grow and bloom

hibiscus.grow()      # Hibiscus is growing.
hibiscus.bloom()     # Hibiscus is blooming.

lavender.grow()      # Lavender is growing.
lavender.bloom()     # Lavender is blooming.
