#!/usr/bin/env python3

class FetchError(Exception):
    """There has been an error while fetching remote data."""
    pass

class NoData(Exception):
    """No valid data got fetched."""
    pass