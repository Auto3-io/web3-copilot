from pathlib import Path
import yaml
import pandas as pd
import pandas as pd
from ast import literal_eval


class LazyLoadedERC20:
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

    def get_contract_address(self, symbol, chain_name):
        df = self.get_dataframe()
        contract_addresses = df.loc[df['symbol'] ==
                                    symbol, 'contract_addresses'].values[0]
        for contract in contract_addresses:
            if contract['platform'] == chain_name:
                return contract['contract_address']
        return None


class LazyLoadedContract:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self._df = None

    def _load_data(self):
        df = pd.read_csv(self.csv_file)
        df['symbol'] = df['symbol'].str.lower()
        df['chain'] = df['chain'].str.lower()
        return df

    def get_dataframe(self):
        if self._df is None:
            self._df = self._load_data()
        return self._df

    def get_contract_abi(self, symbol):
        df = self.get_dataframe()
        abi = df.loc[df['symbol'] == symbol, 'abi'].values[0]

        return abi

    def get_contract_address(self, symbol, chain_name, contract_name):
        df = self.get_dataframe()
        address = df.loc[(df['symbol'] == symbol) & (df['chain'] == chain_name) & (
            df['name'] == contract_name), 'address'].values[0]

        return address


erc20_df = LazyLoadedERC20(Path(__file__).with_name('erc20.csv'))
contract_df = LazyLoadedContract(Path(__file__).with_name('contract.csv'))


def get_protocols():
    p = Path(__file__).with_name('protocols.yaml')
    with p.open('r') as f:
        protocols = yaml.safe_load(f.read())
    return protocols


def get_erc20_address(symbol, chain_name):
    return erc20_df.get_contract_address(symbol, chain_name)


def get_contract_address(protocol, chain_name, contract_name):
    return contract_df.get_contract_address(protocol, chain_name, contract_name)


def get_contract_abi(protocol):
    return contract_df.get_contract_abi(protocol)


__all__ = ['get_protocols', 'get_erc20_address', 'get_erc20_abi']
