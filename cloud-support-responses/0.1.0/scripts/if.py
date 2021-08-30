from espanso import Espanso


def if_func(*args):
    if len(args) < 2:
        raise ValueError("Not enough arguments for if.py")

    else_value = ""
    if len(args) % 2 == 1:
        else_value = args[-1]
        args = args[:-1]

    for condition, result in Espanso.grouper(args, 2):
        if eval(condition):
            return Espanso.string_escape(result)
    return Espanso.string_escape(else_value)

if __name__ == '__main__':
    Espanso.run(if_func)
