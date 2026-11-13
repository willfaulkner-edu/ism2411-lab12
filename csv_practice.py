# 1. Python is great for automating repetitive data tasks and handling massive files that would slow down or crash Excel. Excel is better for quick manual edits and making visual charts, but Python is much better for running automated data pipelines.
# 2. An online store tracking daily customer orders or login history would benefit from an append-mode log file. Append mode is the right tool because it safely adds new records to the bottom of the file every time without accidentally overwriting past data.
# Exercise 2
import csv
import datetime

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
        
        if not row or len(row) < 3:
            continue
            
        
        if row[0].lower() == "product":
            continue
            
        try:
            
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            
            line_total = price * quantity
            total_revenue += line_total
            
            
            print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
        except ValueError:
           
            continue

print("-" * 40)
print(f"Total Revenue: ${total_revenue:.2f}")

# Exercise 5
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
        
        
        writer.writeheader()
        
        for row in reader:
            
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

# Exercise 6

total_revenue = 0

with open("data/sales.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print("-" * 40)
print(f"Total Revenue: ${total_revenue:.2f}")

# 1. csv.reader is preferred for simple, fast scripts where column order is fixed and known.
# 2. csv.DictReader is preferred for readability and safety, as displayingcolumns by name prevents errors if columns are reordered.

# Exercise 7
product_totals = {}

with open("data/sales.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        
        
        if product in product_totals:
            product_totals[product] += line_total
        else:
            product_totals[product] = line_total


for prod in sorted(product_totals.keys()):
    print(f"{prod}: ${product_totals[prod]:.2f}")
# Exercise 8
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", mode="a", encoding="utf-8") as log_file:
    log_file.write(f"Run at {current_time} - Total Revenue: ${total_revenue:.2f}\n")

print(f"Logged successfully! Total Revenue: ${total_revenue:.2f}")
