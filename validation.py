def valid_amount(value):
    try:
        money = float(value)
    except:
        return False

    if money <= 0:
        return False

    return True


def valid_category(category):
    return category != ""