import os
from datetime import datetime

import json
import hashlib


SECRET_KEY = os.getenv("SECRET_KEY")


def generate_auth_token():
    data = {
        "timestamp": str(datetime.now().timestamp()),
        "secret_key": SECRET_KEY
    }
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
