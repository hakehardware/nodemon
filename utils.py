from datetime import datetime
from dateutil import tz

def get_date(data):

    # Define UTC and your local time zone
    utc_zone = tz.tzutc()
    local_zone = tz.tzlocal()

    # Remove the fractional seconds and 'Z' from the input string
    data = data.split('.')[0]
    data = data.rstrip('Z')

    # Convert the input string to a datetime object with UTC time zone
    utc_datetime = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S")
    utc_datetime = utc_datetime.replace(tzinfo=utc_zone)

    # Convert the UTC datetime to the local time zone
    local_datetime = utc_datetime.astimezone(local_zone)

    return local_datetime.strftime("%Y-%m-%d %H:%M:%S")