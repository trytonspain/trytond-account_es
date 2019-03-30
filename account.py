# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Account', 'AccountTemplate', 'FiscalYear', 'Period',
    'TypeTemplate']


class Account(metaclass=PoolMeta):
    __name__ = 'account.account'

    # TODO
    # @classmethod
    # def __setup__(cls):
    #     super(Account, cls).__setup__()
    #     value = ('efective', 'Efective')
    #     if value not in cls.type.selection:
    #         cls.type.selection.append(value)


class AccountTemplate(metaclass=PoolMeta):
    __name__ = 'account.account.template'

    @classmethod
    def check_xml_record(cls, records, values):
        return True


class FiscalYear(metaclass=PoolMeta):
    __name__ = 'account.fiscalyear'
    code = fields.Char('Code', size=None)

    @classmethod
    def search_rec_name(cls, name, clause):
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            ('code',) + tuple(clause[1:]),
            (cls._rec_name,) + tuple(clause[1:]),
            ]


class Period(metaclass=PoolMeta):
    __name__ = 'account.period'
    code = fields.Char('Code', size=None)

    @classmethod
    def search_rec_name(cls, name, clause):
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            ('code',) + tuple(clause[1:]),
            (cls._rec_name,) + tuple(clause[1:]),
            ]


class TypeTemplate(metaclass=PoolMeta):
    __name__ = 'account.account.type.template'

    @classmethod
    def check_xml_record(cls, records, values):
        return True
