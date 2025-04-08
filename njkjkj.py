import numpy as np
import matplotlib.pyplot as plt

def e_to_ix(x, terms=20):
    total = 0
    for n in range(terms):
        total += (1j * x) ** n / np.math.factorial(n)
    return total

def cos_plus_i_sin(x, terms=20):
    cos_x = 0
    sin_x = 0
    for n in range(terms):
        cos_x += ((-1) ** n) * x ** (2 * n) / np.math.factorial(2 * n)
        sin_x += ((-1) ** n) * x ** (2 * n + 1) / np.math.factorial(2 * n + 1)
    return cos_x + 1j * sin_x

# Test for a range of x values
x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
eix_vals = [e_to_ix(x) for x in x_vals]
cis_vals = [cos_plus_i_sin(x) for x in x_vals]

# Compare real and imaginary parts
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_vals, [z.real for z in eix_vals], label='Re(e^{ix})')
plt.plot(x_vals, [z.real for z in cis_vals], '--', label='cos(x)')
plt.title('Real Parts')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_vals, [z.imag for z in eix_vals], label='Im(e^{ix})')
plt.plot(x_vals, [z.imag for z in cis_vals], '--', label='sin(x)')
plt.title('Imaginary Parts')
plt.legend()

plt.tight_layout()
plt.show()
