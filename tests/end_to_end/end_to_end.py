import json
import time

import pytest
import requests
from fastapi.testclient import TestClient

from python_api_template.main import app

client = TestClient(app)

################################
# Prep input
################################
events = []
with open("data/tests.ndjson", "r") as f:
    events.extend([json.loads(i) for i in f.readlines()])

# events = events[:20]  # comment this out to enable all testcases


################################
# Main
################################
test_log = "data/tests.log"
test_output = open(test_log, "a")


@pytest.mark.parametrize("event", events)
def test_e2e(event):
    start_time = time.time()
    response = requests.post(
        "https://llm.karnwong.me",
        data=json.dumps(event),
    )
    end_time = time.time()

    log = {
        "status_code": response.status_code,
        "elapsed_time": end_time - start_time,
        "response": response.json(),
    }
    test_output.write(json.dumps(log) + "\n")

    assert response.status_code == 200


if __name__ == "__main__":
    test_e2e()
