from scipy.special import zeta

# Calculate the Riemann zeta function for different values
s_values = [2, 3, 4, 1.5, 0.5]
zeta_values = [zeta(s) for s in s_values]

for s, z in zip(s_values, zeta_values):
    print(f"ζ({s}) = {z}")
