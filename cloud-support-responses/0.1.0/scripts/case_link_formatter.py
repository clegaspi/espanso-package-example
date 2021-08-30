# Function to get a case or chat from a link that is passed in, and format it accordingly
import re

from espanso import Espanso

def make_case_link_text(raw_value):
    link = Espanso.replace(raw_value)
    partial_case_link = 'https://support.mongodb.com/case/'
    is_intercom = re.match(r'.*intercom.*', link) is not None
    is_case = re.match(r'.*support\.mongodb\.com.*', link) is not None
    if is_case:
        stripped_case_num = re.findall(r'^(?:.*)([0-9]{8})(?:.*)', link)
        if stripped_case_num:
            completed_case_link = f'*Case: {stripped_case_num[0]}* - ' + partial_case_link + stripped_case_num[0]
        else:
            completed_case_link = '*Case:* ' + link
        completed_case_link += f' - *{Espanso.get("capture.priority_level")}*'
    elif is_intercom:
        completed_case_link = '*Intercom Conversation:* ' + link
    else:
        completed_case_link = link
    return completed_case_link


if __name__ == '__main__':
    Espanso.run(make_case_link_text)
