import requests

def client():
	# data = {
	# 	"username": "admin",
	# 	"email": "admin@email.com",
	# 	"password1": "Password0!",
	# 	"password2": "Password0!",
	# }

	# response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
	# 						data=data)

	token_h = "Token 216f70909f02a1d7371683f46a2ece6b0bf23a3d"

	headers = {"Authorization": token_h}
	response = requests.get("http://127.0.0.1:8000/api/profiles/",
							headers=headers)

	print("Status code:", response.status_code)
	response_data = response.json()
	print(response_data)


if __name__ == "__main__":
	client()
