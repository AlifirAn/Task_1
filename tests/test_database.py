from database import Database
from bun import Bun
from ingredient import Ingredient

class TestDatabase:

    def test_database_available_buns_returns_buns_list(self):
        db = Database()
        buns = db.available_buns()

        assert isinstance(buns, list)
        assert isinstance(buns[0], Bun)

    def test_database_available_ingredients_returns_ingredients_list(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients, list)
        assert isinstance(ingredients[0], Ingredient)
