# Mulch Calculator
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Purpose
To learn how to design, write, and test a simple Python program.
## _Scenario_
Premier Landscaping, a local area mulch delivery service, charges for mulch based on three factors: 
1. Cubic yards of mulch needed
2. Distance needed to travel to deliver the mulch
3. Sales tax due on the cost of the mulch

The unit measurement for mulch is a cubic yard (3 ft x 3 ft x 3 ft). The price of mulch is as follows:

| Cubic yards | Price per cubic yard |
| --- | --- |
| ≤ 5 | $36 per cubic yard (minimum order is 3 yards) |
| > 5 and ≤ 10 | $36 per cubic yard for the first 5 cubic yards plus<br>$33 per cubic yard for each cubic yard over 5 |
| > 10 | $36 per cubic yard for the first 5 cubic yards plus<br>$33 per cubic yard for each cubic yard over 5 up to 10 plus<br>$30 per cubic yard for each cubic yard over 10 |

## How to Calculate Cubic Yards
[length in feet * width in feet * (depth in inches / 12)] / 27

Equation:
$$
l * w * (d/12)/27
$$
> Example: a planting bed that is 20 feet long by 5 feet wide that requires 4 inches of mulch would be 1.23 cubic yards. (20 * 5 * 4 / 12) / 27 

## Distance
Delivery charge is $4.25 per mile. Minimum delivery charge is $35. This pays maintenance costs of your delivery truck and driver.
## Total Cost
Is the sum of the cost of the mulch, the cost of delivery and sales tax of 7% applied to cost of the mulch only.

## Example Output
<img src=img\mulch-one-bed.png />
<img src=img\mulch-multi-bed.png />
<img src=img\mulch-test.png />

## Test Cases to Consider
#### ====================> Test case 1 <====================
```` 
Mulch Calculator
=====================
Enter the length of the planting bed, in feet: 40
Enter the width of the planting bed, in feet: 8
Enter the desired depth of mulch, in inches: 4
Enter the dimensions for another planting bed (y/n): n

Total much required is approximately 4 cubic yards.

Enter your distance from Yorkville, IL, in miles: 25

Cost for 4 cubic yards of mulch
================================
          Mulch: $ 144.00
Delivery charge: $ 106.25
      Sales tax: $  10.08
     Total cost: $ 260.33 
````

#### ====================> Test case 2 <====================
````
Mulch Calculator
=====================

Enter the length of the planting bed, in feet: 20
Enter the width of the planting bed, in feet: 3
Enter the desired depth of mulch, in inches: 3
Enter the dimensions for another planting bed (y/n): n

Total much required is approximately 1 cubic yards.
The minimum mulch order is 3 cubic yards.

Enter your distance from Yorkville, IL, in miles: 8

Cost for 3 cubic yards of mulch
================================
          Mulch: $ 108.00
Delivery charge: $  35.00
      Sales tax: $   7.56
     Total cost: $ 150.56 
````

#### ====================> Test case 3 <====================
````
Mulch Calculator
=====================

Enter the length of the planting bed, in feet: 20
Enter the width of the planting bed, in feet: 3
Enter the desired depth of mulch, in inches: 3
Enter the dimensions for another planting bed (y/n): y

Enter the length of the planting bed, in feet: 10
Enter the width of the planting bed, in feet: 3
Enter the desired depth of mulch, in inches: 3
Enter the dimensions for another planting bed (y/n): n

Total much required is approximately 1 cubic yards.
The minimum mulch order is 3 cubic yards.

Enter your distance from Yorkville, IL, in miles: 29

Cost for 3 cubic yards of mulch
================================
          Mulch: $ 108.00
Delivery charge: $ 123.25
      Sales tax: $   7.56
     Total cost: $ 238.81 
````

#### ====================> Test case 4 <====================
````
Mulch Calculator
=====================

Enter the length of the planting bed, in feet: 50
Enter the width of the planting bed, in feet: 10
Enter the desired depth of mulch, in inches: 4
Enter the dimensions for another planting bed (y/n): y

Enter the length of the planting bed, in feet: 75
Enter the width of the planting bed, in feet: 20
Enter the desired depth of mulch, in inches: 4
Enter the dimensions for another planting bed (y/n): y

Enter the length of the planting bed, in feet: 15
Enter the width of the planting bed, in feet: 3
Enter the desired depth of mulch, in inches: 4
Enter the dimensions for another planting bed (y/n): n

Total much required is approximately 26 cubic yards.

Enter your distance from Yorkville, IL, in miles: 10

Cost for 26 cubic yards of mulch
================================
          Mulch: $ 825.00
Delivery charge: $  42.50
      Sales tax: $  57.75
     Total cost: $ 925.25 
````
