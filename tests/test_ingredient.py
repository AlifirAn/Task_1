from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    
    def test_ingredient_get_name_set_sour_cream_return_sour_cream(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 150)

        assert ingredient.get_name() == "sour cream"

    def test_ingredient_get_price_set_fifty_return_fifty(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 50)
        
        assert ingredient.get_price() == 50

    def test_ingredient_get_type_set_souce_return_souce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 80)
        
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE