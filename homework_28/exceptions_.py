div_ = 0
try:
    if div_ == 0:
        raise ValueError
    10 / "1"
    10 / 0
    a = 1
except (ZeroDivisionError, TypeError) as error:
    a = 0
    # print(error)

except ValueError:
    a = 5

customer_pay = 0
if customer_pay < 5000:
    raise ValueError("Unsupported Value: customer pay should be greater than 4999 usd")

# print(a)


