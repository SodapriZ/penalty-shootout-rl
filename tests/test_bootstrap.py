"""Bootstrap test suite to keep CI green during initial setup."""


def test_bootstrap_repository_layout() -> None:
    """Ensure the package is importable and exposes basic metadata."""
    import penalty_shootout_rl

    assert isinstance(penalty_shootout_rl.__version__, str)
    assert penalty_shootout_rl.__version__
