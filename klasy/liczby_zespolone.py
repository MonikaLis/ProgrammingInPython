import cmath

class complex_numbers:
    def addition():
        ap = argparse.ArgumentParser()
        ap.add_argument("a", help="first polynomial coefficient", type=int)
        ap.add_argument("b", help="second polynomial coefficient", type=int)
        args = ap.parse_args()
     
        res.real = args.a.real + args.b.real
        res.imag = args.a.imag + args.b.imag
        return res.real + res.imag

    def subtraction():
        ap = argparse.ArgumentParser()
        ap.add_argument("a", help="first polynomial coefficient", type=int)
        ap.add_argument("b", help="second polynomial coefficient", type=int)
        args = ap.parse_args()
     
        res.real = args.a.real - args.b.real
        res.imag = args.a.imag - args.b.imag
        return res.real + res.imag 

def multiplication():
        ap = argparse.ArgumentParser()
        ap.add_argument("a", help="first polynomial coefficient", type=int)
        ap.add_argument("b", help="second polynomial coefficient", type=int)
        args = ap.parse_args()
        
        res = args.a.real * args.b.real + args.a.real * args.b.image + args.a.image * args.b.real + args.a.image* args.b.image
        return res
    
