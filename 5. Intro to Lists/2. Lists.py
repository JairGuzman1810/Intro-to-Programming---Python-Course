flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold",
                "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

# ------ Length ------
# With the list, we can count the numbers of
# entries in any list with len()

# The list has ten entries
print(len(flowers_list))

# ------ Indexing ------
# We can refer to any item in the list according to
# its position in the list (first, second, third, etc).
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])

# ------ Slicing ------
# pull a segment of a list (for instance, the first three
# entries or the last two entries). This is called slicing.
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

# ------ Removing items ------
# Remove an item from a list with .remove(), and
# put the item you would like to remove in parentheses.
flowers_list.remove("globe thistle")
print(flowers_list)

# ------ Adding items  ------
# To add item to the list, we can use .append()
flowers_list.append("snapdragon")
print(flowers_list)

# ------ Lists are not just for strings  ------
# lists can have items with any data type, including booleans, integers, and floats.
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]

print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])

# To get the minimum we can use min(), for the maximum, max()
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))

# To add every item in the list, use sum().
print("Total books sold in one week:", sum(hardcover_sales))

# Calculations with slice:
# we take the sum from the first five days (sum(hardcover_sales[:5])), and then
# divide by five to get the average number of books sold in the first five days.
print("Average books sold in first five days:", sum(hardcover_sales[:5]) / 5)
