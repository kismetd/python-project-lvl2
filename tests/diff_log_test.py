from gendiff.diff_log import get_diff


def test_generate_flat_log():
    d1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }
    d2 = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    expected = {
        "timeout": {"status": "changed", "old": 50, "new": 20},
        "host": {"status": "unchanged", "value": "hexlet.io"},
        "verbose": {"status": "added", "value": True},
        "proxy": {"status": "removed", "value": "123.234.53.22"},
        "follow": {"status": "removed", "value": False},
    }
    assert get_diff(d1, d2) == expected
