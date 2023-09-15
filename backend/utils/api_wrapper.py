import requests


class ThreeDBinPackingAPI:
    def __init__(self, payload: dict):
        self.api_key = "c0ac439060d83ae3edd654bcdcc71271"
        self.username = "moroh69760@twugg.com"
        self.base_url = "https://global-api.3dbinpacking.com/packer/findBinSize"  # Replace with the actual API base URL
        self.payload = payload

    @staticmethod
    def _get_headers():
        headers = {
            'Content-Type': 'application/json'
        }
        return headers

    def _construct_payload(self):
        self.payload.update({
            "username": self.username,
            "api_key": self.api_key,
            "params": {
                "images_background_color": "255,255,255",
                "images_bin_border_color": "59,59,59",
                "images_bin_fill_color": "230,230,230",
                "images_item_border_color": "214,79,79",
                "images_item_fill_color": "177,14,14",
                "images_item_back_border_color": "215,103,103",
                "images_sbs_last_item_fill_color": "99,93,93",
                "images_sbs_last_item_border_color": "145,133,133",
                "images_width": 100,
                "images_height": 100,
                "images_source": "file",
                "images_sbs": 1,
                "item_coordinates": 1,
                "images_complete": 1,
                "images_separated": 1,
                "images_version": 2
            }
        })

    def make_request(self, method="POST"):
        url = f"{self.base_url}"
        headers = self._get_headers()

        try:
            self._construct_payload()
            response = requests.request(method, url, headers=headers, json=self.payload)

            # Handle response status codes and errors here
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Request to {url} failed: {str(e)}")

    def get_payload(self):
        return self.payload
