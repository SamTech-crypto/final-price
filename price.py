# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied, return original price

# Prompt user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Check if price and discount are valid (positive numbers)
    if original_price <= 0 or discount < 0:
        print("Price and discount must be positive values.")
    else:
        # Call the function and store the result
        final_price = calculate_discount(original_price, discount)

        # Print the result
        if final_price != original_price:
            print(f"Discount applied. Final price: ${final_price:.2f}")
        else:
            print(f"No discount applied. The price remains: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
