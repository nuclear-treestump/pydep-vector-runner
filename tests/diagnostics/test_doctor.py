"""Tests for pydepgate diagnostics doctor."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from pydepgate.dbs.cvedb import constants as cvedb_constants
from pydepgate.dbs.cvedb import schema as cvedb_schema
from pydepgate.dbs.pdgdb import schema as pdgdb_schema
from pydepgate.diagnostics.doctor import DoctorOptions, run_doctor
from pydepgate.diagnostics.model import DoctorCheck, DoctorReport
from pydepgate.diagnostics.render import render_human, render_json


class TestDoctorModel(unittest.TestCase):
    def test_report_summary_counts_statuses(self):
        report = DoctorReport(
            schema_version=1,
            pydepgate_version="0.test",
            generated_at="2026-01-01T00:00:00+00:00",
            checks=(
                DoctorCheck("A", "runtime", "pass", "ok", "ok"),
                DoctorCheck("B", "runtime", "warn", "warn", "warn"),
                DoctorCheck("C", "runtime", "fail", "fail", "fail"),
                DoctorCheck("D", "daemon", "skip", "skip", "skip"),
            ),
        )

        self.assertEqual(report.summary["pass"], 1)
        self.assertEqual(report.summary["warn"], 1)
        self.assertEqual(report.summary["fail"], 1)
        self.assertEqual(report.summary["skip"], 1)
        self.assertTrue(report.failed)
        self.assertTrue(report.warned)

    def test_check_rejects_unknown_status(self):
        with self.assertRaises(ValueError):
            DoctorCheck("A", "runtime", "mystery", "bad", "bad")


class TestDoctorRenderers(unittest.TestCase):
    def test_json_renderer_outputs_valid_json(self):
        report = DoctorReport(
            schema_version=1,
            pydepgate_version="0.test",
            generated_at="2026-01-01T00:00:00+00:00",
            checks=(DoctorCheck("A", "policies", "skip", "reserved", "later"),),
        )

        payload = json.loads(render_json(report))

        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual(payload["checks"][0]["component"], "policies")

    def test_human_renderer_includes_policy_and_daemon_headings(self):
        report = DoctorReport(
            schema_version=1,
            pydepgate_version="0.test",
            generated_at="2026-01-01T00:00:00+00:00",
            checks=(
                DoctorCheck("P", "policies", "skip", "reserved", "later"),
                DoctorCheck("D", "daemon", "skip", "reserved", "later"),
            ),
        )

        output = render_human(report)

        self.assertIn("Policies", output)
        self.assertIn("Daemon", output)
        self.assertIn("SKIP", output)


class TestRunDoctor(unittest.TestCase):
    def test_fresh_state_has_policy_and_daemon_placeholders(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = {
                "XDG_CACHE_HOME": str(Path(tmp) / "cache"),
                "XDG_CONFIG_HOME": str(Path(tmp) / "config"),
                "XDG_DATA_HOME": str(Path(tmp) / "data"),
            }
            with mock.patch.dict(os.environ, env, clear=True):
                report = run_doctor(DoctorOptions(include_event_smoke=False))

        components = {check.component for check in report.checks}
        statuses = {check.check_id: check.status for check in report.checks}
        self.assertIn("policies", components)
        self.assertIn("daemon", components)
        self.assertEqual(statuses["PDG-DOC-POLICIES-000"], "skip")
        self.assertEqual(statuses["PDG-DOC-DAEMON-000"], "skip")
        self.assertFalse(report.failed)

    def test_event_smoke_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = {
                "XDG_CACHE_HOME": str(Path(tmp) / "cache"),
                "XDG_CONFIG_HOME": str(Path(tmp) / "config"),
                "XDG_DATA_HOME": str(Path(tmp) / "data"),
            }
            with mock.patch.dict(os.environ, env, clear=True):
                report = run_doctor(DoctorOptions(include_event_smoke=True))

        event_checks = [c for c in report.checks if c.component == "events"]
        self.assertEqual(event_checks[-1].status, "pass")

    def test_cvedb_compatible_database_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = {
                "XDG_CACHE_HOME": str(Path(tmp) / "cache"),
                "XDG_CONFIG_HOME": str(Path(tmp) / "config"),
                "XDG_DATA_HOME": str(Path(tmp) / "data"),
            }
            with mock.patch.dict(os.environ, env, clear=True):
                db_path = (
                    Path(tmp)
                    / "cache"
                    / "pydepgate"
                    / "cvedb"
                    / cvedb_constants.CVE_DB_FILENAME
                )
                db_path.parent.mkdir(parents=True)
                conn = cvedb_schema.connect(db_path)
                try:
                    cvedb_schema.initialize_schema(conn)
                    conn.commit()
                finally:
                    conn.close()

                report = run_doctor(DoctorOptions(include_event_smoke=False))

        cvedb_checks = [c for c in report.checks if c.component == "cvedb"]
        self.assertEqual(cvedb_checks[0].status, "pass")

    def test_pdgdb_compatible_database_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = {
                "XDG_CACHE_HOME": str(Path(tmp) / "cache"),
                "XDG_CONFIG_HOME": str(Path(tmp) / "config"),
                "XDG_DATA_HOME": str(Path(tmp) / "data"),
            }
            with mock.patch.dict(os.environ, env, clear=True):
                db_path = Path(tmp) / "data" / "pydepgate" / "pdgdb" / "evidence.db"
                db_path.parent.mkdir(parents=True)
                conn = pdgdb_schema.connect(db_path)
                try:
                    pdgdb_schema.initialize_schema(conn)
                    conn.commit()
                finally:
                    conn.close()

                report = run_doctor(DoctorOptions(include_event_smoke=False))

        pdgdb_checks = [c for c in report.checks if c.component == "pdgdb"]
        self.assertEqual(pdgdb_checks[0].status, "pass")

    def test_bad_rules_env_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = {
                "XDG_CACHE_HOME": str(Path(tmp) / "cache"),
                "XDG_CONFIG_HOME": str(Path(tmp) / "config"),
                "XDG_DATA_HOME": str(Path(tmp) / "data"),
                "PYDEPGATE_RULES_FILE": str(Path(tmp) / "missing.gate"),
            }
            with mock.patch.dict(os.environ, env, clear=True):
                report = run_doctor(DoctorOptions(include_event_smoke=False))

        rules_checks = [c for c in report.checks if c.component == "rules"]
        self.assertEqual(rules_checks[0].status, "fail")
        self.assertTrue(report.failed)


if __name__ == "__main__":
    unittest.main()
