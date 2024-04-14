list1 = []

print("paste the domains here and hit enter when finished:  ")

while True:
    user_input = input()
    if user_input == "":
        break
    list1.append(user_input)

new_list = ["0.0.0.0 " + item for item in list1]

newest_list = [item for sublist in [item.split(",") for item in new_list] for item in sublist]

for item in newest_list:
    print(item)
