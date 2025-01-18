# 12. Month to Number of Days
month = input("Enter the month name: ").strip().lower()
if month in ("january", "march", "may", "july", "august", "october", "december"):
    print("31 days")
elif month in ("april", "june", "september", "november"):
    print("30 days")
elif month == "february":
    print("28 or 29 days")
else:
    print("Invalid month")