import os
import requests

def query_ibm_granite(prompt):
    api_key = os.getenv("GRANITE_API_KEY")
    endpoint = os.getenv("GRANITE_API_ENDPOINT")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "input": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_tokens": 200
        }
    }

    try:
        response = requests.post(endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("output", "No response received.")
    except Exception as e:
        return f"Error: {str(e)}"
