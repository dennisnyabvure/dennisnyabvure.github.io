height_lst = []
total = 10

for num in range(total):
    num = float(input('Enter next student height: '))
    height_lst.append(num)
avg = sum(height_lst)/total
print("The average height of the 10 students is ", round(avg,2))
input("\n\nPress the enter key to exit.")
