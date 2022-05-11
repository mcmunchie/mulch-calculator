import math

def get_cubic_yards():
    '''
    Prompt the user for the length in feet, width in feet and depth in inches.
    Assumes that the user enters integer values greater than 0 for all 3 values.
    Calculate the cubic yards (length x width X depth / 12 / 27) based on the input values.
    Return the cubic yards.
    '''
    length = int(input('Enter the length of the planting bed, in feet: '))
    width = int(input('Enter the width of the planting bed, in feet: '))
    depth = int(input('Enter the depth of the planting bed, in inches: '))

    cubic_yards = length * width * (depth / 12) / 27

    return cubic_yards

def calculate_mulch_cost(cubic_yards):
    '''
    Calculate cost of the mulch based on the cubic yards being ordered.
    Cubic yards	    Cost per cubic yard
    -----------     --------------------------------------------------
    <= 5            $36 per cubic yard (minimum order is 3 yards)

    > 5 and <= 10   $36 per cubic yard for the first 5 cubic yards plus
                    $33 per cubic yard for each cubic yard over 5

    > 10            $36 per cubic yard for the first 5 cubic yards plus
                    $33 per cubic yard for each cubic yard over 5 up to 10 plus
                    $30 per cubic yard for each cubic yard over 10
    '''
    cost = 0.0

    if cubic_yards <= 5:
        cost = cubic_yards * 36
    else:
        if cubic_yards <= 10:
            cost = (cubic_yards - 5) * 33 + 5 * 36
        else:
            cost = (cubic_yards - 10) * 30 + 5 * 33 + 5 * 36

    return cost

def main():
    '''
    Compute the cost of mulch based on the size of each plantng bed entered by the user.
    The customer can enter the dimensions for more than one planting bed.
    The total mulch for all planting beds should be rounded up to the next cubic foot before
    calculating the total cost of the mulch and applicable sales tax.
    The mulch cost, sales tax, delivery charge and total cost is displayed to the user.
    '''
    total_cubic_yards = 0.0
    print()
    print("Mulch Calculator")
    print("=====================")
    print()

    keep_going = 'y'
    while keep_going == 'y':
        cubic_yards = get_cubic_yards()
        total_cubic_yards += cubic_yards
        keep_going = input(
            'Enter the dimensions for another planting bed (y/n): ')
        print()

    total_cubic_yards = math.ceil(total_cubic_yards)

    if total_cubic_yards < 3:
        print("Minimum order is 3 cubic yards.")
        total_cubic_yards = 3
    print("Total mulch required is approximately", format(
        total_cubic_yards, '.0f'), "cubic yards.")
    print()
    distance = float(
        input('Enter your distance from Yorkville, IL, in miles: '))
    print()

    delivery_charge = distance * 4.25

    if delivery_charge < 35:
        delivery_charge = 35
    mulch_cost = calculate_mulch_cost(total_cubic_yards)
    sales_tax = mulch_cost * .07
    total_cost = mulch_cost + sales_tax + delivery_charge

    print("Cost for", format(total_cubic_yards, '.0f'), "cubic yards of mulch")
    print("================================")
    print("\t  Mulch: $", format(mulch_cost, '.2f'))
    print("Delivery charge: $", format(delivery_charge, '.2f'))
    print("      Sales tax: $", format(sales_tax, '.2f'))
    print("     Total cost: $", format(total_cost, '.2f'))
    print("\nThank you for choosing Premier Landscaping!")
    print()

if __name__ == "__main__":
    main()
