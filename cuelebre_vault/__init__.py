from pathlib import Path

version_file: Path = Path(__file__).parent.parent.joinpath("VERSION")
__version__: str = version_file.read_text() or "0.1.0"
