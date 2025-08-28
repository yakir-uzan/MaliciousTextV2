from app.Preprocessing.cleaner import  Cleaner
from app.Preprocessing.consumer import  Consumer


class Main:
    def __init__(self):
        self.text_consumer = Consumer()


    def process_messages(self):
        # Subscribe to two topics
        try:
            for message in self.text_consumer.consumer:
                msg = message.value
                topic = message.topic
                original_text = msg.get("text", "")
                cleaned_text = Cleaner(original_text).get_text()

                print("--------------------------------------------------")
                print(f" Topic: {topic}")
                print(f" Original: {original_text}")
                print(f" Cleaned: {cleaned_text}")

                yield {
                    'topic': topic,
                    'original_text': original_text,
                    'cleaned_text': cleaned_text,
                    'timestamp': message.timestamp
                }


        except KeyboardInterrupt:
            print("\n close the consumer...")
        except Exception as e:
            print(f"Error processing messages: {e}")
        finally:
            self.text_consumer.consumer.close()


if __name__ == "__main__":
    main_processor = Main()

    # אופציה 1: שימוש ב-generator
    for processed_message in main_processor.process_messages():
        # עשה משהו עם כל הודעה מעובדת
        print(f"נתקבל טקסט מנוקה: {processed_message['cleaned_text'][:50]}...")
