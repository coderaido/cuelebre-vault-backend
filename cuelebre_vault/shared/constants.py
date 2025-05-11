from pathlib import Path
from typing import Final


class Paths:
    ROOT: Final[Path] = Path(__file__).resolve().parent.parent.parent
    SRC: Final[Path] = ROOT.joinpath("cuelebre_vault")


class Auth:
    TOKEN_HEADER: Final[str] = "Authorization"
    JWT_ALGORITHM: Final[str] = "HS256"
