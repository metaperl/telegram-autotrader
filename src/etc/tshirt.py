"""
Response to
https://www.reddit.com/r/Python/comments/fwq1f3/procedurally_generated_object_attribute/
"""

class Products(object):
    """Sale unit object for GoodPaws' products.
    """
    def __init__(self):
        self.df = get_sheets(scopes, sheet_id, range_name, creds_path)
        self.df = self.df.set_index('order_id')
        dct_sku_dtype = {sku:'int64' for sku in lst_sku}
        self.df = self.df.astype(dct_sku_dtype)

        ##Walee
    walee = [
        't001_walee_S', 't001_walee_M', 't001_walee_L', 't001_walee_XL', 't001_walee_XXL'
    ]

    blues = [
        't001_walee_S', 't001_walee_M', 't001_walee_L', 't001_walee_XL' , 't001_walee_XXL'
    ]

    inventory = {
        'walee': walee,
        'blues' : blues
    }

    def total(self, inventory_index):
        """Total of a particular item.

        Arguments:
            inventory_index - a key into the inventory index (e.g. 'walee' or 'blues' for now.

        Sample usage:
        self.walee_total = self.total('walee')
        self.blues_total = self.total('blues')
        """
        sum = 0
        for key in self.inventory[inventory_index]:
            sum += np.sum(self.df.loc[:, key].values)

        return sum
