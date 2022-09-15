from pytest_cookies import plugin
from pathlib import Path

# path for the pytest cookies framework to find the template to test on
template = str(Path(__file__).parent.parent)
cookies = plugin.Cookies(template=template, output_factory=None, config_file=None)


def test_readme(cookies):
    # cookies.bake creates a temporary version of this template
    result = cookies.bake(template=template)
    readme_file = result.project_path / 'README.md'
    readme_lines = readme_file.read_text().splitlines()
    assert readme_lines[0] == "# ArangoML FeatureStore"


def test_exitcode(cookies):
    result = cookies.bake(template=template)
    assert result.exit_code == 0


def test_exception(cookies):
    result = cookies.bake(template=template)
    print(result.exception)
    assert result.exception is None


def test_name(cookies):
    result = cookies.bake(template=template)
    assert result.project_path.name == "arangomlfeaturestore"


def test_dir(cookies):
    result = cookies.bake(template=template)
    assert result.project_path.is_dir()