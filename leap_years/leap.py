FIRST_GREGORIAN_YEAR = 1583


class Year(int):
    def is_leap(self):
        if self < FIRST_GREGORIAN_YEAR:
            raise NotGregorianYear(self)
        if self % 400 == 0:
            return True
        if self % 100 == 0:
            return False
        return self % 4 == 0


class NotGregorianYear(Exception):
    pass
