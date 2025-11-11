
total =0
    num = float(input("Enter a number (negative to stop): "))
    
    # Check if the number is negative
    if num < 0:
        break  # Exit the loop if negative
    
    # Add the number to the total
    total += num

# Print the final sum
print("The total sum is:", total)
