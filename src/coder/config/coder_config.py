"""Coder project configuration."""

from loguru import logger as lg

from coder.config.coder_paths import CoderPaths
from coder.config.singleton import Singleton


class CoderConfig(metaclass=Singleton):
    """Coder project configuration."""

    def __init__(self) -> None:
        lg.info(f"Loading Coder config")
        self.paths = CoderPaths()

    def __str__(self) -> str:
        s = "CoderConfig:"
        s += f"\n{self.paths}"
        return s

    def __repr__(self) -> str:
        return str(self)


def get_coder_config() -> CoderConfig:
    """Get the coder config."""
    return CoderConfig()


def get_coder_paths() -> CoderPaths:
    """Get the coder paths."""
    return get_coder_config().paths
