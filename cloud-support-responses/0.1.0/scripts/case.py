from espanso import Espanso

# This is mostly the same as if.py, but only allows string equality comparisons
def case_func(original_value, *cases):
    if len(cases) < 2:
        raise ValueError("Not enough arguments for case.py")

    if len(cases) % 2 == 1:
        default_value = cases[-1]
        cases = cases[:-1]
    else:
        default_value = ""

    for comparison_value, result in Espanso.grouper(cases, 2):
        if original_value == comparison_value:
            return Espanso.string_escape(result)
    return default_value

if __name__ == '__main__':
    Espanso.run(case_func)
