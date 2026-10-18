import project_template


def test_version_matches_pyproject():
    assert project_template.__version__ == "0.1.0"
