from app.retriever.fetcher import MongoFetcher
from app.retriever.producer import KafkaPublisher
import time

# יצירת מופעים של המחלקות
fetcher = MongoFetcher()
publisher = KafkaPublisher()

def run():
    while True:
        messages = fetcher.fetch_messagas()
        for msg in messages:
            # בודקת אם הערך הוא אנטישמי ואם כן יוצרת טופיק כזה
            if msg.get("antisemietic") == 1:
                topic = "raw_tweets_antisemitic"
            else:
                topic = "raw_tweets_not_antisemitic"
            # שולח את ההודעות לקאפקה
            publisher.publish(topic, msg)
        # מחכה 60 שניות עד השליחה הבאה
        time.sleep(60)

if __name__ == "__main__":
    run()
