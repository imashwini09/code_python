from Adapters.BankAdapterAbc import BankAdapterAbc
from Banks.IciciBank import IciciBank


class IciciBankAdapter(BankAdapterAbc):
    def __init__(self):
        self.bank = IciciBank()

    def checkBalance(self):
        return self.bank.bal()