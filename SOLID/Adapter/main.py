from Adapters.yesBankAdapter import YesBankAdapter
from Payment import Payment

if __name__ == '__main__':
    b = YesBankAdapter()
    p = Payment(b)
    print(p.checkBalance())
    print(type(p.checkBalance()))