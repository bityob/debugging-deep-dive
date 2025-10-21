def apply_discount(price, discount):
    final_result = price - discount
    return final_result

test_cases = [100, 75, 5]

for case in test_cases:
    result = apply_discount(case, 20)
    print(f"Before: {case=}, After={result=}")