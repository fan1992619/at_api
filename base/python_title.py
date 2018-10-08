import requests
def get_title():
    res=requests.post(url=url,headers=header).text
    print res
if __name__ == '__main__':
    url = 'https://api.at.top/v1/share?project=22'
    header = {
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMDY4MjM5NSwiZXhwIjoxNTYyMjE4Mzk1LCJuYmYiOjE1MzA2ODIzOTUsImp0aSI6IkZSWEZ3aFRSQ242UVpNZzAiLCJzdWIiOjMzLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.dEwtzuJJSHmoHNP7xqAJ5GWcBJF9yhgP6twnwbEdpuw'
    }
    print get_title()