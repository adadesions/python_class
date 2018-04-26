"""
    tuple == list that can't modify or update  
    tuple = ()
"""

fruit = ('apple', 'apple', 'orange')
print(fruit)

face_landmark = [
    (0, 0),
    (1, 5),
    (43, 9)
]
print(face_landmark)

stock = (0.5, 4, 2.5, 3.2)
mean_stock = 0
for price in stock:
    mean_stock = mean_stock + price 
mean_stock = mean_stock/len(stock)
print('Price for tmr:', mean_stock)