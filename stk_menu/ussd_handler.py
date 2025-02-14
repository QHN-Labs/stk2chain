#Intended Functionality WIP
def handle_ussd(input, msisdn):
    if input == "1":  # Send ETH
        return "Enter recipient address:"
    elif input == "1*0x123...*0.1":  # Address + amount
        build_tx(msisdn, "0x123...", 0.1)
