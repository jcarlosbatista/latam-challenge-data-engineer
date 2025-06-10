from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json
from memory_profiler import memory_usage

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    def process():
        tweets_by_day = defaultdict(list)
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                tweet = json.loads(line.strip())
                try:
                    tweet_date = datetime.fromisoformat(tweet["date"]).date()
                    user = tweet["user"]["username"]
                    tweets_by_day[tweet_date].append(user)
                except Exception:
                    continue

        return sorted(
            [(date, Counter(users).most_common(1)[0][0]) for date, users in tweets_by_day.items()],
            key=lambda x: x[0]
        )

    mem_usage, result = memory_usage((process, ), retval=True)
    print(f"Uso de memória: {max(mem_usage) - min(mem_usage):.2f} MiB")
    return result