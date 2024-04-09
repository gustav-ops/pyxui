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
            ss_string = "{}:{}:{}".format(
                config["method"], config["server_password"], config["password"]
            )
            encoded_ss_string = base64.b64encode(ss_string.encode()).decode("utf-8")

            string = "ss://{}@{}:{}#{}".format(
                encoded_ss_string, config["server"], config["port"], config["ps"]
            )

        case _:
            string = None

    return string
