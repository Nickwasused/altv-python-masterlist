from altvcdn import get_version_info, Branch, Platform, Files


# general functions
def test_get_version_info():
    version = get_version_info(Branch.Release, Files.JavaScript, Platform.Linux)
    assert type(version) is dict or version is None
