# 1. Python is great for automating repetitive data tasks and handling massive files that would slow down or crash Excel. Excel is better for quick manual edits and making visual charts, but Python is much better for running automated data pipelines.
# 2. An online store tracking daily customer orders or login history would benefit from an append-mode log file. Append mode is the right tool because it safely adds new records to the bottom of the file every time without accidentally overwriting past data.
# Exercise 2
import csv

with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3
import csv

with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    
   
    header = next(reader)
    print("Header:", header)
    print("-" * 20)
    
    
    for row in reader:
        print(row)

# Exercise 4
import csv

total_revenue = 0

with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    
    for row in reader:
        # Skip empty rows or rows that don't have all 3 columns
        if not row or len(row) < 3:
            continue
            
        # Skip the header row safely
        if row[0].lower() == "product":
            continue
            
        try:
            # Access columns by positional index
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            
            line_total = price * quantity
            total_revenue += line_total
            
            # Print formatted line per product
            print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
        except ValueError:
            # Skip any rows that cannot be converted to numbers
            continue

print("-" * 40)
print(f"Total Revenue: ${total_revenue:.2f}")

# Excercise 5
import csv

input_file = "data/sales.csv"
output_file = "data/cleaned.csv"

original_count = 0
written_count = 0

with open(input_file, mode="r", encoding="utf-8", newline="") as infile:
    reader = csv.reader(infile)
    
    with open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
        fieldnames = ["Product", "Price", "Qty", "Total"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write the header row to cleaned.csv
        writer.writeheader()
        
        for row in reader:
            # Skip empty rows or malformed lines
            if not row or len(row) < 3:
                continue
                
            # Skip the header row from input
            if row[0].lower() == "product":
                continue
                
            try:
                original_count += 1
                product = row[0]
                price = float(row[1])
                qty = int(row[2])
                
                total = price * qty
                
                # Filter for orders with a total greater than $100
                if total > 100:
                    writer.writerow({
                        "Product": product,
                        "Price": f"{price:.2f}",
                        "Qty": qty,
                        "Total": f"{total:.2f}"
                    })
                    written_count += 1
            except ValueError:
                continue

print("Original rows:", original_count)
print("Rows written:", written_count)

# Excercise 6

# csv.reader is preferred for simple, fast scripts where column order is fixed and known.
# csv.DictReader is preferred for readability and safety, as displaying columns by name prevents errors if columns are reordered.


# Excercise 7
import csv
from datetime import datetime

total_revenue = 0
product_totals = {}

with open("data/sales.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Get values as a list (Column 0: Product, Column 1: Price, Column 2: Quantity)
        vals = list(row.values())
        if len(vals) < 3:
            continue
            
        product = str(vals[0]).strip()
        price_str = str(vals[1]).replace("$", "").replace(",", "").strip()
        qty_str = str(vals[2]).strip()
        
        try:
            price = float(price_str)
            quantity = int(float(qty_str))  # float() handles any ".0" decimals safely
        except ValueError:
            continue
            
        line_total = price * quantity
        total_revenue += line_total
        
        # Exercise 7: Accumulate product summary
        if product in product_totals:
            product_totals[product] += line_total
        else:
            product_totals[product] = line_total
            
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print("-" * 40)
print(f"Total Revenue: ${total_revenue:.2f}")

# Exercise 7: Print product summary sorted alphabetically
print("\nSales Summary by Product:")
print("-" * 40)
for prod in sorted(product_totals.keys()):
    print(f"{prod}: ${product_totals[prod]:.2f}")

# Exercise 8: Append to run log
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", mode="a", encoding="utf-8") as log_file:
    log_file.write(f"Run at {current_time} - Total Revenue: ${total_revenue:.2f}\n")

print(f"\nLogged successfully! Total Revenue: ${total_revenue:.2f}")