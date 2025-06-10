from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json
import time

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    start = time.time()

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

    most_active_by_day = [
        (date, Counter(users).most_common(1)[0][0]) for date, users in tweets_by_day.items()
    ]

    print(f"Tempo de execução: {time.time() - start:.2f} segundos")
    return sorted(most_active_by_day, key=lambda x: x[0])