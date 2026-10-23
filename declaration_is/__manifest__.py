# -*- coding: utf-8 -*-
{
    'name': 'Déclaration IS (Impôt sur les Sociétés)',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Localizations',
    'summary': 'Génération de la liasse fiscale IS - Déclaration XML',
    'description': """
        Module de déclaration de l'Impôt sur les Sociétés (IS).
        Permet de générer le fichier XML de la liasse IS.
    """,
    'author': 'Khadija',
    'depends': ['account', 'base', 'custom_company_ma', 'balance_doosys'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/declaration_is_wizard_views.xml',
        'views/declaration_is_history_views.xml',
        'views/declaration_is_menu.xml',
        
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}