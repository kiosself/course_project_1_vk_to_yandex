import requests
from pprint import pprint


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }

    def get_files_list(self):
        files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, path_to_our_file):

        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, requests.get(path_to_our_file))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        return response

    def crt_folder(self, how_to_name="new"):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        url = "%s?%s" % (url, "path={}".format(how_to_name))
        uns = requests.put(url, headers=self.get_headers())
        return uns