from typing import List, Tuple
import json
from memory_profiler import memory_usage

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    def process():
        tweets_with_likes = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                tweet = json.loads(line.strip())
                if "content" in tweet and "likeCount" in tweet:
                    tweets_with_likes.append((tweet["content"], tweet["likeCount"]))

        return sorted(tweets_with_likes, key=lambda x: x[1], reverse=True)[:10]

    mem_usage, result = memory_usage((process,), retval=True)
    print(f"Uso de memória: {max(mem_usage) - min(mem_usage):.2f} MiB")
    return result