from typing import List, Tuple
import json
import time

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    start = time.time()

    tweets_with_likes = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            tweet = json.loads(line.strip())
            if "content" in tweet and "likeCount" in tweet:
                tweets_with_likes.append((tweet["content"], tweet["likeCount"]))

    top10 = sorted(tweets_with_likes, key=lambda x: x[1], reverse=True)[:10]

    print(f"Tempo de execução: {time.time() - start:.2f} segundos")
    return top10