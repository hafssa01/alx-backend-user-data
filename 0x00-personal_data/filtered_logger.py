#!/usr/bin/env python3
"""
Filtered Logger Module
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message."""
    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    return re.sub(pattern, lambda match: f"{match.group(1)}={redaction}", message)
