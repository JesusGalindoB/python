def suma(**kwargs):
    print(kwargs)

def usuarios(*args):
    print(args)

suma(uno=20, dos=30, tres=50, cuatro=60)
usuarios(20, 30, 40, 'juan', True)
