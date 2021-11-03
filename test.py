"""
The below code is commented out code as this has been refactored 
and used elsewhere just neater and easier to understand
"""
#def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided.
    """
    #print("Updating sales worksheet...\n")
    #sales_worksheet = SHEET.worksheet("sales")
    #sales_worksheet.append_row(data)
    #print("Sales worksheet updated successfully.\n")


#def update_surplus_worksheet(data):
    """
    Update surplus worksheet, add new row with the list data provided.
    """
    #print("Updating surplus worksheet...\n")
    #surplus_worksheet = SHEET.worksheet("surplus")
    #surplus_worksheet.append_row(data)
    #print("Surplus worksheet updated successfully.\n")
"""
The above code is commented out code as this has been refactored 
and used elsewhere just neater and easier to understand
"""









# MODEL SOLUTION TO THE CHALLENGE BELOW:


# student writes function
def get_stock_values(data):
    """
    Print out the calculated stock numbers for each sandwich type.
    """
    headings = SHEET.worksheet("stock").get_all_values()[0]

    # headings = SHEET.worksheet('stock').row_values(1)

    print("Make the following numbers of sandwiches for next market:\n")

    # new_data = {}
    # for heading, stock_num in zip(headings, data):
    #     new_data[heading] = stock_num
    # return new_data
    
    return {heading: data for heading, data in zip(headings, data)}
    
stock_values = get_stock_values(stock_data)
print(stock_values)
