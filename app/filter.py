"""
Programmatically generate item filter files.
This project aims to simplify the configuration of colors, sounds, effects etc.
This is done by adding tags to all items and then applying rules to those tags.
In doing so we avoid the many to many assignment of properties and try to
reduce it to one-to-one as much as possible
"""

import os
import datetime

from app import formatting

FILTER_EXTENSION = "filter"
RUTHLESS_EXTENSION = "ruthlessfilter"
FILTER_OUTPUT_PATH = "C:\\Users\\matth\\Documents\\my games\\Path of Exile"


def sort_rules(rules):
    """Sort by importance based on TierStyle, all hide blocks go last"""
    print(type(rules[0]))
    print(type(rules[1]))
    return rules


def generate(*, rules, filter_name, is_ruthless=False):
    header = f"""
        # The following item filter was automatically generated.
        # Created on {datetime.datetime.now().strftime("%A %B %d %Y, %H:%M:%S")}.
    """
    sorted_rules = sort_rules(rules)
    file_content = formatting.format_filter(
        rules=sorted_rules,
        header=header,
    )
    filter_filename = (
        f"{filter_name}.{RUTHLESS_EXTENSION if is_ruthless else FILTER_EXTENSION}"
    )
    output_filepath = os.path.join(FILTER_OUTPUT_PATH, filter_filename)
    with open(output_filepath, mode="w", encoding="utf-8") as output_file:
        output_file.write(file_content)
    divider = "=" * 10
    print(divider)
    print("Inspect the item filter:")
    print(output_filepath)
    print(divider)
