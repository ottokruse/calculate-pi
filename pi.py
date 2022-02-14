import sys
import functools

def calculate_pi(nr_of_fractals):
    """
    Calculate PI using Leibniz formula:
    pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    """
    
    return 4 * functools.reduce(lambda pi_4, i: pi_4 - 1/(2*i + 1) * (i % 2 or -1), range(1, nr_of_fractals), 1)

print(calculate_pi(int(sys.argv[1]) if len(sys.argv) > 1 else 1000))
