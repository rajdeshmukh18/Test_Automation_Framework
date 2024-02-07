from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

def calculate_past_date(time_delta_str):
    # Extract numerical value and unit from the input string
    match = re.match(r'(\d+)\s*(\w+)', time_delta_str)

    if match:
        value, unit = int(match.group(1)), match.group(2).lower()

        # Map units to timedelta arguments
        unit_mapping = {
            'hour': 'hours',
            'hours': 'hours',
            'day': 'days',
            'days': 'days',
            'month': 'months',
            'months': 'months'
        }

        if unit in unit_mapping:
            unit = unit_mapping[unit]

            # Calculate the past date using relativedelta for accurate month handling
            past_date = datetime.now() - relativedelta(**{unit: value})

            return past_date.strftime('%Y-%m-%d')

    # Invalid input format
    raise ValueError("Invalid time delta format. Example: '1 hour ago', '2 days ago', '1 month ago'")

# Examples
print(calculate_past_date("1 hour ago"))
print(calculate_past_date("2 year ago"))
print(calculate_past_date("1 month ago"))
