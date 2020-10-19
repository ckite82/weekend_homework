    def test_add_or_remove_cash__add(self):
        add_or_remove_cash(self.cc_pet_shop,10)
        cash = get_total_cash(self.cc_pet_shop)
        self.assertEqual(1010, cash)

def add_or_remove_cash(dictionary, cash):
    dictionary["admin"]["total_cash"] += cash
    return get_total_cash

    def test_stock_count(self):
        count = get_stock_count(self.cc_pet_shop)
        self.assertEqual(6, count)
    
def get_stock_count(dictionary):
    return len(dictionary["pets"])