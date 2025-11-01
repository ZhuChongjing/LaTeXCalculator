from .calculator import *

app = LaTeXExpressionCalculatorApp()

def interactive_calculator():
    """
    Interactive calculator.
    """
    
    console.print(Panel(
        title="LaTeX Interactive Calculator",
        renderable="""\
enter 'quit' to exit
enter 'help' to view help
enter 'calc' to enter calculation mode
enter 'solve' to enter equation solving mode
enter 'derivative' to calculate derivative
enter 'integral' to calculate integral
enter 'limit' to calculate limit""",
        border_style="green"
    ))

    while True:
        user_input = console.input("\n[green]Command> [/green]").strip().lower()
        
        if user_input == 'quit':
            print("Goodbye!")
            break
        elif user_input == 'help':
            print_help()
        elif user_input == 'calc':
            _calculation_mode()
        elif user_input == 'solve':
            _equation_solving_mode()
        elif user_input == 'derivative':
            _derivative_mode()
        elif user_input == 'integral':
            _integral_mode()
        elif user_input == 'limit':
            _limit_mode()
        else:
            print("Invalid command. Please enter 'help', 'calc', 'solve', 'derivative', 'integral', 'limit', or 'quit'.")


def _calculation_mode():
    console.print(Panel(
        title="Calculation Mode",
        renderable="Enter 'quit' to return to Command mode\nEnter LaTeX expressions to calculate",
        border_style="yellow"
    ))
    
    while True:
        user_input = console.input("\n[yellow]LaTeX> [/yellow]").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            console.print("Returning to Command mode...")
            break
        
        try:
            result = app.calculate(user_input)
            console.print(f"Result: {result['result']}")
            if result['latex_result']:
                console.print(f"LaTeX: {result['latex_result']}")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


def _equation_solving_mode():
    console.print(Panel(
        title="Equation Solving Mode",
        renderable="Enter 'quit' to return to Command mode\nEnter equations to solve (use commas for systems)",
        border_style="yellow"
    ))
    
    while True:
        user_input = console.input("\n[yellow]Equation> [/yellow]").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            console.print("Returning to Command mode...")
            break
        
        try:
            if ',' in user_input:
                equations = [eq.strip() for eq in user_input.split(',')]
                result = app.solve_system(equations)
            else:
                result = app.solve_equation(user_input)
            
            if 'solutions' in result:
                console.print(f"Solutions: {result['solutions']}")
            if 'numeric_solutions' in result:
                console.print(f"Numeric solutions: {result['numeric_solutions']}")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


def _derivative_mode():
    console.print(Panel(
        title="Derivative Mode",
        renderable="Enter 'quit' to return to Command mode\nEnter expressions to differentiate (optionally specify variable: 'expr, var')",
        border_style="yellow"
    ))
    
    while True:
        user_input = console.input("\n[yellow]Derivative> [/yellow]").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            console.print("Returning to Command mode...")
            break
        
        try:
            if ',' in user_input:
                expr, var = [x.strip() for x in user_input.split(',', 1)]
                result = app.calculate_derivative(expr, variable=var)
            else:
                result = app.calculate_derivative(user_input)
            
            console.print(f"Derivative: {result['derivative']}")
            console.print(f"LaTeX: {result['latex_result']}")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


def _integral_mode():
    console.print(Panel(
        title="Integral Mode",
        renderable="Enter 'quit' to return to Command mode\nEnter expressions to integrate (optionally specify variable: 'expr, var')",
        border_style="yellow"
    ))
    
    while True:
        user_input = console.input("\n[yellow]Integral> [/yellow]").strip() 
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            console.print("Returning to Command mode...")
            break
        
        try:
            if ',' in user_input:
                expr, var = [x.strip() for x in user_input.split(',', 1)]
                result = app.calculate_integral(expr, variable=var)
            else:
                result = app.calculate_integral(user_input)
            
            console.print(f"Integral: {result['result']}")
            console.print(f"LaTeX: {result['latex_result']}")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


def _limit_mode():
    console.print(Panel(
        title="Limit Mode",
        renderable="Enter 'quit' to return to Command mode\nEnter expressions to find limit (optionally specify variable and point: 'expr, var, point')",
        border_style="yellow"
    ))
    
    while True:
        user_input = console.input("\n[yellow]Limit> [/yellow]").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            console.print("Returning to Command mode...")
            break
        
        try:
            if ',' in user_input:
                parts = [x.strip() for x in user_input.split(',')]
                if len(parts) == 3:
                    expr, var, point = parts
                    result = app.calculate_limit(expr, variable=var, point=point)
                elif len(parts) == 2:
                    expr, var = parts
                    result = app.calculate_limit(expr, variable=var)
                else:
                    result = app.calculate_limit(parts[0])
            else:
                result = app.calculate_limit(user_input)
            
            console.print(f"Limit: {result['limit']}")
            console.print(f"LaTeX: {result['latex_result']}")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
