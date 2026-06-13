"""
generate_log.py (root-level shim)
Allows direct import of generate_log without the lib. prefix.
The actual implementation lives in lib/generate_log.py.
"""

from lib.generate_log import generate_log

__all__ = ["generate_log"]