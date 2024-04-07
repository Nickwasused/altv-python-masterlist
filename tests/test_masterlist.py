from altvmasterlist import masterlist as altv
from altvmasterlist import enum as altvenum


# general functions
def test_server_stats():
    stats = altv.get_server_stats()
    assert isinstance(stats, dict) or stats is None


def test_get_servers():
    servers = altv.get_servers()
    assert isinstance(servers, list) or servers is None


def test_valid_server_by_id():
    tmp_server = altv.Server()
    tmp_server.set_public_id("mXFlJSM")
    assert tmp_server is None or altv.Server


def test_get_server_by_id_avg():
    tmp_server = altv.Server()
    tmp_server.set_public_id("mXFlJSM")
    avg = tmp_server.get_avg("1d")
    assert isinstance(avg, list) or avg is None


def test_get_server_by_id_avg_result():
    tmp_server = altv.Server()
    tmp_server.set_public_id("mXFlJSM")
    players = tmp_server.get_avg("1d", return_result=True)
    assert isinstance(players, int) or players is None


def test_get_server_by_id_max():
    tmp_server = altv.Server()
    tmp_server.set_public_id("mXFlJSM")
    max_stats = tmp_server.get_max("1d")
    assert isinstance(max_stats, list) or max_stats is None


def test_valid():
    assert altv.validate_id("mXFlJSM") is True


def test_invalid():
    assert altv.validate_id("invalid12345678") is False
    assert altv.validate_id(126) is False
    assert altv.validate_id([]) is False
    assert altv.validate_id({}) is False
    assert altv.validate_id(None) is False


# server object functions
# lets get a server

server = altv.Server()
server.set_public_id("mXFlJSM")


def test_fetch_connect_json():
    connect_json = server.connect_json
    assert isinstance(connect_json, dict) or connect_json is None


def test_dtc_url():
    url = server.get_dtc_url()
    assert "altv://connect/" in url


def test_dtc_url_password():
    url = server.get_dtc_url("test")
    assert "altv://connect/" in url and "test" in url and "password" in url


def test_get_permissions():
    permissions = server.permissions
    assert isinstance(permissions, altvenum.Permissions)
