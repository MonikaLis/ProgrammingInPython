import cmath
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("a", help="first polynomial coefficient",
                    type=int)
ap.add_argument("b", help="second polynomial coefficient",
                    type=int)
ap.add_argument("c", help="third polynomial coefficient",
                    type=int)

args = ap.parse_args()
    

delta = args.b**(2)-4*args.a*args.c
x0 = (-args.b-cmath.sqrt(delta))/2*args.a
x1 = (-args.b+cmath.sqrt(delta))/2*args.a

print('Pierwiastki rownania kwadratowego to: {0} and {1}'.format(x0,x1))

