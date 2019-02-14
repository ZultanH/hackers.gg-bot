import requests
import re
import json

class netcat:
    def __init__(self, id, challenge = None):
        self.id = id
        page = 'https://hackers.gg/api/users/id/{}/'.format(id)
        self.r = requests.get(page)

        if "<h1>Not Found</h1>" in self.r.text:
            raise ValueError("User not found")

        self.obj = json.loads(self.r.text)
        self.challenge = challenge
        self.userobj = {
            'challenges': [x for x in self.obj if x not in ['exp', 'id', 'name', 'rank']],
            'xp': self.obj['exp'],
            'id': self.obj['id'],
            'name': self.obj['name'],
            'rank': self.obj['rank'],
        }

        
    @property
    def url(self):
        if self.challenge and type(self.challenge) is str:
            pass #do shit here
        else:
            raise ValueError("You need to specify a challenge to use this function")

    @property
    def complete_challenges(self):
        return self.userobj['challenges']

    @property
    def iscomplete(self):
        if self.challenge and type(self.challenge) is str:
            return self.challenge in self.userobj['challenges']
        else:
            raise ValueError("You need to specify a challenge to use this function")
        
    @property
    def points(self):
        return self.userobj['xp']

    @property
    def username(self):
        return self.userobj['name']
        
    @property
    def rank(self):
        return self.userobj['rank']
