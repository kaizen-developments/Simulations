import random
import matplotlib.pyplot as plt

def monte_carlo_pi(num_samples=10000):
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []

    for _ in range(num_samples):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

samples = 10000
pi_value, xi, yi, xo, yo = monte_carlo_pi(samples)

print(f"Estimated value of π with {samples} samples: {pi_value:.5f}")
print(f"Value of pi up to 5 digits is 3.14159")
print(f"Portion of the difference w.r.t the original value up to 5 decimal places is {abs(pi_value:.5f - 3.14159)/pi_value:.5f}")
# Plotting
plt.figure(figsize=(6,6))
plt.scatter(xi, yi, color='green', s=1, label='Inside Circle')
plt.scatter(xo, yo, color='red', s=1, label='Outside Circle')
plt.title('Monte Carlo Simulation for Estimating π')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()