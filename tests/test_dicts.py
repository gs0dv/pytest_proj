import pytest

from utils.dicts import get_val

data = {"vcs": "mercurial"}

def test_get_val():
    assert get_val(data, "vcs") == "mercurial"
    assert get_val(data, "vcs", "git") == "mercurial"
    assert get_val({}, "vcs", "git") == "git"
    assert get_val({}, "vcs", "bazaar") == "bazaar"
    assert get_val({}) == None
