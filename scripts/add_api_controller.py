from pathlib import Path

from cuelebre_vault.shared.constants import Paths

submodules: tuple[str, ...] = ("infrastructure", "domain", "application")


def create_python_module(path: Path):
    if path.exists():
        raise ValueError(f"Module {path.name} already exists. Skipping controller creation")
    print(f"Creating module with name: {path.name}")
    path.mkdir(exist_ok=True)
    path.joinpath("__init__.py").touch(exist_ok=True)


if __name__ == "__main__":
    controller_name: str = input("Name of controller to add: ")
    print(f"Creating {controller_name} controller:")
    try:
        controller_path: Path = Paths.SRC.joinpath(controller_name)
        create_python_module(controller_path)
        print("Adding Hexagonal structure")
        for submodule in submodules:
            submodule_path: Path = controller_path.joinpath(submodule)
            create_python_module(submodule_path)
        print("Controller structure creation Done")
    except ValueError as e:
        print(e)
