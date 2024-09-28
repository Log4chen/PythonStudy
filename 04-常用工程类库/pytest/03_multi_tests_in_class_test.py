# 将多个测试方法包含在一个class中，class名称必须以 Test 开头
class TestInClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert 'o' not in x