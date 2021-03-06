#!/usr/bin/python
# -*- coding: utf-8 -*-
from decimal import Decimal

# TODO: Review commented code:
# - irpf_out_*
# - iva_ISP_compras_16
# - ...

tax_result = {
    (u'irpf_1', u'Retenciones IRPF 1%'): {
        ('in', 'credit'
            ): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_1': (u'IRPF Retenciones practicadas Base Imponible 1%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_1': (u'IRPF Retenciones practicadas Cuota 1%',
            ('credit_tax_amount', 1.0))}, 'tax': 1.0}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_1': (u'IRPF Retenciones practicadas Base Imponible 1%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_1': (u'IRPF Retenciones practicadas Cuota 1%',
            ('invoice_tax_amount', -1.0))}, 'tax': -1.0}},
    (u'irpf_15', u'Retenciones IRPF 15%'): {
        ('in', 'credit'
            ): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_15': (u'IRPF Retenciones practicadas Base Imponible 15%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_15': (u'IRPF Retenciones practicadas Cuota 15%'
            , ('credit_tax_amount', 15.0))}, 'tax': 15.0}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_15': (u'IRPF Retenciones practicadas Base Imponible 15%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_15': (u'IRPF Retenciones practicadas Cuota 15%'
            , ('invoice_tax_amount', -15.0))}, 'tax': -15.0}},
    (u'irpf_18', u'Retenciones IRPF 18%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_18': (
                    u'IRPF Retenciones practicadas Base Imponible 18%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'irpf_cuota_18': (
                    u'IRPF Retenciones practicadas Cuota 18%', (
                        'credit_tax_amount',
                        18.0
                        )
                    )
                },
            'tax': 18.0
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_18': (
                    u'IRPF Retenciones practicadas Base Imponible 18%', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'irpf_cuota_18': (
                    u'IRPF Retenciones practicadas Cuota 18%', (
                        'invoice_tax_amount',
                        -18.0
                        )
                    )
                },
            'tax': -18.0
            }
        },
    (u'irpf_19', u'Retenciones IRPF 19%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_19': (u'IRPF Retenciones practicadas Base Imponible 19%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_19': (u'IRPF Retenciones practicadas Cuota 19%'
            , ('credit_tax_amount', 19.0))}, 'tax': 19.0}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_19': (u'IRPF Retenciones practicadas Base Imponible 19%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_19': (u'IRPF Retenciones practicadas Cuota 19%'
            , ('invoice_tax_amount', -19.0))}, 'tax': -19.0}},
    (u'irpf_195', u'Retenciones IRPF 19,5%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_195': (u'IRPF Retenciones practicadas Base Imponible 19,5%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_195': (u'IRPF Retenciones practicadas Cuota 19,5%'
            , ('credit_tax_amount', 19.5))}, 'tax': 19.5}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_195': (u'IRPF Retenciones practicadas Base Imponible 19,5%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_195': (u'IRPF Retenciones practicadas Cuota 19,5%'
            , ('invoice_tax_amount', -19.5))}, 'tax': -19.5}},
    (u'irpf_195a', u'Retenciones IRPF Arrendamientos 19,5%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_195a': (u'IRPF Retenciones practicadas Arrendamientos Base Imponible 19,5%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_195a': (u'IRPF Retenciones practicadas Arrendamientos Cuota 19,5%'
            , ('credit_tax_amount', 19.5))}, 'tax': 19.5}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_195a': (u'IRPF Retenciones practicadas Arrendamientos Base Imponible 19,5%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_195a': (u'IRPF Retenciones practicadas Arrendamientos Cuota 19,5%'
            , ('invoice_tax_amount', -19.5))}, 'tax': -19.5}},
    (u'irpf_19a', u'Retenciones IRPF Arrendamientos 19%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_19a': (u'IRPF Retenciones practicadas Arrendamientos Base Imponible 19%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_19a': (u'IRPF Retenciones practicadas Arrendamientos Cuota 19%'
            , ('credit_tax_amount', 19.0))}, 'tax': 19.0}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_19a': (u'IRPF Retenciones practicadas Arrendamientos Base Imponible 19%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_19a': (u'IRPF Retenciones practicadas Arrendamientos Cuota 19%'
            , ('invoice_tax_amount', -19.0))}, 'tax': -19.0}},
    (u'irpf_2', u'Retenciones IRPF 2%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_2': (u'IRPF Retenciones practicadas Base Imponible 2%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_2': (u'IRPF Retenciones practicadas Cuota 2%',
            ('credit_tax_amount', 2.0))}, 'tax': 2.0}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_2': (u'IRPF Retenciones practicadas Base Imponible 2%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_2': (u'IRPF Retenciones practicadas Cuota 2%',
            ('invoice_tax_amount', -2.0))}, 'tax': -2.0}},
    (u'irpf_20', u'Retenciones IRPF 20%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_20': (u'IRPF Retenciones practicadas Base Imponible 20%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_20': (u'IRPF Retenciones practicadas Cuota 20%'
            , ('credit_tax_amount', 20.0))}, 'tax': 20.0}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_20': (u'IRPF Retenciones practicadas Base Imponible 20%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_20': (u'IRPF Retenciones practicadas Cuota 20%'
            , ('invoice_tax_amount', -20.0))}, 'tax': -20.0}},
    (u'irpf_20a', u'Retenciones IRPF Arrendamientos 20%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_20a': (u'IRPF Retenciones practicadas Arrendamientos Base Imponible 20%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_20a': (u'IRPF Retenciones practicadas Arrendamientos Cuota 20%'
            , ('credit_tax_amount', 20.0))}, 'tax': 20.0}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_20a': (u'IRPF Retenciones practicadas Arrendamientos Base Imponible 20%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_20a': (u'IRPF Retenciones practicadas Arrendamientos Cuota 20%'
            , ('invoice_tax_amount', -20.0))}, 'tax': -20.0}},
    (u'irpf_21', u'Retenciones IRPF 21%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_21': (u'IRPF Retenciones practicadas Base Imponible 21%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'irpf_cuota_21': (u'IRPF Retenciones practicadas Cuota 21%'
            , ('credit_tax_amount', 21.0))}, 'tax': 21.0}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_21': (u'IRPF Retenciones practicadas Base Imponible 21%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'irpf_cuota_21': (u'IRPF Retenciones practicadas Cuota 21%'
            , ('invoice_tax_amount', -21.0))}, 'tax': -21.0}},
    (u'irpf_35', u'Retenciones IRPF 35%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_35': (
                    u'IRPF Retenciones practicadas Base Imponible 35%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'irpf_cuota_35': (
                    u'IRPF Retenciones practicadas Cuota 35%', (
                        'credit_tax_amount',
                        35.0
                        )
                    )
                },
            'tax': 35.0,
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_35': (
                    u'IRPF Retenciones practicadas Base Imponible 35%', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'irpf_cuota_35': (
                    u'IRPF Retenciones practicadas Cuota 35%', (
                        'invoice_tax_amount',
                        -35.0
                        )
                    )
                },
            'tax': -35.0,
            }
        },
    (u'irpf_37', u'Retenciones IRPF 37%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_37': (
                    u'IRPF Retenciones practicadas Base Imponible 37%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'irpf_cuota_37': (
                    u'IRPF Retenciones practicadas Cuota 37%', (
                        'credit_tax_amount',
                        37.0
                        )
                    )
                },
            'tax': 37.0,
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_37': (
                    u'IRPF Retenciones practicadas Base Imponible 37%', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'irpf_cuota_37': (
                    u'IRPF Retenciones practicadas Cuota 37%', (
                        'invoice_tax_amount',
                        -37.0
                        )
                    )
                },
            'tax': -37.0,
            }
        },
    (u'irpf_7', u'Retenciones IRPF 7%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_7': (
                    u'IRPF Retenciones practicadas Base Imponible 7%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'irpf_cuota_7': (
                    u'IRPF Retenciones practicadas Cuota 7%', (
                        'credit_tax_amount',
                        7.0
                        )
                    )
                },
            'tax': 7.0,
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_7': (
                    u'IRPF Retenciones practicadas Base Imponible 7%', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'irpf_cuota_7': (
                    u'IRPF Retenciones practicadas Cuota 7%', (
                        'invoice_tax_amount',
                        -7.0
                        )
                    )
                },
            'tax': -7.0
            }
        },
    (u'irpf_9', u'Retenciones IRPF 9%'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'irpf_base_9': (
                    u'IRPF Retenciones practicadas Base Imponible 9%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'irpf_cuota_9': (
                    u'IRPF Retenciones practicadas Cuota 9%', (
                        'credit_tax_amount',
                        9.0
                        )
                    )
                },
            'tax': 9.0,
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'irpf_base_9': (
                    u'IRPF Retenciones practicadas Base Imponible 9%', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'irpf_cuota_9': (
                    u'IRPF Retenciones practicadas Cuota 9%', (
                        'invoice_tax_amount',
                        -9.0
                        )
                    )
                },
            'tax': -9.0
            }
        },
#    (u'irpf_out_1', u'Retenciones a cuenta IRPF 1%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_1': (u'IRPF Retenciones a cuenta Base Imponible 1%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_1': (u'IRPF Retenciones a cuenta Cuota 1%'
#            , ('credit_tax_amount', 1.0))}, 'tax': 1.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_1': (u'IRPF Retenciones a cuenta Base Imponible 1%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_1': (u'IRPF Retenciones a cuenta Cuota 1%'
#            , ('invoice_tax_amount', -1.0))}, 'tax': -1.0}},
#    (u'irpf_out_15', u'Retenciones a cuenta IRPF 15%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_15': (u'IRPF Retenciones a cuenta Base Imponible 15%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_15': (u'IRPF Retenciones a cuenta Cuota 15%'
#            , ('credit_tax_amount', 15.0))}, 'tax': 15.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_15': (u'IRPF Retenciones a cuenta Base Imponible 15%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_15': (u'IRPF Retenciones a cuenta Cuota 15%'
#            , ('invoice_tax_amount', -15.0))}, 'tax': -15.0}},
#    (u'irpf_out_18', u'Retenciones a cuenta IRPF 18%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_18': (u'IRPF Retenciones a cuenta Base Imponible 18%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_18': (u'IRPF Retenciones a cuenta Cuota 18%'
#            , ('credit_tax_amount', 18.0))}, 'tax': 18.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_18': (u'IRPF Retenciones a cuenta Base Imponible 18%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_18': (u'IRPF Retenciones a cuenta Cuota 18%'
#            , ('invoice_tax_amount', -18.0))}, 'tax': -18.0}},
#    (u'irpf_out_19', u'Retenciones a cuenta IRPF 19%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_19': (u'IRPF Retenciones a cuenta Base Imponible 19%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_19': (u'IRPF Retenciones a cuenta Cuota 19%'
#            , ('credit_tax_amount', 19.0))}, 'tax': 19.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_19': (u'IRPF Retenciones a cuenta Base Imponible 19%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_19': (u'IRPF Retenciones a cuenta Cuota 19%'
#            , ('invoice_tax_amount', -19.0))}, 'tax': -19.0}},
#    (u'irpf_out_195', u'Retenciones a cuenta IRPF 19,5%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_195': (u'IRPF Retenciones a cuenta Base Imponible 19,5%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_195': (u'IRPF Retenciones a cuenta Cuota 19,5%'
#            , ('credit_tax_amount', 19.5))}, 'tax': 19.5}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_195': (u'IRPF Retenciones a cuenta Base Imponible 19,5%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_195': (u'IRPF Retenciones a cuenta Cuota 19,5%'
#            , ('invoice_tax_amount', -19.5))}, 'tax': -19.5}},
#    (u'irpf_out_195a', u'Retenciones a cuenta IRPF Arrendamientos 19,5%'
#     ): {
#         ('in', 'credit'): {
#             'base': Decimal('-100.00'),
#         'codes': {
#                 u'irpf_base_out_195a': (u'IRPF Retenciones a cuenta Arrendamientos Base Imponible 19,5%'
#         , ('credit_base_amount', Decimal('-100.00'))),
#         u'irpf_cuota_out_195a': (u'IRPF Retenciones a cuenta Arrendamientos Cuota 19,5%'
#         , ('credit_tax_amount', 19.5))}, 'tax': 19.5}, ('in',
#         'invoice'): {
#             'base': Decimal('100.00'),
#         'codes': {
#                 u'irpf_base_out_195a': (u'IRPF Retenciones a cuenta Arrendamientos Base Imponible 19,5%'
#         , ('invoice_base_amount', Decimal('100.00'))),
#         u'irpf_cuota_out_195a': (u'IRPF Retenciones a cuenta Arrendamientos Cuota 19,5%'
#         , ('invoice_tax_amount', -19.5))}, 'tax': -19.5}},
#    (u'irpf_out_19a', u'Retenciones a cuenta IRPF Arrendamientos 19%'
#     ): {
#         ('in', 'credit'): {
#             'base': Decimal('-100.00'),
#         'codes': {
#                 u'irpf_base_out_19a': (u'IRPF Retenciones a cuenta Arrendamientos Base Imponible 19%'
#         , ('credit_base_amount', Decimal('-100.00'))),
#         u'irpf_cuota_out_19a': (u'IRPF Retenciones a cuenta Arrendamientos Cuota 19%'
#         , ('credit_tax_amount', 19.0))}, 'tax': 19.0}, ('in',
#         'invoice'): {
#             'base': Decimal('100.00'),
#         'codes': {
#                 u'irpf_base_out_19a': (u'IRPF Retenciones a cuenta Arrendamientos Base Imponible 19%'
#         , ('invoice_base_amount', Decimal('100.00'))),
#         u'irpf_cuota_out_19a': (u'IRPF Retenciones a cuenta Arrendamientos Cuota 19%'
#         , ('invoice_tax_amount', -19.0))}, 'tax': -19.0}},
#    (u'irpf_out_2', u'Retenciones a cuenta IRPF 2%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_2': (u'IRPF Retenciones a cuenta Base Imponible 2%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_2': (u'IRPF Retenciones a cuenta Cuota 2%'
#            , ('credit_tax_amount', 2.0))}, 'tax': 2.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_2': (u'IRPF Retenciones a cuenta Base Imponible 2%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_2': (u'IRPF Retenciones a cuenta Cuota 2%'
#            , ('invoice_tax_amount', -2.0))}, 'tax': -2.0}},
#    (u'irpf_out_20', u'Retenciones a cuenta IRPF 20%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_20': (u'IRPF Retenciones a cuenta Base Imponible 20%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_20': (u'IRPF Retenciones a cuenta Cuota 20%'
#            , ('credit_tax_amount', 20.0))}, 'tax': 20.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_20': (u'IRPF Retenciones a cuenta Base Imponible 20%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_20': (u'IRPF Retenciones a cuenta Cuota 20%'
#            , ('invoice_tax_amount', -20.0))}, 'tax': -20.0}},
#    (u'irpf_out_20a', u'Retenciones a cuenta IRPF Arrendamientos 20%'
#     ): {
#         ('in', 'credit'): {
#             'base': Decimal('-100.00'),
#         'codes': {
#                 u'irpf_base_out_20a': (u'IRPF Retenciones a cuenta Arrendamientos Base Imponible 20%'
#         , ('credit_base_amount', Decimal('-100.00'))),
#         u'irpf_cuota_out_20a': (u'IRPF Retenciones a cuenta Arrendamientos Cuota 20%'
#         , ('credit_tax_amount', 20.0))}, 'tax': 20.0}, ('in',
#         'invoice'): {
#             'base': Decimal('100.00'),
#         'codes': {
#                 u'irpf_base_out_20a': (u'IRPF Retenciones a cuenta Arrendamientos Base Imponible 20%'
#         , ('invoice_base_amount', Decimal('100.00'))),
#         u'irpf_cuota_out_20a': (u'IRPF Retenciones a cuenta Arrendamientos Cuota 20%'
#         , ('invoice_tax_amount', -20.0))}, 'tax': -20.0}},
#    (u'irpf_out_21', u'Retenciones a cuenta IRPF 21%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_21': (u'IRPF Retenciones a cuenta Base Imponible 21%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_21': (u'IRPF Retenciones a cuenta Cuota 21%'
#            , ('credit_tax_amount', 21.0))}, 'tax': 21.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_21': (u'IRPF Retenciones a cuenta Base Imponible 21%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_21': (u'IRPF Retenciones a cuenta Cuota 21%'
#            , ('invoice_tax_amount', -21.0))}, 'tax': -21.0}},
#    (u'irpf_out_35', u'Retenciones a cuenta IRPF 35%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_35': (
#                    u'IRPF Retenciones a cuenta Base Imponible 35%', (
#                        'credit_base_amount',
#                        Decimal('-100.00')
#                        )
#                    ),
#                u'irpf_cuota_out_35': (
#                    u'IRPF Retenciones a cuenta Cuota 35%', (
#                        'credit_tax_amount',
#                        35.0,
#                        )
#                    )
#                },
#            'tax': 35.0
#            },
#        ('in', 'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_35': (
#                    u'IRPF Retenciones a cuenta Base Imponible 35%', (
#                        'invoice_base_amount',
#                        Decimal('100.00')
#                        )
#                    ),
#                u'irpf_cuota_out_35': (
#                    u'IRPF Retenciones a cuenta Cuota 35%', (
#                        'invoice_tax_amount',
#                        -35.0
#                        )
#                    )
#                },
#            'tax': -35.0
#            }
#        },
#    (u'irpf_out_37', u'Retenciones a cuenta IRPF 37%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_37': (u'IRPF Retenciones a cuenta Base Imponible 37%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_37': (u'IRPF Retenciones a cuenta Cuota 37%'
#            , ('credit_tax_amount', 37.0))}, 'tax': 37.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_37': (u'IRPF Retenciones a cuenta Base Imponible 37%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_37': (u'IRPF Retenciones a cuenta Cuota 37%'
#            , ('invoice_tax_amount', -37.0))}, 'tax': -37.0}},
#    (u'irpf_out_7', u'Retenciones a cuenta IRPF 7%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_7': (u'IRPF Retenciones a cuenta Base Imponible 7%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_7': (u'IRPF Retenciones a cuenta Cuota 7%'
#            , ('credit_tax_amount', 7.0))}, 'tax': 7.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_7': (u'IRPF Retenciones a cuenta Base Imponible 7%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_7': (u'IRPF Retenciones a cuenta Cuota 7%'
#            , ('invoice_tax_amount', -7.0))}, 'tax': -7.0}},
#    (u'irpf_out_9', u'Retenciones a cuenta IRPF 9%'): {
#        ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'irpf_base_out_9': (u'IRPF Retenciones a cuenta Base Imponible 9%'
#            , ('credit_base_amount', Decimal('-100.00'))),
#            u'irpf_cuota_out_9': (u'IRPF Retenciones a cuenta Cuota 9%'
#            , ('credit_tax_amount', 9.0))}, 'tax': 9.0}, ('in',
#            'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                u'irpf_base_out_9': (u'IRPF Retenciones a cuenta Base Imponible 9%'
#            , ('invoice_base_amount', Decimal('100.00'))),
#            u'irpf_cuota_out_9': (u'IRPF Retenciones a cuenta Cuota 9%'
#            , ('invoice_tax_amount', -9.0))}, 'tax': -9.0}},
    (u'iva_IC_compras_10_bc',
     u'IVA 10% Intracomunitario. Bienes corrientes'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
             'codes': {},
             'tax': Decimal('0.00')
             },
         ('in', 'invoice'): {
             'base': Decimal('100.00'),
             'codes': {},
             'tax': Decimal('0.00')
             }
         },
    (u'iva_IC_compras_10_bi',
     u'IVA 10% Intracomunitario. Bienes de inversi\xf3n'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
             'codes': {},
             'tax': Decimal('0.00'),
             },
         ('in', 'invoice'): {
             'base': Decimal('100.00'),
             'codes': {},
             'tax': Decimal('0.00'),
             }
         },
    (u'iva_IC_compras_10_servicios',
     u'IVA 10% Intracomunitario. Servicios'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'), 'codes': {
                 },
            'tax': Decimal('0.00')}, ('in', 'invoice'
            ): {
             'base': Decimal('100.00'), 'codes': {
                 },
            'tax': Decimal('0.00')}},
    (u'iva_IC_compras_21_bc',
     u'IVA 21% Intracomunitario. Bienes corrientes'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
             'codes': {},
             'tax': Decimal('0.00')
             },
         ('in', 'invoice'): {
             'base': Decimal('100.00'),
             'codes': {},
             'tax': Decimal('0.00')
             }
         },
    (u'iva_IC_compras_21_bi',
     u'IVA 21% Intracomunitario. Bienes de inversi\xf3n'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
             'codes': {},
             'tax': Decimal('0.00'),
             },
         ('in', 'invoice'): {
             'base': Decimal('100.00'),
             'codes': {},
             'tax': Decimal('0.00'),
             }
         },
    (u'iva_IC_compras_21_ser', u'IVA 21% Intracomunitario. Servicios'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'), 'codes': {
                 },
         'tax': Decimal('0.00')}, ('in', 'invoice'
         ): {
             'base': Decimal('100.00'), 'codes': {
                 },
         'tax': Decimal('0.00')}},
    (u'iva_IC_compras_4_bc',
     u'IVA 4% Intracomunitario. Bienes corrientes'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'), 'codes': {
                 },
            'tax': Decimal('0.00')}, ('in', 'invoice'
            ): {
             'base': Decimal('100.00'), 'codes': {
                 },
            'tax': Decimal('0.00')}},
    (u'iva_IC_compras_4_bi',
     u'IVA 4% Intracomunitario. Bienes de inversi\xf3n'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'), 'codes': {
                 },
            'tax': Decimal('0.00')}, ('in', 'invoice'
            ): {
             'base': Decimal('100.00'), 'codes': {
                 },
            'tax': Decimal('0.00')}},
    (u'iva_IC_compras_4_servicios',
     u'IVA 4% Intracomunitario. Servicios'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'), 'codes': {
                 },
            'tax': Decimal('0.00')}, ('in', 'invoice'
            ): {
             'base': Decimal('100.00'), 'codes': {
                 },
            'tax': Decimal('0.00')}},
    (u'iva_IO', u'IVA 0% Intracomunitario (Bienes)'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'base_intra_42': (u'Entregas Intracomunitarias (Bienes)'
            , ('credit_base_amount', Decimal('-100.00')))},
            'tax': -0.0}, ('out', 'invoice'): {
            'base': Decimal('100.00'
            ),
            'codes': {
                u'base_intra_42': (u'Entregas Intracomunitarias (Bienes)'
            , ('invoice_base_amount', Decimal('100.00')))},
            'tax': 0.0}},
    (u'iva_IO_serv', u'IVA 0% Intracomunitario (Servicios)'): {
#        ('out', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'base_intra_serv_42': (
#                    u'Entregas Intracomunitarias (Servicios)', (
#                        'credit_base_amount',
#                        Decimal('-100.00')
#                        )
#                    )
#                },
#            'tax': -0.0
#            },
        ('out', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'base_intra_serv_42': (
                    u'Entregas Intracomunitarias (Servicios)', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    )
                },
            'tax': 0.0
            }
        },
    (u'iva_ISP_compras', u'IVA Inversi\xf3n del sujeto pasivo'): {
        ('in' , 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {},
            'tax': Decimal('0.00')
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {},
            'tax': Decimal('0.00')
            }
        },
#    (u'iva_ISP_compras_16', u'IVA 0% Inversi\xf3n del sujeto pasivo'
#     ): {
#         ('in', 'credit'): {
#             'base': Decimal('-100.00'),
#             'codes': {
#                 u'base_extra_44': (
#                     u'Inversi\xf3n del sujeto pasivo', (
#                         'credit_base_amount',
#                         Decimal('-100.00')
#                         )
#                     )
#                 },
#             'tax': -0.0
#             },
#         ('in', 'invoice'): {
#             'base': Decimal('100.00'),
#             'codes': {
#                 u'base_extra_44': (
#                     u'Inversi\xf3n del sujeto pasivo', (
#                         'invoice_base_amount',
#                         Decimal('100.00')
#                         )
#                     )
#                 },
#             'tax': 0.0
#             }
#         },
    (u'iva_ISP_obra_0', u'IVA 0% Inversi\xf3n del sujeto pasivo (ejecuciones de obra)'): {
         ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                 u'base_extra_44': (
                    u'Inversi\xf3n del sujeto pasivo', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    )
                },
            'tax': -0.0
            },
         ('out', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'base_extra_44': (
                    u'Inversi\xf3n del sujeto pasivo', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    )
                },
            'tax': 0.0
            }
        },
    (u'iva_ISP_reciclaje_0', u'IVA 0% Inversi\xf3n del sujeto pasivo (chatarra y reciclaje de cart\xf3n)'): {
         ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                 u'base_extra_44': (
                    u'Inversi\xf3n del sujeto pasivo', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    )
                },
            'tax': -0.0
            },
         ('out', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                 u'base_extra_44': (
                    u'Inversi\xf3n del sujeto pasivo', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    )
                },
            'tax': 0.0
            }
        },
    (u'iva_X0', u'IVA 0% Exportaciones'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'base_extra_43': (u'Exportaciones y operaciones asimiladas'
            , ('credit_base_amount', Decimal('-100.00')))},
            'tax': -0.0}, ('out', 'invoice'): {
            'base': Decimal('100.00'
            ),
            'codes': {
                u'base_extra_43': (u'Exportaciones y operaciones asimiladas'
            , ('invoice_base_amount', Decimal('100.00')))},
            'tax': 0.0}},
    (u'iva_X0_compras_bc', u'IVA 0% Importaciones bienes corrientes'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_26': (u'Base importaciones bienes corrientes'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_27': (u'Cuotas devengadas importaciones bienes corrientes'
         , ('credit_tax_amount', -0.0))}, 'tax': -0.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_26': (u'Base importaciones bienes corrientes'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_27': (u'Cuotas devengadas importaciones bienes corrientes'
         , ('invoice_tax_amount', 0.0))}, 'tax': 0.0}},
    (u'iva_X0_compras_bi',
     u'IVA 0% Importaciones bienes de inversi\xf3n'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
            'codes': {
                 u'iva_ded_28': (u'Base importaciones bienes inversi\xf3n'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'iva_ded_29': (u'Cuotas devengadas importaciones bienes inversi\xf3n'
            , ('credit_tax_amount', -0.0))}, 'tax': -0.0}, ('in',
            'invoice'): {
             'base': Decimal('100.00'),
            'codes': {
                 u'iva_ded_28': (u'Base importaciones bienes inversi\xf3n'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'iva_ded_29': (u'Cuotas devengadas importaciones bienes inversi\xf3n'
            , ('invoice_tax_amount', 0.0))}, 'tax': 0.0}},
    (u'iva_X10_compras_bc', u'IVA 10% Importaciones bienes corrientes'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_26_10': (u'Base importaciones bienes corrientes (10%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_27_10': (u'Cuotas devengadas importaciones bienes corrientes (10%)'
         , ('credit_tax_amount', -10.0))}, 'tax': -10.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_26_10': (u'Base importaciones bienes corrientes (10%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_27_10': (u'Cuotas devengadas importaciones bienes corrientes (10%)'
         , ('invoice_tax_amount', 10.0))}, 'tax': 10.0}},
    (u'iva_X10_compras_bi',
     u'IVA 10% Importaciones bienes de inversi\xf3n'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
            'codes': {
                 u'iva_ded_28_10': (u'Base importaciones bienes inversi\xf3n (10%)'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'iva_ded_29_10': (u'Cuotas devengadas importaciones bienes inversi\xf3n (10%)'
            , ('credit_tax_amount', -10.0))}, 'tax': -10.0}, ('in',
            'invoice'): {
             'base': Decimal('100.00'),
            'codes': {
                 u'iva_ded_28_10': (u'Base importaciones bienes inversi\xf3n (10%)'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'iva_ded_29_10': (u'Cuotas devengadas importaciones bienes inversi\xf3n (10%)'
            , ('invoice_tax_amount', 10.0))}, 'tax': 10.0}},
    (u'iva_X21_compras_bc', u'IVA 21% Importaciones bienes corrientes'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_26_21': (u'Base importaciones bienes corrientes (21%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_27_21': (u'Cuotas devengadas importaciones bienes corrientes (21%)'
         , ('credit_tax_amount', -21.0))}, 'tax': -21.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_26_21': (u'Base importaciones bienes corrientes (21%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_27_21': (u'Cuotas devengadas importaciones bienes corrientes (21%)'
         , ('invoice_tax_amount', 21.0))}, 'tax': 21.0}},
    (u'iva_X21_compras_bi',
     u'IVA 21% Importaciones bienes de inversi\xf3n'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
            'codes': {
                 u'iva_ded_28_21': (u'Base importaciones bienes inversi\xf3n (21%)'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'iva_ded_29_21': (u'Cuotas devengadas importaciones bienes inversi\xf3n (21%)'
            , ('credit_tax_amount', -21.0))}, 'tax': -21.0}, ('in',
            'invoice'): {
             'base': Decimal('100.00'),
            'codes': {
                 u'iva_ded_28_21': (u'Base importaciones bienes inversi\xf3n (21%)'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'iva_ded_29_21': (u'Cuotas devengadas importaciones bienes inversi\xf3n (21%)'
            , ('invoice_tax_amount', 21.0))}, 'tax': 21.0}},
    (u'iva_X4_compras_bc', u'IVA 4% Importaciones bienes corrientes'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_26_4': (u'Base importaciones bienes corrientes (4%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_27_4': (u'Cuotas devengadas importaciones bienes corrientes (4%)'
         , ('credit_tax_amount', -4.0))}, 'tax': -4.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_26_4': (u'Base importaciones bienes corrientes (4%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_27_4': (u'Cuotas devengadas importaciones bienes corrientes (4%)'
         , ('invoice_tax_amount', 4.0))}, 'tax': 4.0}},
    (u'iva_X4_compras_bi',
     u'IVA 4% Importaciones bienes de inversi\xf3n'): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
            'codes': {
                 u'iva_ded_28_4': (u'Base importaciones bienes inversi\xf3n (4%)'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'iva_ded_29_4': (u'Cuotas devengadas importaciones bienes inversi\xf3n (4%)'
            , ('credit_tax_amount', -4.0))}, 'tax': -4.0}, ('in',
            'invoice'): {
             'base': Decimal('100.00'),
            'codes': {
                 u'iva_ded_28_4': (u'Base importaciones bienes inversi\xf3n (4%)'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'iva_ded_29_4': (u'Cuotas devengadas importaciones bienes inversi\xf3n (4%)'
            , ('invoice_tax_amount', 4.0))}, 'tax': 4.0}},
    (u'iva_ded_AI', u'Adquisiciones Intracomunitarias (Bienes)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_rect_19': (u'Rectificativas en Adquisiciones intracomunitarias (Bienes). Base Imponible'
         , ('credit_base_amount', Decimal('-100.00')))}, 'tax': -0.0},
         ('in', 'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_19': (u'En adquisiciones intracomunitarias (Bienes). Base Imponible'
         , ('invoice_base_amount', Decimal('100.00')))}, 'tax': 0.0}},
    (u'iva_ded_AI_serv', u'Adquisiciones Intracomunitarias (Servicios)'): {
         ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                 u'iva_ded_rect_serv_19': (
                    u'Rectificativas en Adquisiciones intracomunitarias (Servicios). Base Imponible', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    )
                },
            'tax': -0.0
            },
         ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                 u'iva_ded_serv_19': (
                    u'En adquisiciones intracomunitarias (Servicios). Base Imponible', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    )
                },
            'tax': 0.0
            }
        },
    (u'iva_dev_AI', u'Adquisiciones Intracomunitarias (Bienes)'): {
#         ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                u'iva_dev_19': (
#                    u'Adquisiciones intracomunitarias. Base Imponible', (
#                        'credit_base_amount',
#                        Decimal('-100.00')
#                        )
#                    ),
#                u'iva_dev_rect_19': (
#                    u'Rectificativas de Adquisiciones intracomunitarias (Bienes). Base Imponible', (
#                        'credit_base_amount',
#                        Decimal('-100.00')
#                        )
#                    )
#                },
#            'tax': -0.0,
#            },
#         ('in', 'invoice'): {
#            'base': Decimal('100.00'),
#            'codes': {
#                 u'iva_dev_19': (
#                    u'Adquisiciones intracomunitarias. Base Imponible', (
#                        'invoice_base_amount',
#                        Decimal('100.00')
#                        )
#                    )
#                },
#            'tax': 0.0,
#            }
        },
    (u'iva_dev_AI_serv', u'Adquisiciones Intracomunitarias (Servicios)'): {
#         ('in', 'credit'): {
#            'base': Decimal('-100.00'),
#            'codes': {
#                 u'iva_dev_rect_serv_19': (
#                    u'Rectificativas de Adquisiciones intracomunitarias (Servicios). Base Imponible', (
#                        'credit_base_amount',
#                        Decimal('-100.00')
#                        )
#                    )
#                },
#            'tax': -0.0},
#        ('in', 'invoice'): {
#             'base': Decimal('100.00'),
#             'codes': {
#                 u'iva_dev_serv_19': (
#                    u'Adquisiciones intracomunitarias (Servicios). Base Imponible', (
#                        'invoice_base_amount',
#                        Decimal('100.00')
#                        )
#                    )
#                },
#            'tax': 0.0
#            }
        },
    (u'iva_no_ded_10', u'10% IVA no Deducible'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_no_ded_22_10': (
                    u'IVA no Deducible Base Imponible (10%)', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_no_ded_cuota_23_10': (
                    u'Cuotas no deducible (10%)', (
                        'credit_tax_amount',
                        -10.0
                        )
                    )
                },
            'tax': -10,
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_no_ded_22_10': (
                    u'IVA no Deducible Base Imponible (10%)', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'iva_no_ded_cuota_23_10': (
                    u'Cuotas no deducible (10%)', (
                        'invoice_tax_amount',
                        10.0
                        )
                    )
                },
            'tax': 10,
            }
        },
    (u'iva_no_ded_21', u'21% IVA no Deducible'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_no_ded_22_21': (
                    u'IVA no Deducible Base Imponible (21%)', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
            u'iva_no_ded_cuota_23_21': (
                    u'Cuotas no deducible (21%)', (
                        'credit_tax_amount',
                        -21.0
                        )
                    )
                },
            'tax': -21.0
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_no_ded_22_21': (
                    u'IVA no Deducible Base Imponible (21%)', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'iva_no_ded_cuota_23_21': (
                    u'Cuotas no deducible (21%)', (
                        'invoice_tax_amount',
                        21.0
                        )
                    )
                },
            'tax': 21.0
            }
        },
    (u'iva_no_ded_4', u'4% IVA no Deducible'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_no_ded_22_4': (
                    u'IVA no Deducible Base Imponible (4%)', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
            u'iva_no_ded_cuota_23_4': (
                    u'Cuotas no deducible (4%)', (
                        'credit_tax_amount',
                        -4.0
                        )
                    )
                },
            'tax': -4.0
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_no_ded_22_4': (
                    u'IVA no Deducible Base Imponible (4%)', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'iva_no_ded_cuota_23_4': (
                    u'Cuotas no deducible (4%)', (
                        'invoice_tax_amount',
                        4.0
                        )
                    )
                },
            'tax': 4.0
            }
        },
    (u'iva_reagp_compras_12',
     u'IVA Soportado 12% + IRPF 2% Regimen Especial Agricultura y Pesca'): {
#         ('in', 'credit'): {
#             'base': Decimal('-100.00'),
#             'codes': {},
#             'tax': Decimal('0.00')
#             },
#         ('in', 'invoice'): {
#             'base': Decimal('100.00'),
#             'codes': {},
#             'tax': Decimal('0.00')
#             }
         },
    (u'iva_rep_0_asis',
     u'IVA 0% Operaciones exentas sin derecho a deducci\xf3n (servicios asistenciales)'): {
#         ('in', 'credit'): {
#             'base': Decimal('-100.00'),
#             'codes': {
#                 u'base_rep_ex': (
#                     u'Base ventas exentas', (
#                         'credit_base_amount',
#                         Decimal('-100.00')
#                         )
#                     )
#                 },
#             'tax': -0.0
#             },
#         ('in', 'invoice'): {
#             'base': Decimal('100.00'),
#             'codes': {
#                 u'base_rep_ex': (
#                     u'Base ventas exentas', (
#                         'invoice_base_amount',
#                         Decimal('100.00')
#                         )
#                     )
#                 },
#             'tax': 0.0
#             }
         },
    (u'iva_rep_0_ter_rus',
     u'IVA 0% Operaciones exentas sin derecho a deducci\xf3n (arrendamiento terrenos r\xfasticos)'): {
#         ('in', 'credit'): {
#             'base': Decimal('-100.00'),
#             'codes': {
#                 u'base_rep_ex': (
#                     u'Base ventas exentas', (
#                         'credit_base_amount',
#                         Decimal('-100.00')
#                         )
#                     )
#                 },
#             'tax': -0.0
#             },
#         ('in', 'invoice'): {
#             'base': Decimal('100.00'),
#             'codes': {
#                 u'base_rep_ex': (
#                     u'Base ventas exentas', (
#                         'invoice_base_amount',
#                         Decimal('100.00')
#                         )
#                     )
#                 },
#             'tax': 0.0
#             }
         },
    (u'iva_rep_10', u'IVA 10%'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_dev_04_10': (
                    u'R\xe9gimen general IVA Devengado. Base Imponible 10%' , (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_dev_06_10': (
                    u'R\xe9gimen general IVA Devengado. Cuota 10%', (
                        'credit_tax_amount',
                        -10.0
                        )
                    )
                },
                'tax': -10.0
            },
        ('out', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_dev_04_10': (
                    u'R\xe9gimen general IVA Devengado. Base Imponible 10%', (
                        'invoice_base_amount',
                        Decimal('100.00'))),
                u'iva_dev_06_10': (
                    u'R\xe9gimen general IVA Devengado. Cuota 10%', (
                        'invoice_tax_amount',
                        10.0
                        )
                    )
                },
            'tax': 10.0
            }
        },
    (u'iva_rep_21', u'IVA 21%'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_dev_07_21': (
                    u'R\xe9gimen general IVA Devengado. Base Imponible 21%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_dev_09_21': (
                    u'R\xe9gimen general IVA Devengado. Cuota 21%', (
                        'credit_tax_amount',
                        -21.0
                        )
                    )
                },
            'tax': -21.0
            },
        ('out', 'invoice'): {
            'base': Decimal('100.00'),
                                  'codes': {
                u'iva_dev_07_21': (u'R\xe9gimen general IVA Devengado. Base Imponible 21%'
                                  , ('invoice_base_amount',
                                  Decimal('100.00'))),
                                  u'iva_dev_09_21': (u'R\xe9gimen general IVA Devengado. Cuota 21%'
                                  , ('invoice_tax_amount', 21.0))},
                                  'tax': 21.0}},
    (u'iva_rep_4', u'IVA 4%'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_dev_01': (
                    u'R\xe9gimen general IVA Devengado. Base Imponible 4%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_dev_03': (
                    u'R\xe9gimen general IVA Devengado. Cuota 4%', (
                        'credit_tax_amount',
                        -4.0
                        )
                    )
                },
            'tax': -4.0
            },
        ('out', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_dev_01': (
                    u'R\xe9gimen general IVA Devengado. Base Imponible 4%', (
                        'invoice_base_amount',
                        Decimal('100.00'))),
                u'iva_dev_03': (
                    u'R\xe9gimen general IVA Devengado. Cuota 4%', (
                        'invoice_tax_amount',
                        4.0
                        )
                    )
                },
            'tax': 4.0
            }
        },
    (u'iva_rep_alq_ex', u'IVA alquiler vivienda exento'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'base_rep_alq_ex': (u'Base repercutida alquiler vivienda exenta'
            , ('credit_base_amount', Decimal('-100.00')))},
            'tax': -0.0}, ('out', 'invoice'): {
            'base': Decimal('100.00'
            ),
            'codes': {
                u'base_rep_alq_ex': (u'Base repercutida alquiler vivienda exenta'
            , ('invoice_base_amount', Decimal('100.00')))},
            'tax': 0.0}},
    (u'iva_rep_ex', u'IVA Exento'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'base_rep_ex': (u'Base ventas exentas',
            ('credit_base_amount', Decimal('-100.00')))},
            'tax': -0.0}, ('out', 'invoice'): {
            'base': Decimal('100.00'
            ), 'codes': {
                u'base_rep_ex': (u'Base ventas exentas',
            ('invoice_base_amount', Decimal('100.00')))},
            'tax': 0.0}},
    (u'iva_rep_no_sujeto', u'No sujeto'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'), 'codes': {
                },
            'tax': Decimal('0.00')}, ('out', 'invoice'
            ): {
            'base': Decimal('100.00'), 'codes': {
                },
            'tax': Decimal('0.00')}},
    (u'iva_sop_10', u'10% IVA Soportado (operaciones corrientes)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_22_10': (u'Base operaciones interiores corrientes (10%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_23_10': (u'Cuotas soportadas operaciones interiores corrientes (10%)'
         , ('credit_tax_amount', -10.0))}, 'tax': -10.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_22_10': (u'Base operaciones interiores corrientes (10%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_23_10': (u'Cuotas soportadas operaciones interiores corrientes (10%)'
         , ('invoice_tax_amount', 10.0))}, 'tax': 10.0}},
    (u'iva_sop_10_inv', u'10% IVA Soportado (bienes de inversi\xf3n)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_24_10': (u'Base operaciones interiores bienes inversi\xf3n (10%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_25_10': (u'Cuotas soportadas operaciones interiores bienes inversi\xf3n (10%)'
         , ('credit_tax_amount', -10.0))}, 'tax': -10.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_24_10': (u'Base operaciones interiores bienes inversi\xf3n (10%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_25_10': (u'Cuotas soportadas operaciones interiores bienes inversi\xf3n (10%)'
         , ('invoice_tax_amount', 10.0))}, 'tax': 10.0}},
    (u'iva_sop_21', u'21% IVA Soportado (operaciones corrientes)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_22_21': (u'Base operaciones interiores corrientes (21%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_23_21': (u'Cuotas soportadas operaciones interiores corrientes (21%)'
         , ('credit_tax_amount', -21.0))}, 'tax': -21.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_22_21': (u'Base operaciones interiores corrientes (21%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_23_21': (u'Cuotas soportadas operaciones interiores corrientes (21%)'
         , ('invoice_tax_amount', 21.0))}, 'tax': 21.0}},
    (u'iva_sop_21_inv', u'21% IVA Soportado (bienes de inversi\xf3n)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_24_21': (u'Base operaciones interiores bienes inversi\xf3n (21%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_25_21': (u'Cuotas soportadas operaciones interiores bienes inversi\xf3n (21%)'
         , ('credit_tax_amount', -21.0))}, 'tax': -21.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_24_21': (u'Base operaciones interiores bienes inversi\xf3n (21%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_25_21': (u'Cuotas soportadas operaciones interiores bienes inversi\xf3n (21%)'
         , ('invoice_tax_amount', 21.0))}, 'tax': 21.0}},
    (u'iva_sop_4', u'4% IVA Soportado (operaciones corrientes)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_22_4': (u'Base operaciones interiores corrientes (4%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_23_4': (u'Cuotas soportadas operaciones interiores corrientes (4%)'
         , ('credit_tax_amount', -4.0))}, 'tax': -4.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_22_4': (u'Base operaciones interiores corrientes (4%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_23_4': (u'Cuotas soportadas operaciones interiores corrientes (4%)'
         , ('invoice_tax_amount', 4.0))}, 'tax': 4.0}},
    (u'iva_sop_4_inv', u'4% IVA Soportado (bienes de inversi\xf3n)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'iva_ded_24_4': (u'Base operaciones interiores bienes inversi\xf3n (4%)'
         , ('credit_base_amount', Decimal('-100.00'))),
         u'iva_ded_25_4': (u'Cuotas soportadas operaciones interiores bienes inversi\xf3n (4%)'
         , ('credit_tax_amount', -4.0))}, 'tax': -4.0}, ('in',
         'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'iva_ded_24_4': (u'Base operaciones interiores bienes inversi\xf3n (4%)'
         , ('invoice_base_amount', Decimal('100.00'))),
         u'iva_ded_25_4': (u'Cuotas soportadas operaciones interiores bienes inversi\xf3n (4%)'
         , ('invoice_tax_amount', 4.0))}, 'tax': 4.0}},
    (u'iva_sop_alq_ex', u'IVA Soportado alquiler vivienda exento'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'base_sop_alq_ex': (u'Base soportada alquiler vivienda exenta'
         , ('credit_base_amount', Decimal('-100.00')))}, 'tax': -0.0},
         ('in', 'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'base_sop_alq_ex': (u'Base soportada alquiler vivienda exenta'
         , ('invoice_base_amount', Decimal('100.00')))}, 'tax': 0.0}},
    (u'iva_sop_ex', u'IVA Soportado exento (operaciones corrientes)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'base_sop_ex': (u'Base adquisiciones exentas',
         ('credit_base_amount', Decimal('-100.00')))}, 'tax': -0.0},
         ('in', 'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'base_sop_ex': (u'Base adquisiciones exentas',
         ('invoice_base_amount', Decimal('100.00')))}, 'tax': 0.0}},
    (u'iva_sop_ex_inv', u'IVA Soportado exento (bienes de inversi\xf3n)'
     ): {
         ('in', 'credit'): {
             'base': Decimal('-100.00'),
         'codes': {
                 u'base_sop_ex': (u'Base adquisiciones exentas',
         ('credit_base_amount', Decimal('-100.00')))}, 'tax': -0.0},
         ('in', 'invoice'): {
             'base': Decimal('100.00'),
         'codes': {
                 u'base_sop_ex': (u'Base adquisiciones exentas',
         ('invoice_base_amount', Decimal('100.00')))}, 'tax': 0.0}},
    (u'iva_sop_no_sujeto', u'No sujeto'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'), 'codes': {
                },
            'tax': Decimal('0.00')}, ('in', 'invoice'
            ): {
            'base': Decimal('100.00'), 'codes': {
                },
            'tax': Decimal('0.00')}},
    (u're_05', u'0.50% Recargo Equivalencia Ventas'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_dev_10': (u'Recargo Equivalencia Base Imponible 0.5%'
            , ('credit_base_amount', Decimal('-100.00'))),
            u'iva_dev_12': (u'Recargo Equivalencia. Cuota 0.5%',
            ('credit_tax_amount', -0.5))}, 'tax': -0.5}, ('out',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_dev_10': (u'Recargo Equivalencia Base Imponible 0.5%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'iva_dev_12': (u'Recargo Equivalencia. Cuota 0.5%',
            ('invoice_tax_amount', 0.5))}, 'tax': 0.5}},
    (u're_14', u'1.4% Recargo Equivalencia Ventas'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_dev_13_14': (
                    u'Recargo Equivalencia Base Imponible 1.4%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_dev_15_14': (
                    u'Recargo Equivalencia. Cuota 1.4%', (
                        'credit_tax_amount',
                        Decimal('-1.4'),
                        )
                    )
                },
            'tax': Decimal('-1.4'),
            },
        ('out', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_dev_13_14': (
                    u'Recargo Equivalencia Base Imponible 1.4%', (
                        'invoice_base_amount',
                        Decimal('100.00'),
                        )
                    ),
                u'iva_dev_15_14': (
                    u'Recargo Equivalencia. Cuota 1.4%', (
                        'invoice_tax_amount',
                        Decimal('1.4'),
                        )
                    )
                },
            'tax': Decimal('1.4'),
            }
        },
    (u're_52', u'5.2% Recargo Equivalencia Ventas'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_dev_16_52': (
                    u'Recargo Equivalencia Base Imponible 5.2%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_dev_18_52': (
                    u'Recargo Equivalencia. Cuota 5.2%', (
                        'credit_tax_amount',
                        Decimal('-5.2'),
                        )
                    )
                },
            'tax': Decimal('-5.2'),
            },
        ('out', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_dev_16_52': (
                    u'Recargo Equivalencia Base Imponible 5.2%', (
                        'invoice_base_amount',
                        Decimal('100.00'),
                        )
                    ),
                u'iva_dev_18_52': (
                    u'Recargo Equivalencia. Cuota 5.2%', (
                        'invoice_tax_amount',
                        Decimal('5.2'),
                        )
                    )
                },
            'tax': Decimal('5.2')
            }
        },
    (u're_buy_05', u'0.50% Recargo Equivalencia Compras'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_ded_10': (
                    u'Recargo Equivalencia Ded. Base Imponible 0.5%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_ded_12': (
                    u'Recargo Equivalencia Ded. Cuota 0.5%', (
                        'credit_tax_amount',
                        -0.5
                        )
                    )
                },
            'tax': -0.5}, ('in',
            'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_ded_10': (u'Recargo Equivalencia Ded. Base Imponible 0.5%'
            , ('invoice_base_amount', Decimal('100.00'))),
            u'iva_ded_12': (u'Recargo Equivalencia Ded. Cuota 0.5%',
            ('invoice_tax_amount', 0.5))}, 'tax': 0.5}},
    (u're_buy_14', u'1.4% Recargo Equivalencia Compras'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_ded_13_14': (
                    u'Recargo Equivalencia Ded. Base Imponible 1.4%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_ded_15_14': (
                    u'Recargo Equivalencia Ded. Cuota 1.4%', (
                        'credit_tax_amount',
                        Decimal('-1.4'),
                        )
                    )
                },
            'tax': Decimal('-1.4'),
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_ded_13_14': (
                    u'Recargo Equivalencia Ded. Base Imponible 1.4%', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'iva_ded_15_14': (
                    u'Recargo Equivalencia Ded. Cuota 1.4%', (
                        'invoice_tax_amount',
                        Decimal('1.4'),
                        )
                    )
                },
            'tax': Decimal('1.4')
            }},
    (u're_buy_52', u'5.2% Recargo Equivalencia Compras'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {
                u'iva_ded_16_52': (
                    u'Recargo Equivalencia Ded. Base Imponible 5.2%', (
                        'credit_base_amount',
                        Decimal('-100.00')
                        )
                    ),
                u'iva_ded_18_52': (
                    u'Recargo Equivalencia Ded. Cuota 5.2%', (
                        'credit_tax_amount',
                        Decimal('-5.2'),
                        )
                    )
                },
            'tax': Decimal('-5.2'),
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {
                u'iva_ded_16_52': (
                    u'Recargo Equivalencia Ded. Base Imponible 5.2%', (
                        'invoice_base_amount',
                        Decimal('100.00')
                        )
                    ),
                u'iva_ded_18_52': (
                    u'Recargo Equivalencia Ded. Cuota 5.2%', (
                        'invoice_tax_amount',
                        Decimal('5.2'),
                        )
                    )
                },
            'tax': Decimal('5.2'),
            }
        },
    (u'suplido_compras', u'Suplido'): {
        ('in', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {},
            'tax': Decimal('0.00'),
            },
        ('in', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {},
            'tax': Decimal('0.00'),
            }
        },
    (u'suplido_ventas', u'Suplido'): {
        ('out', 'credit'): {
            'base': Decimal('-100.00'),
            'codes': {},
            'tax': Decimal('0.00')
            },
        ('out', 'invoice'): {
            'base': Decimal('100.00'),
            'codes': {},
            'tax': Decimal('0.00')
            }
        },
    }
