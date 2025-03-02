import requests

BASE_URL = "https://middleware.example.com"

def test_inquiry():
   
    response = requests.post(f"{BASE_URL}/inquiry", json={"customer_id": "123456"})
    
    assert response.status_code == 200, "Inquiry request failed!"
    

    response_data = response.json()
    assert "bill_amount" in response_data, "Bill amount missing in response"
    assert response_data["bill_amount"] > 0, "Invalid bill amount"
    
    print("berhasil")

test_inquiry()

import requests
from unittest.mock import patch

BASE_URL = "https://middleware.example.com"


def mock_biller_response():
    return {"bill_amount": 50000, "due_date": "2025-03-10", "status": "Pending"}

def test_biller_mock():
    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = mock_biller_response()
        mock_post.return_value.status_code = 200

  
        response = requests.post(f"{BASE_URL}/biller")
        
        
        assert response.status_code == 200, "Biller request failed!"
        assert response.json()["status"] == "Pending", "Invalid status response"
    
        print("berhasil")

test_biller_mock()


