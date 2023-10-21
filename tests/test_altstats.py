from altvmasterlist import altstats as altv
from altvmasterlist import shared as shared


# general functions
def test_get_server_stats():
    stats = altv.get_server_stats()
    assert type(stats) is list or stats is None


def test_get_servers():
    servers = altv.get_servers()
    assert type(servers) is list or servers is None


def test_get_server_by_id():
    server = altv.Server(86)
    assert type(server) is altv.Server or server is None


def test_validate_id():
    assert altv.validate_id(86) is True


def test_validate_id_invalid():
    assert altv.validate_id("invalid") is False
    assert altv.validate_id([]) is False
    assert altv.validate_id({}) is False
    assert altv.validate_id(None) is False


# server object functions
# lets get a server

server = altv.Server(127)


def test_dtc_url():
    url = server.get_dtc_url()
    assert "altv://connect/" in url


def test_dtc_url_password():
    url = server.get_dtc_url("test")
    assert "altv://connect/" in url and "test" in url and "password" in url


def test_get_permissions():
    permissions = server.permissions
    assert type(permissions) is shared.Permissions or permissions is None