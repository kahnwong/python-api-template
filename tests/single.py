from fastapi.testclient import TestClient

from python_api_template.main import app

client = TestClient(app)


################################
# Main
################################
def test_single():
    response = client.post("/", json={"id": "foo", "message": "hello world"})

    assert response.status_code == 200


if __name__ == "__main__":
    test_single()
    print("\n\n\n\n\n")
