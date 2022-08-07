from gendiff.diff_log import generate_log


def test_generate_flat_log():
    d1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }
    d2 = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    expected = [
        {"property": "follow", "values": {"old": "False"}},
        {"property": "host", "values": {"unchanged": "hexlet.io"}},
        {"property": "proxy", "values": {"old": "123.234.53.22"}},
        {"property": "timeout", "values": {"old": "50", "new": "20"}},
        {"property": "verbose", "values": {"new": "True"}},
    ]
    assert generate_log(d1, d2) == expected
