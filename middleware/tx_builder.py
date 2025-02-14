# Intent Functionality WIP

def build_tx(msisdn, to, amount):
    user_address = get_address_from_sim(msisdn)  # SIM → Address mapping
    tx = {
        'to': to,
        'value': Web3.toWei(amount, 'ether'),
        'nonce': get_nonce(user_address)
    }
    signed_tx = sign_tx(tx, user_private_key)
    broadcast(signed_tx)
