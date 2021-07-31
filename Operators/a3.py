from datetime import date
start_date = input("Enter start date in YYYY-MM-DD format")
year, month, day = map(int, start_date.split('-'))
start_date = date(year, month, day)

end_date = input("Enter end date in YYYY-MM-DD format")
year1, month1, day1 = map(int, end_date.split('-'))
end_date = date(year1, month1, day1)

delta = end_date - start_date
print(str(delta.days)+" days")

'''Output
Enter start date in YYYY-MM-DD format2014-07-02
Enter end date in YYYY-MM-DD format2014-07-11
9 days '''