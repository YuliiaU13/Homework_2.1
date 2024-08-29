from datetime import datetime


class TimeUtils:
    @staticmethod
    def calculate_time_difference(timestamp_str, next_timestamp_str):
        timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
        next_timestamp = datetime.strptime(next_timestamp_str, "%H:%M:%S")
        # next_timestamp > timestamp:
        return (timestamp - next_timestamp).total_seconds()

