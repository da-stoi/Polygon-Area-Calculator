import math
#Getting your minimum, maximum, and side length.
min = input('What is the minimum # of sides?\n')
max = input('What is the maximum # of sides?\n')
sideLength = input('What is the side length?\n')

min = int(float(min))
max = int(float(max))
sideLength = int(sideLength)

if min < 3 :
  print('Invalid minimum ammount. Must be greater than or equal to 3')
elif max < min :
  print('Invalid maximum ammount. Must be greater than or equal to your minimum amount of',min)
elif sideLength <= 0 :
  print ('Invalid side length. Must be greater than 0')
else :

  print('Your minimum is:',min)
  print('Your maximum is:',max)
  print('Your side length is:',sideLength)
  print ('Starting...')

  for x in range(min, max+1):
    singleAngleInt = ((x-2)*180)/x
    singleAngleCenter = 180-singleAngleInt
  
    singleTriangleHeight = ((sideLength/2)/(math.tan(math.radians(singleAngleCenter/2))))
  
    halfSingleArea = ((sideLength/2)*(singleTriangleHeight))
    totalArea = halfSingleArea*x

    print ('~~~~~~~~~~~~~~~~~~~~~ ',x,'-gon ~~~~~~~~~~~~~~~~~~~~~')
    print ('The interior angle of a',x,'-gon is: ',round(singleAngleInt, 2))
    print ('The center angle of a',x,'-gon is: ',round(singleAngleCenter, 2))
    print ('The total area of a',x,'-gon with a side length of',sideLength,'is: ', round(totalArea, 2))
    print ('')

  print ('~~~~~~~~~~~~~~~~~~~~~~-= End =-~~~~~~~~~~~~~~~~~~~~~~')
