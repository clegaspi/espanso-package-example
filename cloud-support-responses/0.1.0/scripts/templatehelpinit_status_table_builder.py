from espanso import Espanso

def build_status_table():
    table_rows = [
        Espanso.replace(Espanso.get("text_prod_down"))
    ]

    trailing_table_rows = [
        Espanso.replace(Espanso.get("text_case_link")),
        Espanso.replace(Espanso.get("text_atlas_link")),
        Espanso.replace(Espanso.get("text_rs_topology")),
        Espanso.replace(Espanso.get("text_restarted_nodes"))
    ]

    if Espanso.get("capture.prod_down") == "YES":
        table_rows.append(Espanso.replace(Espanso.get("text_prod_down_duration")))

    table_rows += trailing_table_rows
    
    text_to_print = ""

    for row in table_rows:
        text_to_print += row
        if text_to_print[-1] != '\n':
            text_to_print += '\n'

    return text_to_print

if __name__ == "__main__":
    Espanso.run(build_status_table)
