from altvmasterlist import masterlist as altv
from altvmasterlist import enum as altvenum


# general functions
def test_server_stats():
    stats = altv.get_server_stats()
    assert isinstance(stats, dict) or stats


def test_get_servers():
    servers = altv.get_servers()
    assert isinstance(servers, list) or servers


def test_group():
    tmp_server = altv.Server("YMRctiN")
    assert isinstance(tmp_server.group, altvenum.Group)


def test_valid_server_by_id():
    tmp_server = altv.Server("mXFlJSM")
    assert isinstance(tmp_server, altv.Server)


def test_get_server_by_id_avg():
    tmp_server = altv.Server("mXFlJSM")
    avg = tmp_server.get_avg("1d")
    assert isinstance(avg, list)


def test_get_server_by_id_avg_result():
    tmp_server = altv.Server("mXFlJSM")
    players = tmp_server.get_avg("1d", return_result=True)
    assert isinstance(players, int)


def test_get_server_by_id_max():
    tmp_server = altv.Server("mXFlJSM")
    max_stats = tmp_server.get_max("1d")
    assert isinstance(max_stats, list)


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

server = altv.Server("mXFlJSM")


def test_fetch_connect_json():
    connect_json = server.connect_json
    assert isinstance(connect_json, dict)


def test_dtc_url():
    url = server.get_dtc_url()
    assert "altv://connect/" in url


def test_dtc_url_password():
    url = server.get_dtc_url("test")
    assert "altv://connect/" in url and "test" in url and "password" in url


def test_get_permissions():
    permissions = server.permissions
    assert isinstance(permissions, altvenum.Permissions)