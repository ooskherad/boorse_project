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
        self.name_en = name_en
        self.symbol_name = symbol_name
        self.company_digit_code12 = company_digit_code12
        self.symbol_digit_code12 = symbol_digit_code12
        self.symbol_digit5 = symbol_digit5
        self.company_digit4 = company_digit4
        self.market = market
        self.table_code = table_code
        self.industry_group_code = industry_group_code
        self.industry_subgroup_code = industry_subgroup_code
        self.industry_group_name = industry_group_name
        self.industry_subgroup_name = industry_subgroup_name
        self.base_volume = base_volume

