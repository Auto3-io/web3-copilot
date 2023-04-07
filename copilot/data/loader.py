from pathlib import Path
import yaml
import pandas as pd
import pandas as pd
from ast import literal_eval


class LazyLoadedDataFrame:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self._df = None

    def _load_data(self):
        df = pd.read_csv(self.csv_file)
        df['contract_addresses'] = df['contract_addresses'].apply(
            lambda x: literal_eval(x))
        return df

    def get_dataframe(self):
        if self._df is None:
            self._df = self._load_data()
        return self._df

    def get_contract_address(self, token_name, chain_name):
        df = self.get_dataframe()
        contract_addresses = df.loc[df['name'] ==
                                    token_name, 'contract_addresses'].values[0]
        for contract in contract_addresses:
            if contract['platform'] == chain_name:
                return contract['contract_address']
        return None


erc20_df = LazyLoadedDataFrame(Path(__file__).with_name('erc20.csv'))


def get_erc20_tokens():
    p = Path(__file__).with_name('erc20.csv')
    df = pd.read_csv(p)
    df['contract_addresses'] = df['contract_addresses'].apply(
        lambda x: literal_eval(x))
    return df


def get_protocols():
    p = Path(__file__).with_name('protocols.yaml')
    with p.open('r') as f:
        protocols = yaml.safe_load(f.read())
    return protocols


__all__ = ['get_protocols', 'get_erc20_tokens']
