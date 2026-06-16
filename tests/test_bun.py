from bun import Bun

class TestBun:

    def test_bun_get_name_set_black_bun_return_black_bun(self):
        bun = Bun("black bun", 150)

        assert bun.get_name() == "black bun"

    def test_bun_get_price_set_hundred_return_hundred(self):
        bun = Bun("white bun", 100)

        assert bun.get_price() == 100
