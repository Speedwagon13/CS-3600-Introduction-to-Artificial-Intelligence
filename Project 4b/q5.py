import NeuralNet
import Testing

accuraciesPen = []

for i in range(5):
    print "Pen iteration: " + str(i + 1)
    accuraciesPen.append(Testing.testPenData()[1])

print "max: " + str(max(accuraciesPen))
print "average: " + str(Testing.average(accuraciesPen))
print "standard deviation: " + str(Testing.stDeviation(accuraciesPen))

accuraciesCar = []

for i in range(5):
    print "Car iteration: " + str(i + 1)
    accuraciesCar.append(Testing.testCarData()[1])

print "max: " + str(max(accuraciesCar))
print "average: " + str(Testing.average(accuraciesCar))
print "standard deviation: " + str(Testing.stDeviation(accuraciesCar))

print "----Final Stats----\n"
print "Pen\n"
print "max: " + str(max(accuraciesPen))
print "average: " + str(Testing.average(accuraciesPen))
print "standard deviation: " + str(Testing.stDeviation(accuraciesPen))
print "\nCar"
print "max: " + str(max(accuraciesCar))
print "average: " + str(Testing.average(accuraciesCar))
print "standard deviation: " + str(Testing.stDeviation(accuraciesCar))
