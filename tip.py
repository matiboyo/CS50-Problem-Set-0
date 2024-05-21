def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
def dollars_to_float(d):
    formatted_d = d.replace('$', '')
    return float(formatted_d)
def percent_to_float(p):
    formatted_p = p.replace('%',  '')    
    return float(formatted_p)/100
main()