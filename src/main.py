from api.client import APIClient


def search_by_username():
    print("Search by UserName")
    user = input("> ")
    client = APIClient()
    user_data = client.get_user_by_username(user)
    if user_data:
        name = user_data["name"]
        email = user_data["email"]
        phone = user_data["phone"]
        print(f"{name} can be reached via the following methods")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
    else:
        print("User not found")


if __name__ == '__main__':
    print("Hello world")
    search_by_username()
