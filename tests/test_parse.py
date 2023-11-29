import sys
import os
import unittest
from pathlib import Path

log_path = Path(os.environ["SPLUNK_HOME"] + "/var/log/splunk")
log_path.mkdir(parents=True, exist_ok=True)
(log_path / Path("utbox.log")).write_text("")

path_to_add = os.path.abspath(os.path.join(__file__, '..','..','utbox', 'bin'))
sys.path.append(path_to_add)
