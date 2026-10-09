import time
def call_llm_with_retry(prompt, client, retries = 3) :
    for attempt in range(retries):
        try:
            return client.generate(prompt)

        except (TimeoutError, ConnectionError) as e:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)


class FakeClient:
    def __init__(self):
        self.calls = 0

    def generate(self, prompt):
        self.calls += 1
        if self.calls < 3:
            raise TimeoutError("Simulated timeout")
        return f"response to: {prompt}"

if __name__ == "__main__":
    print(call_llm_with_retry("hello", FakeClient()));