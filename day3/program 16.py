views = int(input())
retention_percent = int(input())
is_original = input()
is_enrolled = input()
copyright_strike = input()

if copyright_strike == "true":
    print("Not Eligible")
elif is_enrolled == "false":
    print("Not Eligible")
elif is_original == "false":
    print("Not Eligible")
elif views >= 100000 and retention_percent >= 50:
    print("Eligible - Premium Payout")
elif views >= 100000 and retention_percent < 50:
    print("Eligible - Standard Payout")
elif 10000<views>99999 and retention_percent >= 60:
    print("Eligible - Standard Payout")
elif 10000<views>99999 and retention_percent < 60:
    print("Eligible - Minimum Payout")
elif views<10000:
    print("Not Eligible - Below Threshold")
