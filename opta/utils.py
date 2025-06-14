from datetime import datetime
import pytz


def opta_format_parse_date(date_str: str) -> datetime:
    # Parse the date string assuming it's in the format YYYY-MM-DDZ
    parsed_date = datetime.strptime(date_str, "%Y-%m-%dZ")
    # Set the timezone to UTC
    parsed_date = parsed_date.replace(tzinfo=pytz.UTC)
    return parsed_date
