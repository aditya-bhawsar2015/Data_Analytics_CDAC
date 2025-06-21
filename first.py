#Array Properties
import numpy as np

sales = [0, 5, 155, 0 , 518, 616]
sales_array = np.array(sales)

print(type(sales_array))
print(f"ndim : {sales_array.ndim}")
print(f"shape : {sales_array.shape}")
print(f"size : {sales_array.size}")
print(f"dtype : {sales_array.dtype}")

#where() function

result_array = np.where(sales_array ==0, "No Sales", "some Sales")
print("Sales categorization (using where) : ",result_array)

# show all 

print(sales_array[sales_array != 0])