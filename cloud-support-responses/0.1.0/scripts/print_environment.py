import os

def print_env():
    print("Printing environment vars")
    for var, value in os.environ.items():
        if var.startswith("ESPANSO_"):
            print(b"VAR: " + bytes(var, 'utf-8'))
            print(b"VALUE: " + bytes(value, 'utf-8'))

if __name__ == '__main__':
    print_env()
