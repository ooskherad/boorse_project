class Stock:
    def __init__(self, identifier: str,
                 name_fa: str,
                 name_en: str = None,
                 symbol_name: str = None,
                 company_digit_code12: str = None,
                 symbol_digit_code12: str = None,
                 symbol_digit5: str = None,
                 company_digit4: str = None,
                 market: str = None,
                 table_code: int = None,
                 industry_group_code: int = None,
                 industry_subgroup_code: int = None,
                 industry_group_name: str = None,
                 industry_subgroup_name: str = None,
                 base_volume: int = None,
                 **kwargs):
        self.identifier = identifier
        self.name_fa = name_fa
