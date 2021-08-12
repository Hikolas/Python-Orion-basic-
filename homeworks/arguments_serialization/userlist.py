import argparse
import json


class RepetOfInfo(Exception):
    pass

def operations():
    for data in users_data:
        if args.username == data.get("username") or args.email == data.get("email"):
            raise RepetOfInfo

parser = argparse.ArgumentParser()

parser.add_argument("--username", help="Your user username")
parser.add_argument("--email", help="Your user email")
args = parser.parse_args()
user_dict = {}

if args.username:
    user_dict['username'] = args.username

if args.email:
    user_dict['email'] = args.email

user_file = open('users.json', 'r')
users_data = json.loads(user_file.readline())
user_file.close()

try:
    operations()
except RepetOfInfo:
    print("Error: This mail or username is in use")
else:
    users_data.append(user_dict)

user_file = open('users.json', 'w')
user_file.write(json.dumps(users_data))
user_file.close()