number = int(input("Enter your investment plan: "))
year = 1
while year <= 30:
    investment_plan = number * (1 + 0.10) ** year
    increase_rate = 0.10 * investment_plan

    print(f"your investment is now {increase_rate:.2f}, your ROI is ${investment_plan:.2f}  in year {year}")
    year += 1
