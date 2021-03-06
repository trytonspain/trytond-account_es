# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.

try:
    from trytond.modules.account_es.tests.test_account_es import (
        suite, create_chart, get_tax)
except ImportError:
    from .test_account_es import suite, create_chart, get_tax

__all__ = ['suite', 'create_chart', 'get_tax']
