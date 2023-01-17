# A program to convert a bitcoin amount to us dollars

def main():
    print("As of 1/17/2023 at 4:23pm, bitcoin is currently trading at $21,334 per bitcoin.")
    
    bitcoin_amount = float(input("Enter the bitcoin amount: "))
    dollar_amount = bitcoin_amount * 21334
    formatted_dollars = format(dollar_amount, ".2f")

    print("That is worth", formatted_dollars, "us dollars.")
    
main()