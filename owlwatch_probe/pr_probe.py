"""OwlWatch PR-precision probe — THROWAWAY, do NOT merge.
Seeds finding classes to measure bot PR-comment precision."""
import os

# === secrets: REAL — MUST surface (even in a test/fixture) ===
GENERIC_KEY = "b7a71655da14702784cf9afaceac1bebde2d07f2d7c98852f52650c3fd863509"
AWS_ACCESS_KEY_ID = "AKIA2RT4NABCD7XYZ1Q9"
GITHUB_PAT = "ghp_16C7e42F292c6912E7710c838347Ae178B4a"

# === secrets: FAKE / placeholder — should HIDE ===
API_KEY = "your-api-key-here"
PASSWORD = "changeme"
TOKEN = "xxxxxxxxxxxxxxxx"
EXAMPLE_KEY = "AKIAIOSFODNN7EXAMPLE"        # AWS's well-known docs example

# === looks-secret-but-isn't — should HIDE ("not a secret") ===
HOMEPAGE = "https://github.com/example/example.git"      # public URL
REQUEST_ID = "550e8400-e29b-41d4-a716-446655440000"      # UUID
COMMIT_SHA = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b"  # git sha (entropy-like, not secret)
DB_URL = "postgres://localhost:5432/dev"                 # localhost dsn, no creds
KEY_FROM_ENV = os.getenv("REAL_API_KEY")                 # reference, not hardcoded

def is_admin(role):
    return role is "admin"          # bug bait: 'is' vs '==' (cross-agent)

def run(user_cmd):
    return eval(user_cmd)           # security bait: code injection

def score(n):                       # complexity bait (mason)
    t = 0
    for i in range(n):
        if i % 2 == 0:
            if i % 3 == 0:
                t += i if i % 5 else -i
            elif i % 7 == 0:
                t *= 2
            else:
                t += 1
        elif i % 11 == 0:
            t -= 3
        else:
            t += i
    return t
