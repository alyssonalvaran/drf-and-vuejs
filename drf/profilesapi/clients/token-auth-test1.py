import requests

def client():
	token_h = "Token de49a691a343254d4a11a2bd3e9cc6ae1f0949a6"

	# credentials = {
	# 	"username": "alyssonalvaran",
	# 	"password": "Password0!",
	# }

	# response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
	# 						data=credentials)

	headers = {"Authorization": token_h}
	response = requests.get("http://127.0.0.1:8000/api/profiles/",
							headers=headers)

	print("Status code:", response.status_code)
	response_data = response.json()
	print(response_data)


if __name__ == "__main__":
	client()
