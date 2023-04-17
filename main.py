from pic_vk import VKONTAKTE
from yadisk import YandexDisk
import datetime as dt
import json


def save_photos(vk_id, y_token, count=5):
    url = "https://oauth.vk.com/authorize?client_id=51601563&redirect_uri=https://" \
          "oauth.vk.com/blank.html&display=page&scope=photos&response_type=token"
    print(url)
    token = input("go to link and enter token")

    photos = VKONTAKTE(token)
    photos = photos.get_photos(vk_id)

    yad = YandexDisk(y_token)

    if "error" in photos:
        print(photos["error"]["error_msg"])
    else:
        info = {}
        folder_name = dt.datetime.now().strftime("%d-%m-%Y")
        yad.crt_folder(folder_name)
        info[folder_name] = []

        for item in photos["response"]["items"]:
            likes = item["likes"]["count"]
            photo, p_type = item["sizes"][-1]["url"], item["sizes"][-1]["type"]
            print(likes, photo, p_type)
            now = int(dt.datetime.now().timestamp())
            name = "{}/{}_{}".format(folder_name, likes, now)
            info[folder_name].append({
                "file_name": "{}_{}.jpg".format(likes, now),
                "size": p_type
            })
            yad.upload_file_to_disk(name, photo)
            count -= 1
            if not count:
                break

        with open("results.json", "w") as f:
            json.dump(info, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    my_id = input("enter vk id:")
    my_token = input("enter YD token:")
    save_photos(my_id, my_token)