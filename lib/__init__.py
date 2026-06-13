"""
lib/__init__.py
Automation toolkit package.
Exposes core utilities for log generation and API data fetching.
"""

from .generate_log import generate_log

__all__ = ["generate_log"]