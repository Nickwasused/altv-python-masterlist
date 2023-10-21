#!/usr/bin/env python3
from requests.adapters import HTTPAdapter, Retry
from dataclasses import dataclass
from json import dumps
from enum import Enum
import requests
import logging
import secrets

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)


class MasterlistUrls(Enum):
    """This class is used for the masterlist submodule. It provides all urls needed."""
    all_server_stats = "https://api.alt-mp.com/servers/info"
    all_servers = "https://api.alt-mp.com/servers"
    specific_server = "https://api.alt-mp.com/servers/{}"
    specific_server_average = "https://api.alt-mp.com/servers/{}/avg/{}"
    specific_server_maximum = "https://api.alt-mp.com/servers/{}/max/{}"


class Extra(Enum):
    """This class defines extra values."""
    user_agent = "AltPublicAgent"
    default_password = "17241709254077376921"


def request(url: str, server: any = None) -> dict | None:
    """This is the common request function to fetch remote data.

    Args:
        url (str): The Url to fetch.
        server (Server): An alt:V masterlist or altstats Server object.

    Returns:
        None: When an error occurred. But exceptions will still be logged!
        json: As data
    """
    # Use the User-Agent: AltPublicAgent, because some servers protect their CDN with
    # a simple User-Agent check e.g. https://luckyv.de does that
    with requests.session() as session:
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        session.mount('http', HTTPAdapter(max_retries=retries))
        if "http://" in url and server and not server.useCdn:
            logging.warning(f"server is not using cdn. can't fetch connect.json")
            return None
        else:
            session.headers = {
                'User-Agent': Extra.user_agent.value,
                'content-type': 'application/json; charset=utf-8'
            }

        try:
            api_request = session.get(url, timeout=20)
            if api_request.status_code != 200:
                logging.warning(f"the request returned nothing.")
                return None
            else:
                return api_request.json()
        except Exception as e:
            logging.error(e)
            return None


class Permissions:
    """This is the Permission class used by get_permissions.

    Returns:
        Required: The required permissions of an alt:V server. Without them, you can not play on the server.
        Optional: The optional permissions of an alt:V server. You can play without them.
    """
    @dataclass
    class Required:
        """Required Permissions of an alt:V server.

        Attributes:
        ----------
            screen_capture (bool): This allows a screenshot to be taken of the alt:V process (just GTA) and any webview
            webrtc (bool): This allows peer-to-peer RTC inside JS
            clipboard_access (bool): This allows to copy content to users clipboard
        """
        screen_capture: bool = False
        webrtc: bool = False
        clipboard_access: bool = False

    @dataclass
    class Optional:
        """Optional Permissions of an alt:V server.

        Attributes:
        ----------
            screen_capture (bool): This allows a screenshot to be taken of the alt:V process (just GTA) and any webview
            webrtc (bool): This allows peer-to-peer RTC inside JS
            clipboard_access (bool): This allows to copy content to users clipboard
        """
        screen_capture: bool = False
        webrtc: bool = False
        clipboard_access: bool = False
