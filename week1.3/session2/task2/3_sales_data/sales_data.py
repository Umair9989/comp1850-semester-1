import csv
from collections import defaultdict


def analyze_sales_data(file_path):
    # Initialize variables for core statistics
    max_sale_amount = -1
    max_sale_date = None
    total_sales_amount = 0
    row_count = 0

    # Dictionaries for tracking product sales (Widget: Total Units Sold)
    product_units_sold = defaultdict(int)
    product_total_sales_value = defaultdict(float)

    # Dictionaries for regional analysis
    region_sales_amount = defaultdict(float)
    # Nested dictionary: {Region: {Product: Units Sold}}
    region_product_units = defaultdict(lambda: defaultdict(int))

    try:
        # Open and read the CSV file
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    # Extract and clean data from the row
                    date = row["Date"]
                    product = row["Product"]
                    # Convert sales amount (handling potential string formatting)
                    sales_amount = float(row["Sales_Amount"])
                    units_sold = int(row["Units_Sold"])
                    region = row["Region"]

                    # 1. Track largest sale day
                    if sales_amount > max_sale_amount:
                        max_sale_amount = sales_amount
                        max_sale_date = date

                    # 2. Accumulate values for average sale amount
                    total_sales_amount += sales_amount
                    row_count += 1

                    # 3. Track widget units sold overall
                    product_units_sold[product] += units_sold
                    product_total_sales_value[product] += sales_amount

                    # 4. Regional statistics
                    region_sales_amount[region] += sales_amount
                    region_product_units[region][product] += units_sold

                except (ValueError, KeyError) as e:
                    # Skip malformed rows safely
                    print(f"Warning: Skipping invalid row {row}: {e}")
                    continue

    except FileNotFoundError:
        print(
            f"Error: The file '{file_path}' could not be found. Please check the path."
        )
        return
    except PermissionError:
        print(
            f"Error: Permission denied when trying to read '{file_path}'."
        )
        return

    # Check if we actually processed any valid data
    if row_count == 0:
        print("No valid data found in the CSV file.")
        return

    # Calculate final core aggregates
    average_sale = total_sales_amount / row_count
    most_sold_widget = max(product_units_sold, key=product_units_sold.get)

    # --- PRINT RESULTS IN A NICE, HUMAN-READABLE FORMAT ---
    print("=" * 50)
    print("SALES DATA ANALYSIS REPORT ")
    print("=" * 50)

    print("\n Core Statistics:")
    print(f"  • Largest Sale Day:    {max_sale_date} (${max_sale_amount:,.2f})")
    print(f"  • Average Sale Amount: ${average_sale:,.2f}")
    print(
        f"  • Top Selling Widget:  {most_sold_widget} ({product_units_sold[most_sold_widget]:,} units sold)"
    )

    print("\n Regional Performance:")
    for region, total_sales in region_sales_amount.items():
        # Find the top widget for this specific region
        regional_products = region_product_units[region]
        top_regional_widget = max(regional_products, key=regional_products.get)
        top_regional_units = regional_products[top_regional_widget]

        print(f"  Region: {region}")
        print(f"    - Total Revenue:    ${total_sales:,.2f}")
        print(
            f"    - Most Sold Widget: {top_regional_widget} ({top_regional_units:,} units)"
        )

    print("\n Total Sales Per Widget:")
    for widget, units in product_units_sold.items():
        revenue = product_total_sales_value[widget]
        print(
            f"  • {widget}: {units:,} units sold | Total Revenue: ${revenue:,.2f}"
        )

    print("=" * 50)


# Run the script
if __name__ == "__main__":
    analyze_sales_data("sales.csv")
