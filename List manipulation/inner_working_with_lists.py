# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

 
# Create areas_copy
areas_copy = list(areas)

# Note: Here we are demonstrating that using list() copies a list into another explicitly

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
print(areas_copy)