from pathlib import Path

from toml import load as load_toml

project_root_path: Path = Path(__file__).parent.parent
if __name__ == "__main__":
    pyproject_file: Path = project_root_path.joinpath("pyproject.toml")
    version_file: Path = project_root_path.joinpath("VERSION")
    project_config: dict = load_toml(pyproject_file)
    project_version: str = project_config["project"]["version"]

    version_file.write_text(project_version)
