import json

import pytest
from fastapi.testclient import TestClient

from python_api_template.main import app

client = TestClient(app)

################################
# Prep input
################################
events = []
with open("data/tests.ndjson", "r") as f:
    events.extend([json.loads(i) for i in f.readlines()])

events = events[:5]  # comment this out to enable all testcases


################################
# Main
################################
test_log = "data/tests.log"
test_output = open(test_log, "a")


@pytest.mark.parametrize("event", events)
def test_full(event):
    response = client.post(
        "/",
        json=event,
    )

    test_output.write(json.dumps(response.json()) + "\n")

    assert response.status_code == 200


if __name__ == "__main__":
    test_full()
