import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict
import os

class FunctionAnalyzer:
    def __init__(self):
        self.x = sp.symbols('x')
        self.function = None
        self.symbolic_expr = None
        
    def parse_function(self, func_str: str) -> bool:
        try:
            func_str = func_str.replace('^', '**')
            self.symbolic_expr = sp.sympify(func_str)
            self.function = sp.lambdify(self.x, self.symbolic_expr, 'numpy')
            return True
        except Exception as e:
            print(f"Error parsing function: {e}")
            return False
    
    def evaluate_at_point(self, x_val: float) -> float:
        try:
            return float(self.function(x_val))
        except Exception as e:
            if 'division by zero' in str(e).lower():
                raise ValueError(f"Division by zero at x = {x_val}")
            elif 'math domain error' in str(e).lower():
                raise ValueError(f"Domain error at x = {x_val}")
            else:
                raise
    
    def find_local_extrema(self, interval: Tuple[float, float]) -> Dict:
        a, b = interval
        derivative = sp.diff(self.symbolic_expr, self.x)
        f_prime = sp.lambdify(self.x, derivative, 'numpy')
        
        critical_points = []
        solutions = sp.solve(derivative, self.x)
        for sol in solutions:
            try:
                x_val = float(sol.evalf())
                if a <= x_val <= b:
                    critical_points.append(x_val)
            except:
                pass
        
        critical_points.extend([a, b])
        results = {'maxima': [], 'minima': [], 'saddle': []}
        
        for point in critical_points:
            try:
                y_val = self.evaluate_at_point(point)
                second_deriv = sp.diff(derivative, self.x)
                f_double_prime = sp.lambdify(self.x, second_deriv, 'numpy')
                try:
                    second_deriv_val = f_double_prime(point)
                    if second_deriv_val > 0:
                        results['minima'].append((point, y_val))
                    elif second_deriv_val < 0:
                        results['maxima'].append((point, y_val))
                    else:
                        results['saddle'].append((point, y_val))
                except:
                    results['saddle'].append((point, y_val))
            except ValueError:
                continue
        return results
    
    def find_roots(self, interval: Tuple[float, float], num_points: int = 1000) -> List[float]:
        a, b = interval
        x_vals = np.linspace(a, b, num_points)
        try:
            y_vals = self.function(x_vals)
        except Exception as e:
            print(f"Warning: {e}")
            return []
        
        roots = []
        for i in range(len(x_vals) - 1):
            if y_vals[i] == 0:
                roots.append(x_vals[i])
            elif y_vals[i] * y_vals[i+1] < 0:
                root = self._bisection_root(x_vals[i], x_vals[i+1])
                roots.append(root)
        return roots
    
    def _bisection_root(self, a: float, b: float, tol: float = 1e-10) -> float:
        fa = self.evaluate_at_point(a)
        fb = self.evaluate_at_point(b)
        if fa == 0:
            return a
        if fb == 0:
            return b
        for _ in range(100):
            c = (a + b) / 2
            fc = self.evaluate_at_point(c)
            if fc == 0 or (b - a) / 2 < tol:
                return c
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        return (a + b) / 2
    
    def plot_function(self, interval: Tuple[float, float], title: str = "Function Plot") -> plt.Figure:
        a, b = interval
        discontinuities = self._find_discontinuities(interval)
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if discontinuities:
            segments = sorted([a] + discontinuities + [b])
            for i in range(len(segments) - 1):
                seg_start, seg_end = segments[i], segments[i+1]
                if seg_end - seg_start < 1e-6:
                    continue
                x_vals = np.linspace(seg_start, seg_end, 1000)
                try:
                    y_vals = self.function(x_vals)
                    ax.plot(x_vals, y_vals, 'b-', linewidth=2)
                except Exception:
                    ax.axvline(x=seg_start, color='r', linestyle='--', alpha=0.5)
        else:
            x_vals = np.linspace(a, b, 1000)
            y_vals = self.function(x_vals)
            ax.plot(x_vals, y_vals, 'b-', linewidth=2)
        
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('f(x)', fontsize=12)
        ax.set_title(title, fontsize=14)
        
        for disc in discontinuities:
            ax.axvline(x=disc, color='r', linestyle='--', 
                      label='Discontinuity' if disc == discontinuities[0] else "")
        
        extrema = self.find_local_extrema(interval)
        if extrema['maxima']:
            max_x, max_y = zip(*extrema['maxima'])
            ax.plot(max_x, max_y, 'r^', markersize=10, label='Local Maxima')
        if extrema['minima']:
            min_x, min_y = zip(*extrema['minima'])
            ax.plot(min_x, min_y, 'gv', markersize=10, label='Local Minima')
        
        ax.legend()
        plt.tight_layout()
        return fig
    
    def _find_discontinuities(self, interval: Tuple[float, float]) -> List[float]:
        a, b = interval
        discontinuities = []
        if self.symbolic_expr.is_rational_function():
            denominator = sp.denom(self.symbolic_expr)
            solutions = sp.solve(denominator, self.x)
            for sol in solutions:
                try:
                    x_val = float(sol.evalf())
                    if a <= x_val <= b:
                        discontinuities.append(x_val)
                except:
                    pass
        for subexpr in sp.preorder_traversal(self.symbolic_expr):
            if subexpr.func == sp.log:
                arg = subexpr.args[0]
                solutions = sp.solve(arg, self.x)
                for sol in solutions:
                    try:
                        x_val = float(sol.evalf())
                        if a <= x_val <= b and arg.subs(self.x, x_val) <= 0:
                            discontinuities.append(x_val)
                    except:
                        pass
        return sorted(set(discontinuities))
    
    def calculate_integral(self, interval: Tuple[float, float]) -> float:
        a, b = interval
        integral = sp.integrate(self.symbolic_expr, (self.x, a, b))
        return float(integral.evalf())


def example_usage():
    analyzer = FunctionAnalyzer()
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    
    print("=" * 50)
    print("Example 1: f(x) = x^3 - 3*x + 2")
    print("=" * 50)
    analyzer.parse_function("x**3 - 3*x + 2")
    extrema = analyzer.find_local_extrema((-3, 3))
    print("Local Maxima:", extrema['maxima'])
    print("Local Minima:", extrema['minima'])
    roots = analyzer.find_roots((-3, 3))
    print("Roots:", roots)
    integral = analyzer.calculate_integral((-3, 3))
    print(f"Integral from -3 to 3: {integral:.4f}")
    fig = analyzer.plot_function((-3, 3), "f(x) = x³ - 3x + 2")
    plt.savefig("example_polynomial.png", dpi=150, bbox_inches='tight')
    
    print("\n" + "=" * 50)
    print("Example 2: f(x) = sin(x) + cos(x)")
    print("=" * 50)
    analyzer.parse_function("sin(x) + cos(x)")
    extrema = analyzer.find_local_extrema((0, 2*np.pi))
    print("Extrema in [0, 2π]:")
    print("  Maxima:", extrema['maxima'])
    print("  Minima:", extrema['minima'])
    fig = analyzer.plot_function((0, 2*np.pi), "f(x) = sin(x) + cos(x)")
    plt.savefig("example_trig.png", dpi=150, bbox_inches='tight')
    
    print("\n" + "=" * 50)
    print("Example 3: f(x) = 1/(x-2)")
    print("=" * 50)
    analyzer.parse_function("1/(x-2)")
    try:
        # This will show discontinuity at x=2
        fig = analyzer.plot_function((0, 4), "f(x) = 1/(x-2)")
        plt.savefig("example_discontinuity.png", dpi=150, bbox_inches='tight')
        print(f"Plot saved as '{script_name}_plot3.png' (note discontinuity at x=2)")
    except Exception as e:
        print(f"Plot error (expected for discontinuous function): {e}")
    
    print("\n" + "=" * 50)
    print("Example 4: Error Handling")
    print("=" * 50)
    
    # Invalid function
    success = analyzer.parse_function("x^ + 1")
    print(f"Parse invalid function 'x^ + 1': {'Success' if success else 'Failed (as expected)'}")
    
    # Valid function but problematic evaluation
    analyzer.parse_function("log(x-3)")
    try:
        result = analyzer.evaluate_at_point(2)
        print(f"log(2-3) = {result}")
    except ValueError as e:
        print(f"Error evaluating log(x-3) at x=2: {e}")


if __name__ == "__main__":
    example_usage()
