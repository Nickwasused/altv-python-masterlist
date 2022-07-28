import altstats as altv


# general functions
def test_get_server_stats():
    stats = altv.get_server_stats()
    assert type(stats) is list or stats is None


def test_get_servers_average():
    avg = altv.get_servers_average()
    assert type(avg) is tuple or avg is None


def test_get_servers():
    servers = altv.get_servers()
    assert type(servers) is list or servers is None


def test_get_server_by_id():
    server = altv.get_server_by_id(86)
    assert type(server) is altv.Server or server is None


def test_validate_id():
    assert altv.validate_id(86) is True


def test_validate_id_invalid():
    assert altv.validate_id("invalid") is False


# server object functions
# lets get a server

server = altv.get_server_by_id(86)


def test_get_json():
    json = server.get_json()
    assert type(json) is dict or json is None


def test_dtc_url():
    url = server.get_dtc_url()
    assert "altv://connect/" in url


def test_dtc_url_password():
    url = server.get_dtc_url("test")
    assert "altv://connect/" in url and "test" in url and "password" in url


def test_get_permissions():
    permissions = server.get_permissions()
    assert type(permissions) is dict or permissions is None