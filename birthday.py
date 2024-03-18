



def cek_birthday(token):
    import requests,json
    from requests import get as elite
    url="https://graph.facebook.com/v19.0/me?fields=birthday&access_token="+token
    rq=elite(url).json()
    birthday=rq["birthday"]
    return birthday


print(cek_birthday(token))
