import requests
s = requests.session()
s.keep_alive = False
requests.adapters.DEFAULT_RETRIES = 5
payload={
	"username": 17186382422,
	"password": 123456,
	"repassword": 123456
}
r=requests.get('https://kennethreitz.org', verify=False)
# r=requests.post('https://www.wanandroid.com/user/register',headers={'Connection':'close'})
s = requests.session()

s.keep_alive = False

print(r.text)
