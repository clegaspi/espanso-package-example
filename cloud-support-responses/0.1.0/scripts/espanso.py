import re
import os
import sys
from itertools import zip_longest

class Espanso:
    @staticmethod
    def run(func, *args, print_result=True, replace_vars_in_args=True):
        if not args:
            args = []
            if len(sys.argv) > 1:
                args = sys.argv[1:]

        if replace_vars_in_args:
            args = [Espanso.replace(arg) for arg in args]
        
        try:
            result = func(*args)
        except Exception:
            import traceback
            # Print traceback to stdout so espanso outputs it
            traceback.print_exc(file=sys.stdout)
            # Required to exit the function and not re-raise the exception
            return
        
        if print_result:
            print(result)
        
    @staticmethod
    def get(var_name, default=""):
        sysvar_name = "ESPANSO_" + var_name.upper().replace(".", "_").replace(" ","-")
        return os.environ.get(sysvar_name, default=default)

    @staticmethod    
    def replace(value):
        espanso_vars = set(re.findall(r'{{(.+?)}}', value))
        for var in espanso_vars:
            var_value = Espanso.get(var)
            value = re.sub(
                r'{{' + re.escape(var) + r'}}',
                var_value, 
                Espanso.string_escape(value)
            )
        return value

    @staticmethod
    def grouper(iterable, n, fillvalue=None):
        "Collect data into fixed-length chunks or blocks"
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
        args = [iter(iterable)] * n
        return zip_longest(fillvalue=fillvalue, *args)

    @staticmethod
    def string_escape(s, encoding='utf-8'):
        # From https://stackoverflow.com/questions/14820429/how-do-i-decodestring-escape-in-python3
        return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
                .decode('unicode-escape') # Perform the actual octal-escaping decode
                .encode('latin1')         # 1:1 mapping back to bytes
                .decode(encoding))        # Decode original encoding
