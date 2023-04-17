import requests

class VKONTAKTE:
    def __init__(self, token):
        self.token = token

    def get_photos(self, vk_id):
        token = self.token
        url = "https://api.vk.com/method/photos.get"
        params = {
            "owner_id": "{}".format(vk_id),
            "album_id": "profile",
            "access_token": token,
            "v": "5.131",
            "rev": "0",
            "extended": "1"
        }
        res = requests.get(url, params=params)
        return res.json()