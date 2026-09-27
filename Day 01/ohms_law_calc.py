
print("Ohm's Law Calculator")
print("This program calculates the missing value in Ohm's Law (V = I * R) given two of the three values (Voltage, Current, Resistance).")

I = input("Enter the current (I) in amperes (A), or type 'none' if unknown: ")
R = input("Enter the resistance (R) in ohms (Ω), or type 'none' if unknown: ")

if I == 'none' and R == 'none':
    print("Error: Both current (I) and resistance (R) cannot be unknown.")

elif I == 'none':
    R = float(R)
    V = float(input("Current (I) is unknown. Enter the voltage (V) in volts: "))
    I = V / R
    print(f"The calculated current (I) is: {I} amperes (A)")

elif R == 'none':
    I = float(I)
    V = float(input("Resistance (R) is unknown. Enter the voltage (V) in volts: "))
    R = V / I
    print(f"The calculated resistance (R) is: {R} ohms (Ω)")

else:
    I = float(I)
    R = float(R)
    V = I * R
    print(f"The calculated voltage (V) is: {V} volts (V)")