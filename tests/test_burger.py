import pytest
from unittest.mock import Mock
from burger import Burger

class TestBurger:
    
    @pytest.fixture
    def burger(self):
        return Burger()
    
    def test_set_buns_sets_correct_bun(self, burger):
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_ingredient_to_list(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_deletes_ingredient_from_list(self, burger):
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    def test_move_ingredient_changes_order(self, burger):
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1


    def test_get_price_calculates_two_buns_one_ing(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == 250

    def test_get_receipt_generates_bun_ing_bun_price(self, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 150
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "chili sauce"
        mock_ingredient.get_price.return_value = 50
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()

        expected_receipt = (
        "(==== black bun ====)\n"
        "= sauce chili sauce =\n"
        "(==== black bun ====)\n\n"
        "Price: 350"
    )
       
        # Проверяем, что в чеке присутствуют все обязательные текстовые блоки
        assert receipt == expected_receipt