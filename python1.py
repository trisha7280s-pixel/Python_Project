def to_twos_complement_8bit(val):
    """Converts an integer to its 8-bit 2's complement binary string representation."""
    # Mask to 8 bits to handle negative numbers automatically
    bits = val & 0xFF
    return f"{bits:08b}"

def from_twos_complement_8bit(binary_str):
    """Converts an 8-bit 2's complement binary string back to a signed decimal integer."""
    val = int(binary_str, 2)
    # If the sign bit (MSB) is 1, it's a negative number
    if val & 0x80:
        val -= 0x100
    return val

def add_8bit_signed(a, b):
    """Adds two integers using 8-bit 2's complement arithmetic and checks for overflow."""
    # Get binary representations
    bin_a = to_twos_complement_8bit(a)
    bin_a_val = int(bin_a, 2)
    bin_b = to_twos_complement_8bit(b)
    bin_b_val = int(bin_b, 2)
    
    # Perform 8-bit addition
    result_raw = bin_a_val + bin_b_val
    result_8bit = result_raw & 0xFF
    bin_result = f"{result_8bit:08b}"
    
    # Convert back to decimal signed value
    dec_result = from_twos_complement_8bit(bin_result)
    
    # Check for Overflow: 
    # Overflow occurs if two numbers of the same sign yield a result with a different sign.
    # Alternatively, if the carry into the MSB XOR carry out of the MSB is 1.
    sign_a = (bin_a_val >> 7) & 1
    sign_b = (bin_b_val >> 7) & 1
    sign_r = (result_8bit >> 7) & 1
    
    overflow = (sign_a == sign_b) and (sign_a != sign_r)
    
    return bin_a, bin_b, bin_result, dec_result, overflow

def print_expression_report(label, a, b):
    bin_a, bin_b, bin_result, dec_result, overflow = add_8bit_signed(a, b)
    print(f"--- Expression {label}: ({a}) + ({b}) ---")
    print(f"Operand A ({a: >+3}): {bin_a}")
    print(f"Operand B ({b: >+3}): {bin_b}")
    print(f"Binary Result:  {bin_result}")
    print(f"Decimal Result: {dec_result}")
    print(f"Overflow:       {'YES (Arithmetic Overflow Occurred)' if overflow else 'NO'}")
    print()

# Verify the expressions
print_expression_report("(a)", 20, 15)
print_expression_report("(b)", -20, -15)