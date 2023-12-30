from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)  # are we creating a datatype here?
class DataIngestionCongig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path