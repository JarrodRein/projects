import cmath

# Read complex number input as string and convert to complex
z = complex(input()) # e.g., "1+2j"

# Calculate magnitude and phase
r = abs(z) # magnitude = sqrt(x^2 + y^2)
phi = cmath.phase(z) # phase angle in radians

# Print results
print(r)
print(phi)