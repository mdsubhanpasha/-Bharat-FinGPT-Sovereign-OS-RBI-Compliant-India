# Copyright (c) 2026 MOHAMMAD SUBHAN PASHA - Zero Trust
import os
class Vault:
    def __init__(self):
        self.inventor = "MOHAMMAD SUBHAN PASHA"
    def get_secret(self, key: str):
        return os.getenv(key, "VAULT_SECRET")
