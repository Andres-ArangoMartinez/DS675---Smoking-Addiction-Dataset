"""Small regression checks for evidence-handling failures, using synthetic inputs."""

import hashlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

import verify


class EvidenceChecks(unittest.TestCase):
    def expected(self, raw, rows=2, missing=1):
        return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
                "git_blob_sha1": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest(),
                "rows": rows, "columns": 3, "participants": 1,
                "duplicate_participant_day_keys": 0, "days_per_participant": [1, 2],
                "missing_Overall_Craving_Score": missing}

    def test_duplicate_key_cannot_masquerade_as_complete_panel(self):
        raw = b"Participant_ID,Day_Number,Overall_Craving_Score\nA,1,0\nA,1,\n"
        results = {c["name"]: c for c in verify.csv_checks(raw, self.expected(raw))}
        self.assertEqual(results["duplicate_participant_day_keys"]["status"], "failed")
        self.assertEqual(results["every_participant_has_exact_day_coverage"]["status"], "failed")

    def test_zero_is_observed_and_blank_remains_missing(self):
        raw = b"Participant_ID,Day_Number,Overall_Craving_Score\nA,1,0\nA,2,\n"
        self.assertTrue(all(c["status"] == "passed" for c in
                            verify.csv_checks(raw, self.expected(raw))))

    def test_malformed_width_and_empty_csv_are_rejected(self):
        for raw in (b"", b"Participant_ID,Day_Number,Overall_Craving_Score\nA,1,0,extra\n"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                verify.csv_checks(raw, self.expected(raw))

    def test_ambiguous_archive_is_rejected_without_extracting(self):
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.writestr("one/data.csv", "x\n1\n")
            archive.writestr("two/data.csv", "x\n2\n")
        with self.assertRaisesRegex(ValueError, "exactly one"):
            verify.archive_csv(buffer.getvalue(), "data.csv")

    def test_missing_license_is_a_failed_check(self):
        expected = {"id": 1, "ref": "owner/data", "version": 1,
                    "reported_license": "CC0: Public Domain"}
        results = verify.metadata_checks(
            {"id": 1, "ref": "owner/data", "currentVersionNumber": 1}, expected, "test")
        self.assertEqual(results[-1]["status"], "failed")

    def test_existing_output_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "existing.json"
            original = b'{"historical":true}\n'
            output.write_bytes(original)
            result = subprocess.run([sys.executable, str(verify.HERE / "verify.py"),
                                     "--output", str(output)], capture_output=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(output.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
