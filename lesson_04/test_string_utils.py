def test_capitalize():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty():
    assert utils.capitalize("") == ""

def test_trim():
        assert utils.trim("   skypro") == "skypro"

def test_trim_without_spaces():
        assert utils.trim("skypro") == "skypro"


from string_utils import StringUtils

utils = StringUtils()


def test_trim_empty():
        assert utils.trim("") == ""

def test_contains_true():
    assert utils.contains("SkyPro", "S") is True


def test_contains_false():
    assert utils.contains("SkyPro", "U") is False


def test_contains_space():
    assert utils.contains("Sky Pro", " ") is True

def test_delete_symbol_letter():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_word():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "U") == "SkyPro"