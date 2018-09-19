from a1 import __file__ as f

def check_linalg():
    return not ('linalg' in open(f, 'r').read()) 
