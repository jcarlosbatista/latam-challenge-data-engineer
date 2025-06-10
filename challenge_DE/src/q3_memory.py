from typing import List, Tuple
import json
import re
from collections import Counter
from memory_profiler import memory_usage

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    def process():
        country_mentions = Counter()
        pattern = re.compile(r"\b(India|USA|Canada|UK|Australia)\b", re.IGNORECASE)

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                tweet = json.loads(line.strip())
                matches = pattern.findall(tweet.get("content", ""))
                country_mentions.update([m.lower() for m in matches])

        return country_mentions.most_common()

    mem_usage, result = memory_usage((process,), retval=True)
    print(f"Uso de memória: {max(mem_usage) - min(mem_usage):.2f} MiB")
    return result