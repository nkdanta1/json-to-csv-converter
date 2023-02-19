from app import app


def test_convert_endpoint():
    # Create a test client using the Flask app
    client = app.test_client()

    # Define a sample JSON payload to send to the endpoint
    payload = {"name": "Alice", "age": 25}

    # Send a POST request to the endpoint with the JSON payload
    response = client.post("/convert", json=payload)

    # Check that the response has a 200 status code
    assert response.status_code == 200

    # Check that the response has a 'Content-Disposition' header
    assert "Content-Disposition" in response.headers

    # Check that the response has a 'Content-Type' header set to 'text/csv'
    assert response.headers["Content-Type"] == "text/csv"

    # Check that the response contains the expected CSV data
    expected_csv1 = "name,age\nAlice,25\n"
    expected_csv2 = "age,name\n25,Alice\n"
    assert (
        response.data.decode("utf-8") == expected_csv1
        or response.data.decode("utf-8") == expected_csv2
    )
