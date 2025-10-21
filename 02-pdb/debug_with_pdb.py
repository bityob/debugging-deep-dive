def calculate_discount(price, discount_percent):
    breakpoint()
    final_price = price + (price * discount_percent / 100)
    return final_price

def main():
    price = 100
    discount = 20  # We expect final price to be 80
    print("Calculating discounted price...")
    result = calculate_discount(price, discount)
    print(f"Expected: 80 | Got: {result}")

if __name__ == "__main__":
    main()
