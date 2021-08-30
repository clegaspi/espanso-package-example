from espanso import Espanso


def build_selection_options():
    options = [
        "driver",
        "conn_string",
        "ip_access_list",
        "app_error_logs",
        "last_occurrence",
        "connection_logic",
        "server_ips",
        "mongo_shell",
        "connectivity_tests",
    ]

    text_to_print = ""

    for option in options:
        ask_var = "capture.ask_" + option
        text_var = "text_" + option
        if Espanso.get(ask_var) == "Yes":
            text_to_print += Espanso.replace(Espanso.get(text_var))
            if text_to_print[-1] != '\n':
                text_to_print += '\n'
    
    return text_to_print

if __name__ == '__main__':
    Espanso.run(build_selection_options)
