def float_to_binary_fixed(num, frac_bits=4):
    """Converts a positive float to a fixed-point binary string."""
    integer_part = int(num)
    fractional_part = num - integer_part
    
    # Convert integer part to binary
    bin_int = bin(integer_part)[2:]
    
    # Convert fractional part to binary
    bin_frac = []
    while fractional_part > 0 and len(bin_frac) < frac_bits:
        fractional_part *= 2
        bit = int(fractional_part)
        bin_frac.append(str(bit))
        fractional_part -= bit
        
    # Pad fractional part with trailing zeros if necessary
    frac_str = "".join(bin_frac).ljust(frac_bits, '0')
    return f"{bin_int}.{frac_str}"

def binary_fixed_to_float(bin_str):
    """Converts a fixed-point binary string back to a float."""
    int_str, frac_str = bin_str.split('.')
    
    # Calculate integer decimal value
    decimal_val = int(int_str, 2)
    
    # Add fractional decimal value
    for i, bit in enumerate(frac_str):
        if bit == '1':
            decimal_val += 2 ** -(i + 1)
            
    return decimal_val

def subtract_binary(bin_a, bin_b):
    """Subtracts two aligned fixed-point binary strings (assuming bin_a >= bin_b)."""
    int_a, frac_a = bin_a.split('.')
    int_b, frac_b = bin_b.split('.')
    
    # Remove the dot to perform pure integer subtraction
    combined_a = int(int_a + frac_a, 2)
    combined_b = int(int_b + frac_b, 2)
    
    # Perform subtraction
    diff_int = combined_a - combined_b
    
    # Re-insert the binary point
    total_bits = len(int_a + frac_a) # Assuming lengths are already aligned
    frac_len = len(frac_a)
    
    # Format the result back into binary string format
    diff_bin_str = bin(diff_int)[2:].zfill(total_bits)
    
    # Split back into integer and fractional string parts
    res_int = diff_bin_str[:-frac_len] or "0"
    res_frac = diff_bin_str[-frac_len:]
    
    return f"{res_int}.{res_frac}"

# --- Execution Steps ---
num1, num2 = 1.5, 0.25
print(f"Initial Values: a = {num1}, b = {num2}\n")

# Step 1: Convert to fixed binary format
bin_a = float_to_binary_fixed(num1, frac_bits=4)
bin_b = float_to_binary_fixed(num2, frac_bits=4)
print(f"Step 1: Convert to Binary")
print(f"  a -> {bin_a}")
print(f"  b -> {bin_b}\n")

# Step 2 & 3: Align points (already handled by matching frac_bits) and subtract
binary_result = subtract_binary(bin_a, bin_b)
print(f"Step 2 & 3: Align points and Subtract Significands")
print(f"    {bin_a}")
print(f"  - {bin_b}")
print(f"  ----------")
print(f"    {binary_result} (Binary Answer)\n")

# Step 4: Convert back to decimal
decimal_result = binary_fixed_to_float(binary_result)
print(f"Step 4: Express Final Answer")
print(f"  Binary representation: {binary_result}")
print(f"  Decimal value:        {decimal_result}")