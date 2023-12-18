import csv

# Step 1: Read in menu_data.csv
menu_data = []  # Initialize an empty menu list object
menu_file_path = "/Users/helobonetti/Desktop/BERKELEY/python-homework/PyRamen/menu_data.csv"
with open(menu_file_path, newline="") as menu_file:
    # Use the reader function to read menu_data.csv
    menu_reader = csv.reader(menu_file)

    # Use the next function to skip the header (first row of the CSV)
    next(menu_reader)

    # Loop over the rest of the rows and append every row to the menu list object
    for row in menu_reader:
        menu_data.append(row)

# Step 2: Read in sales_data.csv
sales_data = []  # Initialize an empty sales list object
sales_file_path = "/Users/helobonetti/Desktop/BERKELEY/python-homework/PyRamen/sales_data.csv"
with open(sales_file_path, newline="") as sales_file:
    # Use the reader function to read sales_data.csv
    sales_reader = csv.reader(sales_file)

    # Use the next function to skip the header (first row of the CSV)
    next(sales_reader)

    # Loop over the rest of the rows
    for row in sales_reader:
        # Check if 'Quantity' is a valid integer
        try:
            quantity = int(row[1])
        except ValueError:
            print(f"Invalid value for Quantity: {row[1]}. Replacing with default quantity (0).")
            quantity = 0  # Set a default value or choose another strategy

        sales_item = row[4]


# Step 3: Initialize an empty report dictionary
report = {}

# Create a dictionary to map menu items to their corresponding price and cost
menu_dict = {menu_row[0]: {"price": float(menu_row[3]), "cost": float(menu_row[4])} for menu_row in menu_data}

# Loop through every row in the sales list object
for row in sales_data:
    # Set variables for Quantity and Menu_Item
    try:
        quantity = int(row[1])
    except ValueError:
        print(f"Invalid value for Quantity: {row[1]}. Skipping this field.")
        quantity = 0  # Set a default value or choose another strategy

    sales_item = row[4]

    # Check if sales_item is already in the report dictionary
    if sales_item not in report:
        # Initialize key-value pairs for the sales_item
        report[sales_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }

    # Check if sales_item is in the menu_dict
    if sales_item in menu_dict:
        # Access price and cost directly from the menu_dict
        price = menu_dict[sales_item]["price"]
        cost = menu_dict[sales_item]["cost"]

        # Calculate profit for each item
        profit = price - cost

        # Cumulatively add values to the corresponding metrics in the report
        report[sales_item]["01-count"] += quantity
        report[sales_item]["02-revenue"] += price * quantity
        report[sales_item]["03-cogs"] += cost * quantity
        report[sales_item]["04-profit"] += profit * quantity
    else:
        print(f"{sales_item} does not exist in the menu data! NO MATCH!")

# Write out the contents of the report dictionary to a text file
output_file_path = "/Users/helobonetti/Desktop/BERKELEY/python-homework/PyRamen/output_report.txt"
with open(output_file_path, "w") as output_file:
    for ramen_type, metrics in report.items():
        output_line = f"{ramen_type} {metrics}\n"
        output_file.write(output_line)
        print(output_line.strip())
