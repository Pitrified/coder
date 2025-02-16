"""Test that the environment variables are available."""

import os

import pytest


def test_env_vars() -> None:
    """The environment var CODER_SAMPLE_ENV_VAR is available."""
    assert "CODER_SAMPLE_ENV_VAR" in os.environ
    assert os.environ["CODER_SAMPLE_ENV_VAR"] == "sample"
