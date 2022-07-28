import masterlist as altv


# general functions
def test_server_stats():
    stats = altv.get_server_stats()
    assert type(stats) is dict or stats is None


def test_get_servers():
    servers = altv.get_servers()
    assert type(servers) is list or servers is None


def test_valid_server_by_id():
    server = altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f")
    assert server is None or altv.Server


def test_get_server_by_id_avg():
    avg = altv.get_server_by_id_avg("bb7228a0d366fc575a5682a99359424f", "1d")
    assert type(avg) == list or avg is None


def test_get_server_by_id_avg_result():
    players = altv.get_server_by_id_avg_result("bb7228a0d366fc575a5682a99359424f", "1d")
    assert type(players) is int or players is None


def test_get_server_by_id_max():
    max_stats = altv.get_server_by_id_max("bb7228a0d366fc575a5682a99359424f", "1d")
    assert type(max_stats) == list or max_stats is None


def test_valid():
    assert altv.validate_id("bb7228a0d366fc575a5682a99359424f") is True


def test_invalid():
    assert altv.validate_id("invalid") is False


# server object functions
# lets get a server

server = altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f")


def test_get_json():
    json = server.get_json()
    assert type(json) is dict or json is None


def test_fetch_connect_json():
    connect_json = server.fetch_connect_json()
    assert type(connect_json) is dict or connect_json is None


def test_dtc_url():
    url = server.get_dtc_url()
    assert "altv://connect/" in url


def test_dtc_url_password():
    url = server.get_dtc_url("test")
    assert "altv://connect/" in url and "test" in url and "password" in url


def test_get_permissions():
    permissions = server.get_permissions()
    assert type(permissions) is dict or permissions is None
