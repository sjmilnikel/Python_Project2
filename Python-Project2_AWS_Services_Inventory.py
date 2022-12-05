# Create a list of services using Python.

# The list should be empty initially.
my_list = []

# Populate the list using append or insert.
my_list.append('S3')
my_list.append('Lambda')
my_list.append('CloudFront')
my_list.append('DynamDB')

# Print the list and the length of the list.
print(my_list)
print(len(my_list))

# Remove two specific services from the list by name or by index.
del my_list[1]
del my_list[2]

# Print the new list and the new length of the list.
print(my_list)
print(len(my_list))

