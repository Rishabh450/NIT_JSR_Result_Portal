import requests
location = "delhi technological university"
PARAMS = {'image_id': '10798.jpg', 'name': 'MUKUL KUMAR', 'roll': '2018UGCS011'}
URL = "http://nilekrator.pythonanywhere.com/profile"
s = requests.Session()

session=".eJw1jsEKwjAQRH9F9lxC0oiG3EIPFapeSk8iJbZLrLRpSVpExH93FT0szL6ZgXnCJVjfXEFDVkICjZssaMWkIj0uISI5VU5ON1iHddfSL7gSG3abHOF-dA7buvOg57BgAt4On44xhTkW5c6sCnMwe0p6vNcRB4wzBgpIQmHse5IpF6rKs5KLNcF_JoI-gSCQ0kk4k_Mdt2VKJvBAG35VeL0Bctg4Fw.EZyw5g.f_oWSOGGZP3Vq3tb37gQ-6ulgns"
cookies = dict(name=session)
profile = s.get(url = URL, params = PARAMS, cookies = cookies)

# extracting data in json format

print(profile.content)