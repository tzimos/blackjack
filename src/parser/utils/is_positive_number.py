def is_positive_number(val):
    try:
        val = int(val)
        return val > 0
    except ValueError:
        return False
    return True
