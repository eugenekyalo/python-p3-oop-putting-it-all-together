# testing/shoe_test.py

from lib.shoe import Shoe

class TestShoe:
    def test_has_brand_and_size(self):
        stan_smith = Shoe("Adidas", 9)
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9
