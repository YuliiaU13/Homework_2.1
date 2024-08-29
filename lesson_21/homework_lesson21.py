from utils.time_utils import TimeUtils


class LogAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def filter_logs(self):
        with open(self.input_file, 'r') as file:
            return [line for line in file if "Key TSTFEED0300|7E3E|0400" in line]

    def analyze_logs(self):
        filtered_logs = self.filter_logs()
        with open(self.output_file, 'w') as f:
            for i in range(len(filtered_logs) - 1):
                current_line = filtered_logs[i]
                next_line = filtered_logs[i + 1]

                current_timestamp_str = self.extract_timestamp(current_line)
                next_timestamp_str = self.extract_timestamp(next_line)

                heartbeat_difference = TimeUtils.calculate_time_difference(current_timestamp_str, next_timestamp_str)

                if 31 < heartbeat_difference < 33:
                    f.write(f"WARNING: Heartbeat difference is {heartbeat_difference} seconds in {current_timestamp_str}\n")
                elif heartbeat_difference == 33:
                    f.write(f"ERROR: Heartbeat difference is {heartbeat_difference} seconds in {current_timestamp_str}\n")

        print(f"Analysis is completed. Results are written down in the '{self.output_file}'")

    @staticmethod
    def extract_timestamp(line):
        return line[line.find("Timestamp ") + len("Timestamp "):].strip()[:8]


if __name__ == "__main__":
    input_file = "hblog.txt"
    output_file = "hb_test.log"
    analyzer = LogAnalyzer(input_file, output_file)
    analyzer.analyze_logs()
