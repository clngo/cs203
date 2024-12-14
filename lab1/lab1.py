class Flower:
 # Common base class for all Flowers
    def __init__(self, petalName, petalNumber, petalPrice):
        self.name = petalName
        self.petals = petalNumber
        self.price = petalPrice
    def setName(self, petalName):
         self.name = petalName

    def setPetals(self, petalNumber):
         self.petals = petalNumber

    def setPrice(self, petalPrice):
         self.price = petalPrice

    def getName(self):
      return self.name

    def getPetals(self):
      return self.petals

    def getPrice(self):
      return self.price

#This would create first object of Flower class
f1 = Flower("Sunflower", 2, 1000)
print ("Flower Details:")
print ("Name: ", f1.getName())
print ("Number of petals:", f1.getPetals())
print ("Price:",f1.getPrice())
print ("\n")

#This would create second object of Flower class
f2 = Flower("Rose", 5, 2000)
f2.setPrice(3333)
f2.setPetals(6)
print ("Flower Details:")
print ("Name: ", f2.getName())
print ("Number of petals:", f2.getPetals())
print ("Price:",f2.getPrice())

class Product:
 def __init__(self, n:str, a:int, p:int):
  self.name = n
  self.amount = a
  self.price = p

 def get_price(self, buyingg):
  cost = buyingg * self.price
  if buyingg >= 10 and buyingg <= 99:
   return cost * .9
  if buyingg >= 100:
   return cost * .8
  else:
   return cost

 def make_purchase(self, buying):
  return self.amount - buying

class Converter:
 def __init__(self, l: int, u: str):
  self.length = l
  self.unit = u

 def inch(self):
  if self.unit == "inch":
      return self.length
  if self.unit == "foot":
      return self.length * 12
  if self.unit == "yard":
      return self.length * 36
  if self.unit == "mile":
      return self.length * 63360
  if self.unit == "meter":
      return self.length * 39.37
  if self.unit == "kilometer":
      return self.length * 1000 * 39.37
  if self.unit == "centimeter":
      return self.length * 39.37 / 100
  if self.unit == "millimeter":
      return self.length * 39.37 / 1000

 def foot(self):
    if self.unit == "foot":
        return self.length
    if self.unit == "inch":
        return self.length * 12
    if self.unit == "yard":
        return self.length / 3
    if self.unit == "mile":
        return self.length / 5280
    if self.unit == "meter":
        return self.length / 3.280839895
    if self.unit == "kilometer":
        return self.length / 1000 / 3.280839895
    if self.unit == "centimeter":
        return self.length * 100 / 3.280839895
    if self.unit == "millimeter":
        return self.length * 1000 * 3.280839895

 def yard(self):
        if self.unit == "yard":
            return self.length
        if self.unit == "inch":
            return self.length * 36
        if self.unit == "foot":
            return self.length * 3
        if self.unit == "mile":
            return self.length / 1760
        if self.unit == "meter":
            return self.length * 1.09361
        if self.unit == "kilometer":
            return self.length * 1.09361 * 1000
        if self.unit == "centimeter":
            return self.length * 1.09361 / 100
        if self.unit == "millimeter":
            return self.length * 1.09361 / 1000

 def mile(self):
     if self.unit == "mile":
         return self.length
     if self.unit == "inch":
         return self.length / 63360
     if self.unit == "foot":
         return self.length / 5280
     if self.unit == "yard":
         return self.length / 1760
     if self.unit == "meter":
         return self.length / 1609.344
     if self.unit == "kilometer":
         return self.length / 1.609344
     if self.unit == "centimeter":
         return self.length / 160934.4
     if self.unit == "millimeter":
         return self.length / 1609344

 def meter(self):
     if self.unit == "meter":
         return self.length
     if self.unit == "inch":
         return self.length / 39.37007874
     if self.unit == "foot":
         return self.length * 0.3048
     if self.unit == "yard":
         return self.length * 0.9144
     if self.unit == "mile":
         return self.length * 1609.344
     if self.unit == "kilometer":
         return self.length * 1000
     if self.unit == "centimeter":
         return self.length / 100
     if self.unit == "millimeter":
         return self.length / 1000

 def kilometer(self):
     if self.unit == "kilometer":
         return self.length
     if self.unit == "inch":
         return self.length / 39.37007874 / 1000
     if self.unit == "foot":
         return self.length * 0.3048 / 1000
     if self.unit == "yard":
         return self.length * 0.9144 / 1000
     if self.unit == "mile":
         return self.length * 1.609344
     if self.unit == "meter":
         return self.length / 1000
     if self.unit == "centimeter":
         return self.length / 100000
     if self.unit == "millimeter":
         return self.length / 1000000

 def centimeter(self):
     if self.unit == "centimeter":
         return self.length
     if self.unit == "inch":
         return self.length / 39.37007874 * 100
     if self.unit == "foot":
         return self.length * 0.3048 * 100
     if self.unit == "yard":
         return self.length * 0.9144 * 100
     if self.unit == "mile":
         return self.length * 1609.344 * 100
     if self.unit == "kilometer":
         return self.length * 1000 * 100
     if self.unit == "meter":
         return self.length * 100
     if self.unit == "millimeter":
         return self.length / 1000 * 100

 def millimeter(self):
     if self.unit == "millimeter":
         return self.length
     if self.unit == "inch":
         return self.length / 39.37007874 * 1000
     if self.unit == "foot":
         return self.length * 0.3048 * 1000
     if self.unit == "yard":
         return self.length * 0.9144 * 1000
     if self.unit == "mile":
         return self.length * 1609.344 * 1000
     if self.unit == "kilometer":
         return self.length * 1000 * 1000
     if self.unit == "meter":
         return self.length * 1000
     if self.unit == "centimeter":
         return self.length / 1000 * 1000
