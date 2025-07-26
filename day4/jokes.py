import requests
url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

#Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(list(data.keys()))
    print("Here's a random Chuck Norris Joke:")
    print(data['value'], f"(Created at: {data['created_at']})")
else:
    print(f"Failed to retrieve joke. Status code: {response.status_code}")