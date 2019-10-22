import requests

def main():
    # response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&&symbols=GBP")

    payload = {
        "base": "USD",
        "symbols": ["KRW", "PHP"]
    }
    response = requests.get(
        "https://api.exchangeratesapi.io/latest",
        params=payload
    )

    if response.status_code != 200:
        print("Status code: ", response.status_code)
        raise Exception("There's an error!")
    
    data = response.json()
    print("JSON data: ", data)

if __name__ == "__main__":
    main()