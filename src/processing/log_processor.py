import re
import pandas as pd
from pathlib import Path


LOG_PATTERN = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+)\s+"
    r"(\w+)\s+"
    r"([\w\.\$]+):\s+"
    r"(.*)"
)


def process_log_file(log_file_path):

    records = []

    with open(log_file_path, "r", encoding="utf-8", errors="ignore") as file:

        for line in file:

            match = LOG_PATTERN.match(line)

            if match:

                records.append(
                    {
                        "timestamp": match.group(1),
                        "log_level": match.group(2),
                        "component": match.group(3),
                        "message": match.group(4),
                        "source_file": Path(log_file_path).name
                    }
                )

    return pd.DataFrame(records)