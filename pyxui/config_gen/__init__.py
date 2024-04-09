import json
import base64
from urllib.parse import urlencode


def config_generator(protocol: str, config=dict, data: dict = None) -> str:

    string = None

    match protocol:
        case "vmess":
            string = "vmess://" + base64.b64encode(
                json.dumps(config).encode("utf-8")
            ).decode("utf-8")

        case "vless":
            string = "vless://{}@{}:{}?{}#{}".format(
                config["id"],
                config["add"],
                config["port"],
                urlencode(data),
                config["ps"],
            )

        case "shadowsocks":
            string = "ss://{}:{}@{}:{}#{}".format(
                config["method"],
                config["server_password"],
                config["password"],
                config["server"],
                config["port"],
                config["ps"],
            )

        case _:
            string = None

    return string
