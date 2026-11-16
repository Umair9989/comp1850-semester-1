
import matplotlib.pyplot as plt  # import library

# Test 1: Original example - y=x^2
x = [ k for k in range(10) ]  # create a range for the data
y = [ k*k for k in x ]      # create a simple function y=x^2

plt.figure(figsize=(12, 8))

# Subplot 1: Original plot
plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o', color='blue', linewidth=2)
plt.xlabel('x')
plt.ylabel('y=x^2')
plt.title('Original: y=x^2')
plt.grid(True)

# Subplot 2: Modified range - larger data
plt.subplot(2, 2, 2)
x2 = [k for k in range(20)]
y2 = [k*k for k in x2]
plt.plot(x2, y2, marker='s', color='red', linewidth=2)
plt.xlabel('x')
plt.ylabel('y=x^2')
plt.title('Extended Range: y=x^2 (0-20)')
plt.grid(True)

# Subplot 3: Different function - y=2x+3
plt.subplot(2, 2, 3)
x3 = [k/10 for k in range(100)]
y3 = [2*k + 3 for k in x3]
plt.plot(x3, y3, marker='^', color='green', linewidth=2)
plt.xlabel('x')
plt.ylabel('y=2x+3')
plt.title('Linear Function: y=2x+3')
plt.grid(True)

# Subplot 4: Multiple functions with scatter plot
plt.subplot(2, 2, 4)
x4 = [k for k in range(10)]
y4a = [k*k for k in x4]
y4b = [k*2 for k in x4]
plt.scatter(x4, y4a, marker='o', color='purple', s=100, label='y=x^2', alpha=0.7)
plt.scatter(x4, y4b, marker='s', color='orange', s=100, label='y=2x', alpha=0.7)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Multiple Functions Comparison')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()  # display
