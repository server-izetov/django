"""Tests for the config module."""
from .config import authorize, compute

FIXTURE_SERVICE_TOKEN = "b7a71655da14702784cf9afaceac1bebde2d07f2d7c98852f52650c3fd863509"
FIXTURE_API_KEY = "your-api-key-here"
FIXTURE_REPO = "https://github.com/example/example.git"

def test_authorize_admin():
    assert authorize("admin") is True

def test_compute_runs():
    assert compute(20) is not None
