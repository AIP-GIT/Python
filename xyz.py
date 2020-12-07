#Give a list of weight and value pairs  for items and a bag with capacity.Calculate the maximum item value that can be carried in the bag . 
#NotItems can be carried in parts/fraction.                    Input:…………. Items as (value , weight) pairs     , 
Items =[(60,10), (100,20),(120,30)]                      
xyz=[(a/b,b) for a,b in Items]
xyz.sort(reverse=True,key=lambda xyz:xyz[0])

total=0
capacity=50
print(xyz)
#xyz=0
for item in xyz:
  if item[1] <=capacity:
    total=total+item[0]*item[1]#60 ,140
    capacity=capacity-item[1]
  else:
    total=total+item[0]*capacity#140+4.0*20=240
    break
print(total)


#Take two list of numbers of products quantities and prices and calculate total price.Use list comprehension and aggregartion .
#Input: product_quantities = [13,5,6,10,11] ; 
#prices = [1.2 , 6.5,1.0,4.8,5.0]  
#output : Total = 157.1
product_quantities = [13,5,6,10,11]
prices = [1.2 , 6.5,1.0,4.8,5.0]
p=sum([a*b for a,b  in zip(product_quantities,prices)])
print(p)

