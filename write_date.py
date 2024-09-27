# AUTHOR: Marcus Ed. Butler
# VERSION: 2024-09-27_R0
# DESCRIPTION: Writes the current date into a file.
# This covers 13.1 and 13.2


from datetime import date


# Grab the current date.
current_date = date.today().strftime("%Y/%m/%d")

# Write to file.
with open("today.txt", "w") as f_obj:
    f_obj.write(current_date)
    f_obj.write("\n") # Removes symbol.


# Read from file.
with open("today.txt", "r") as f_obj:
    today_string = f_obj.read()

print(today_string)
