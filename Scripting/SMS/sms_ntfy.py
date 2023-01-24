import requests

requests.post(
    "https://ntfy.sh/test", data="Backup successful 😀".encode(encoding="utf-8")
)
