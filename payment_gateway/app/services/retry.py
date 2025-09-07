import time, random

def retry_operation(operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            if random.random() < 0.3:  # simulate 30% failure chance
                raise Exception("Simulated network failure")
            return operation()
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e
def safe_commit(db, obj):
    def _commit():
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    return retry_operation(_commit)
