import hello


def test_add():
    assert hello.add(1234, 67588) == 1234 + 67588
    assert hello.add(-869, 7656) == (-869) + 7656
    assert hello.add(-98, -756) == (-98) + (-756)
    assert hello.add(0, 65) == 0 + 65
