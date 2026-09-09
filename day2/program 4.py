price=float(input())
quantity=int(input())
discount=float(input())
total=price*quantity
discount_amount=total*discount/100
final_amount=total-discount_amount
print(final_amount)
