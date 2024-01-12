from sympy import Symbol, diff


def get_function_and_derivative(func):
    x = Symbol('x')
    function = func(x)
    derivative = diff(func(x), x)
    return function, derivative


def newton_raphson(func, func_derivative, initial_guess, tolerance=1e-6, max_iterations=100):
    """
    Newton-Raphson method for finding the root of a function.

    Parameters:
    - func: The function for which the root is to be found.
    - func_derivative: The derivative of the function.
    - initial_guess: Initial guess for the root.
    - tolerance: The acceptable level of error.
    - max_iterations: Maximum number of iterations allowed.

    Returns:
    - The approximate root.
    - The number of iterations performed.
    """

    x = Symbol('x')  # Include x in the newton_raphson scope
    x_n = initial_guess
    iteration = 0

    while iteration < max_iterations:
        f_x_n = func.subs(x, x_n)  # Use x consistently
        f_prime_x_n = func_derivative.subs(x, x_n)

        if abs(f_prime_x_n) < tolerance:
            raise ValueError("Derivative is close to zero. Newton-Raphson method may not converge.")

        x_n -= f_x_n / f_prime_x_n

        if abs(f_x_n) < tolerance:
            return x_n, iteration

        print(f"Iteration = {iteration}, x = {x_n:.6f}, f(x) = {f_x_n:.6f}")
        iteration += 1

    raise ValueError("Newton-Raphson method did not converge within the maximum number of iterations.")


# Example usage:
def example_function(x):
    return x**6 + x**4 + x**2 + x


function, derivative = get_function_and_derivative(example_function)
print(" Newton-Raphson method")
print("=" * 50)
initial_guess = float(input('Enter initial guess: '))
root, iterations = newton_raphson(function, derivative, initial_guess)

print(f"Approximate root: {root}")
print(f"Iterations: {iterations}")
