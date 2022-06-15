class PriceError(Exception):
    """ Exception for negative price. """

    def __str__(self):
        return 'Price can not be less then 0!'


class DepositError(Exception):
    """ Exception for negative deposit. """

    def __str__(self):
        return 'Deposit can not be less then 0!'


class TermError(Exception):
    """ Exception for negative term. """

    def __str__(self):
        return 'Term can not be less then 0!'
