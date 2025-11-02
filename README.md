# LaTeXCalculator

A Python package for performing mathematical calculations using LaTeX syntax.

See the document at [LaTeXCalculator's Document](https://zhuchongjing.github.io/LaTeXCalculator-docs).

## Description

LaTeXCalculator is a powerful Python library that allows you to perform mathematical calculations using LaTeX syntax. It provides a simple and intuitive interface for evaluating complex mathematical expressions, solving equations, computing integrals, derivatives, limits, and more. Whether you're a student, researcher, or professional, LaTeXCalculator makes it easy to work with mathematical expressions in a format that's familiar to many in the scientific and mathematical community.

## Features

- **Evaluate LaTeX mathematical expressions** with numerical or symbolic results
- **Compute integrals** of LaTeX expressions
- **Calculate derivatives** of any order
- **Evaluate limits** of functions
- **Solve equations** and **systems of equations**
- **Support for variables** with custom values
- **Command-line interface** for quick calculations
- **Rich output formatting** for better readability
- **Comprehensive LaTeX command support** for mathematical notation

## Installation

You can install LaTeXCalculator using pip:

```bash
pip install LaTeXCalculator
```

## Usage

### Command Line Interface

LaTeXCalculator provides a command-line interface through the `latexcalc` command:

```bash
latexcalc
```

This will launch an interactive calculator where you can input LaTeX expressions and get instant results.

### Python API

You can also use LaTeXCalculator programmatically in your Python code:

> [!NOTE]
> 
> Code:
> 
> ```python
> from LaTeXCalculator import LaTeXExpressionCalculatorApp
> calc = LaTeXExpressionCalculatorApp()
> result = calc.calculate(r"\frac{1}{2} + \frac{1}{3}")
> print(result)
> ```
> 
> Output:
> 
> ```python
> {
>     'input': '\\frac{1}{2} + \\frac{1}{3}',
>     'parsed_expression': '1/3 + 1/2',
>     'result': 0.8333333333333334,
>     'result_type': 'numeric',
>     'latex_result': None,
>     'free_variables': []
> }
> ```

## Examples

### Basic Calculations

```python
from LaTeXCalculator import LaTeXExpressionCalculator

calc = LaTeXExpressionCalculator()

# Basic arithmetic
basic = calc.calculate(r"2 + 2 \times 3")
print(f"2 + 2 \times 3 = {basic['result']}")

# Fractions
fraction = calc.calculate(r"\frac{3}{4} + \frac{1}{2}")
print(f"\frac{{3}}{{4}} + \frac{{1}}{{2}} = {fraction['result']}")

# Square roots
sqrt_result = calc.calculate(r"\sqrt{16} + \sqrt{9}")
print(f"\sqrt{{16}} + \sqrt{{9}} = {sqrt_result['result']}")

# Trigonometric functions
trig = calc.calculate(r"\sin(\pi/2) + \cos(0)")
print(f"\sin(\pi/2) + \cos(0) = {trig['result']}")
```

### Algebraic Expressions

```python
from LaTeXCalculator import LaTeXExpressionCalculator

calc = LaTeXExpressionCalculator()

# Symbolic calculation (no numerical evaluation)
symbolic = calc.calculate(r"(x + y)^2", return_type='symbolic')
print(f"(x + y)^2 = {symbolic['result']}")

# Set variable values
calc.set_variables({'x': 3, 'y': 4})

# Calculate with variables
with_vars = calc.calculate(r"x^2 + y^2")
print(f"x^2 + y^2 = {with_vars['result']} where x=3, y=4")
```

### Integrals

```python
from LaTeXCalculator import LaTeXIntegralCalculator

integral_calc = LaTeXIntegralCalculator()

# Calculate indefinite integral
indefinite = integral_calc.calculate(r"x^2")
print(f"\int x^2 dx = {indefinite['latex_result']}")

# Calculate integral with a different variable
with_var = integral_calc.calculate(r"t^3", variable='t')
print(f"\int t^3 dt = {with_var['latex_result']}")
```

### Derivatives

```python
from LaTeXCalculator import LaTeXDerivativeCalculator

 deriv_calc = LaTeXDerivativeCalculator()

# Calculate first derivative
derivative = deriv_calc.calculate(r"\sin(x)")
print(f"\frac{{d}}{{dx}}\sin(x) = {derivative['latex_result']}")

# Calculate higher-order derivative
second_deriv = deriv_calc.calculate(r"x^3", n=2)
print(f"\frac{{d^2}}{{dx^2}}x^3 = {second_deriv['latex_result']}")

# Calculate derivative with respect to a different variable
with_var = deriv_calc.calculate(r"y^2", variable='y')
print(f"\frac{{d}}{{dy}}y^2 = {with_var['latex_result']}")
```

### Limits

```python
from LaTeXCalculator import LaTeXLimitCalculator

limit_calc = LaTeXLimitCalculator()

# Calculate limit
limit = limit_calc.calculate(r"\frac{\sin(x)}{x}", point='0')
print(f"\lim_{{x \to 0}}\frac{{\sin(x)}}{{x}} = {limit['result']}")

# Calculate limit at infinity
infinite_limit = limit_calc.calculate(r"\frac{1}{x}", point='\infty')
print(f"\lim_{{x \to \infty}}\frac{{1}}{{x}} = {infinite_limit['result']}")
```

### Equation Solving

```python
from LaTeXCalculator import LaTeXEquationSolver

eqn_solver = LaTeXEquationSolver()

# Solve a linear equation
solution = eqn_solver.solve(r"2x + 3 = 7")
print(f"Solution to 2x + 3 = 7: {solution['solutions']}")

# Solve a quadratic equation
quadratic = eqn_solver.solve(r"x^2 - 5x + 6 = 0")
print(f"Solutions to x^2 - 5x + 6 = 0: {quadratic['solutions']}")
```

### Systems of Equations

```python
from LaTeXCalculator import LaTeXSystemSolver

system_solver = LaTeXSystemSolver()

# Solve a system of equations
system = [
    r"x + y = 5",
    r"2x - y = 1"
]
solutions = system_solver.solve(system)
print(f"Solutions to the system: {solutions['solutions']}")
```

## Supported LaTeX Commands

LaTeXCalculator supports a wide range of LaTeX commands for mathematical notation, including but not limited to:

### Arithmetic Operators

- Addition: `+`
- Subtraction: `-`
- Multiplication: `\times`, `\cdot`, implicit multiplication (`2x`)
- Division: `/`, `\div`, `\frac{a}{b}`
- Exponentiation: `^` (automatically converted to `**`)

### Functions

- Trigonometric: `\sin`, `\cos`, `\tan`, `\cot`, `\sec`, `\csc`
- Inverse trigonometric: `\arcsin`, `\arccos`, `\arctan`
- Hyperbolic: `\sinh`, `\cosh`, `\tanh`
- Logarithmic: `\log`, `\ln`
- Exponential: `\exp`
- Square root: `\sqrt{x}`
- Nth root: `\sqrt[n]{x}`
- Absolute value: `\abs{x}`
- Factorial: `\factorial{x}`
- Gamma function: `\gamma{x}`
- Binomial coefficient: `\binom{n}{k}`

### Constants and Symbols

- `\pi` (pi)
- `\infty` (infinity)
- Greek letters: `\alpha`, `\beta`, `\gamma`, etc.

## Dependencies

LaTeXCalculator relies on the following Python libraries:

- [sympy](https://www.sympy.org/): For symbolic mathematics
- [rich](https://rich.readthedocs.io/): For enhanced terminal output

These dependencies are automatically installed when you install LaTeXCalculator via pip.

## License

LaTeXCalculator is licensed under the MIT License. See the [LICENSE file](https://github.com/ZhuChongjing/LaTeXCalculator/blob/main/LICENSE) for more details.

## Author

LaTeXCalculator was created by Zhu Chongjing.

For questions or feedback, please contact [zhuchongjing_pypi@163.com](mailto:zhuchongjing_pypi@163.com).
