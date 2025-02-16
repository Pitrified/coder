"""Test the coder paths."""

import pytest

from coder.config.coder_config import get_coder_paths


def test_coder_paths() -> None:
    """Test the coder paths."""
    coder_paths = get_coder_paths()
    assert coder_paths.src_fol.name == "coder"
    assert coder_paths.root_fol.name == "coder"
    assert coder_paths.data_fol.name == "data"
