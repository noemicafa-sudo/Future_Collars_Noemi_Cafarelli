current_package_weight = 0
packages_sent = 0
unused_capacity_per_package = []
max_unused_package = None
max_unused_capacity = 0
total_weight = 0

max_items= (int(input("How many items do you have? ")))
items_count=0

while items_count < max_items:
    weight= float(input(f"What is the weight of item {items_count+1}?"))
    if weight == 0:
        break
    elif weight < 1 or weight > 10:
        print("The value has to be between 1 and 10")
        continue
    if current_package_weight + weight > 20:
        packages_sent += 1
        total_weight += current_package_weight

        unused = 20 - current_package_weight
        unused_capacity_per_package.append(unused)

        if unused > max_unused_capacity:
            max_unused_capacity = unused
            max_unused_package = packages_sent

        current_package_weight = weight
    else:
        current_package_weight += weight
    items_count += 1

if current_package_weight > 0:
    packages_sent += 1
    total_weight += current_package_weight

    unused = 20 - current_package_weight
    unused_capacity_per_package.append(unused)

if unused > max_unused_capacity:
    max_unused_capacity = unused
    max_unused_package = packages_sent

print(f"Packages sent: {packages_sent}\n"
      f"Total weight sent {total_weight}\n"
      f"Total unused capacity {packages_sent*20-total_weight}kg\n"
      f"Package with most unused space {max_unused_package} with {max_unused_capacity} kg used")


