import pytest

def test_dogtail():
    from youqu3.dogtail import Dogtail
    dock = Dogtail().ele("Btn_文件管理器").click()
    print(dock)
    assert dock

def test_ocr():
    from youqu3.ocr import OCR
    res = OCR.ocr()
    print(res)
    assert res

def test_mousekey():
    from youqu3.mousekey import MouseKey
    res = MouseKey.current_location()
    print(res)
    assert res


if __name__ == '__main__':
    pytest.main()