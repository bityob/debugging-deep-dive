def sanitize(quantity):
    # ❌ Bug: treats 0 as falsy and turns it into 1
    return quantity or 1

def total(price, quantity):
    q = sanitize(quantity)     # bug is hiding here
    return price * q
    
price = 100
quantity = 0
result = total(price, quantity)
print(f"Total = {result}")  # Expected 0, got 100