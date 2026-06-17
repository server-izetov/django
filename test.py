"""Temp file to exercise OwlWatch auto-fix (#402). Safe to delete after testing."""
from os import getcwd, path


def _demo() -> str:
    return getcwd()


def is_admin(role: str) -> bool:
    return role == "admin"
