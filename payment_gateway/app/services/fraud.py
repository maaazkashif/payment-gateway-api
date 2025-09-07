def fraud_check(amount: float, customer_balance: float) -> (bool, str):
    if amount > 5000:
        return False, "Amount exceeds fraud threshold"
    if amount > customer_balance * 0.9:  # spending >90% of balance
        return False, "Suspicious activity: draining account"
    return True, ""
