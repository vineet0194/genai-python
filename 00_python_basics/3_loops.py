# Loops

for i in range(1, 10):      #[1, 10)
    print(i)

print("\n\n")

##############################################################################################

orders = [1,2,3,4,5]

for i in orders:
    print(f"order num{i}")

print("\n\n")

##############################################################################################

seasons = ['spring', 'winter', 'summer']

# enumarate (numbers)
for i, item in enumerate(seasons, start=1):     # if u dont use start, it will be 0 based
    print(f"{i}: {item}!")

print("\n\n")

# zips (enumerate with custom)
for item in zip([50, 60, 70], seasons):     # need not be num-string, can be anything => it "zips" them
    print(item)

print("\n\n")

##############################################################################################

idx = 0
while True:
    if (idx==2):
        idx+=1
        continue

    if (idx==5):
        break

    print(idx)
    idx+=1

print("\n\n")

##############################################################################################

# Walrus Operator ( := )    exec and use on the go

val = 27
# rem = val % 5

# if (rem):
#     print("not div")

if (rem := val % 5):
    print("not div")

while (num := int(input("enter 1: ")) != 1):
    print("wrong input bro!")