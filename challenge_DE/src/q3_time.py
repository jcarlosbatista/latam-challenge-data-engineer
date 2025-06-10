from typing import List, Tuple
import json
import time
import re
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    start = time.time()

    country_mentions = Counter()
    pattern = re.compile(r"\b(India|USA|Canada|UK|Australia)\b", re.IGNORECASE)

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            tweet = json.loads(line.strip())
            matches = pattern.findall(tweet.get("content", ""))
            country_mentions.update([m.lower() for m in matches])

    print(f"Tempo de execução: {time.time() - start:.2f} segundos")
    return country_mentions.most_common()