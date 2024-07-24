import re
from datetime import datetime


def string_match(source_str, words_to_match, seperator=','):
    words_to_match = words_to_match.split(seperator)
    pattern = re.compile('|'.join(words_to_match))
    match = re.search(pattern, source_str)
    return True if match else False


def get_timestamp(style="%Y-%m-%d_%H-%M-%S"):
    current_time = datetime.now()
    timestamp_str = current_time.strftime(style)
    return timestamp_str
