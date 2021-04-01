import requests
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

def main():
	next_token = writeFollowers({})
	while next_token != "Done":
		params = {"pagination_token": next_token}
		next_token = writeFollowers(params)
		#print("next_token - " + next_token)

	checkFollowers()


def writeFollowers(params):

	url = "https://api.twitter.com/2/users/1253685736173260800/followers?max_results=1000"

	payload={}
	headers = {
	'Authorization': BEARER_TOKEN,
	'Cookie': 'personalization_id="v1_3UimKLKcTq6SudD+zOZKcA=="; guest_id=v1%3A160071275276748192'
	}

	response = requests.request("GET", url, headers=headers, data=payload, params=params)

	followers = response.json()
	#print(followers)
	#print()
	#print()

	f = open("usernames.txt", "a")
	for i in followers["data"]:
		#print(i["username"])
		f.write(i["username"] + "\n")
	f.close()

	if "next_token" in followers["meta"].keys():
		return followers["meta"]["next_token"]
	else:
		return "Done"



	

def checkFollowers():
	with open("applicants.txt", "r") as file:
			applicants = file.read().split("\n")
	
	with open("usernames.txt", "r") as file:
		followers = file.read().split("\n")
	

	for applicant in applicants:
		if applicant in followers:
			print(applicant)
	
	#print(followers)


main()