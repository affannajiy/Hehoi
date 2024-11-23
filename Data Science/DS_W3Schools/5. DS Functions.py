#Commonly used functions in Data Science are:
#min(), max(), sum(), avg(), count(), mean(), median(), mode(), std(), var()

#for this part in this chapter we will focus in min(), max(), mean().

#max()
#Definiton: Finds the hightest value in a list

Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print (Average_pulse_max)

#Expected Output: 125


#min()
#Definiton: Finds the lowest value in a list

Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print (Average_pulse_min)

#Expected Output: 80

#mean()
#Definiton: Finds the average value in a list

import numpy as np

Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
Average_calorie_burnage = np.mean(Calorie_burnage)

#We write np.mean so that we can use numpy functions

print(Average_calorie_burnage)

#Expected Output Calorie_burnage: 285.0