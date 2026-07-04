"""Tests for the public diagnostics API wrapper."""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import pydepgate.api as api
from pydepgate.diagnostics.model import DoctorReport


class TestDoctorApi(unittest.TestCase):
    def test_doctor_api_returns_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = {
                "XDG_CACHE_HOME": str(Path(tmp) / "cache"),
                "XDG_CONFIG_HOME": str(Path(tmp) / "config"),
                "XDG_DATA_HOME": str(Path(tmp) / "data"),
            }
            with mock.patch.dict(os.environ, env, clear=True):
                report = api.doctor(include_event_smoke=False)

        self.assertIsInstance(report, DoctorReport)
        self.assertIn("checks", report.to_dict())
        self.assertTrue(any(check.component == "policies" for check in report.checks))


if __name__ == "__main__":
    unittest.main()
