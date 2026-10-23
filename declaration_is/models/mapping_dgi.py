# -*- coding: utf-8 -*-
class MappingDGI:

    # BILAN ACTIF (tableau id = 3)
    # Colonnes : C = Brut N, D = Amort N, E = Net N, F = Net N-1
    BilanActif = {
        # Section A : IMMOBILISATIONS EN NON VALEURS
        'C7': 497, 'D7': 498, 'E7': 499, 'F7': 500,   # Total A
        'C8': 238, 'D8': 241, 'E8': 244, 'F8': 247,   # Frais préliminaires
        'C9': 239, 'D9': 242, 'E9': 245, 'F9': 248,   # Charges à répartir
        'C10': 240, 'D10': 243, 'E10': 246, 'F10': 249, # Primes de remboursement

        # Section B : IMMOBILISATIONS INCORPORELLES
        'C11': 502, 'D11': 503, 'E11': 504, 'F11': 505, # Total B
        'C12': 274, 'D12': 278, 'E12': 282, 'F12': 286, # Recherche & développement
        'C13': 275, 'D13': 279, 'E13': 283, 'F13': 287, # Brevets, marques
        'C14': 276, 'D14': 280, 'E14': 284, 'F14': 288, # Fonds commercial
        'C15': 277, 'D15': 281, 'E15': 285, 'F15': 289, # Autres incorporelles

        # Section C : IMMOBILISATIONS CORPORELLES
        'C16': 507, 'D16': 508, 'E16': 509, 'F16': 510, # Total C
        'C17': 207, 'D17': 214, 'E17': 221, 'F17': 228, # Terrains
        'C18': 208, 'D18': 215, 'E18': 222, 'F18': 229, # Constructions
        'C19': 209, 'D19': 216, 'E19': 223, 'F19': 230, # Installations techniques
        'C20': 210, 'D20': 217, 'E20': 224, 'F20': 231, # Matériel transport
        'C21': 211, 'D21': 218, 'E21': 225, 'F21': 232, # Mobilier, matériel bureau
        'C22': 212, 'D22': 219, 'E22': 226, 'F22': 233, # Autres corporelles
        'C23': 213, 'D23': 220, 'E23': 227, 'F23': 234, # Corporelles en cours

        # Section D : IMMOBILISATIONS FINANCIERES
        'C24': 512, 'D24': 513, 'E24': 514, 'F24': 515, # Total D
        'C25': 254, 'D25': 258, 'E25': 262, 'F25': 266, # Prêts immobilisés
        'C26': 255, 'D26': 259, 'E26': 263, 'F26': 267, # Autres créances financières
        'C27': 256, 'D27': 260, 'E27': 264, 'F27': 268, # Titres de participation
        'C28': 257, 'D28': 261, 'E28': 265, 'F28': 269, # Autres titres immobilisés

        # Section E : ECARTS DE CONVERSION - ACTIF
        'C29': 517, 'D29': 518, 'E29': 519, 'F29': 520, # Total E
        'C30': 192, 'D30': 194, 'E30': 196, 'F30': 198, # Diminution créances immobilisées
        'C31': 193, 'D31': 195, 'E31': 197, 'F31': 199, # Augmentation dettes financement

        # TOTAL I
        'C32': 291, 'D32': 292, 'E32': 293, 'F32': 294, # Total I (A+B+C+D+E)

        # Section F : STOCKS
        'C34': 522, 'D34': 523, 'E34': 524, 'F34': 525, # Total F
        'C35': 160, 'D35': 165, 'E35': 170, 'F35': 175, # Marchandises
        'C36': 161, 'D36': 166, 'E36': 171, 'F36': 176, # Matières et fournitures
        'C37': 162, 'D37': 167, 'E37': 172, 'F37': 177, # Produits en cours
        'C38': 163, 'D38': 168, 'E38': 173, 'F38': 178, # Produits intermédiaires
        'C39': 164, 'D39': 169, 'E39': 174, 'F39': 179, # Produits finis

        # Section G : CREANCES DE L'ACTIF CIRCULANT
        'C40': 527, 'D40': 528, 'E40': 529, 'F40': 530, # Total G
        'C41': 122, 'D41': 129, 'E41': 136, 'F41': 143, # Fournisseurs débiteurs
        'C42': 123, 'D42': 130, 'E42': 137, 'F42': 144, # Clients
        'C43': 124, 'D43': 131, 'E43': 138, 'F43': 145, # Personnel
        'C44': 125, 'D44': 132, 'E44': 139, 'F44': 146, # Etat
        'C45': 126, 'D45': 133, 'E45': 140, 'F45': 147, # Comptes d'associés
        'C46': 127, 'D46': 134, 'E46': 141, 'F46': 148, # Autres débiteurs
        'C47': 128, 'D47': 135, 'E47': 142, 'F47': 149, # Comptes de régularisation

        # Section H : TITRES VALEURS DE PLACEMENT
        'C48': 181, 'D48': 182, 'E48': 183, 'F48': 184, # Titres valeurs placement

        # Section I : ECARTS DE CONVERSION - ACTIF (éléments circulants)
        'C49': 151, 'D49': 152, 'E49': 153, 'F49': 154, # Ecarts conversion circulant

        # TOTAL II
        'C51': 296, 'D51': 297, 'E51': 298, 'F51': 299, # Total II (F+G+H+I)

        # TRESORERIE - ACTIF
        'C53': 532, 'D53': 533, 'E53': 534, 'F53': 535, # Total Trésorerie
        'C54': 303, 'D54': 306, 'E54': 309, 'F54': 312, # Chèques et valeurs à encaisser
        'C55': 304, 'D55': 307, 'E55': 310, 'F55': 313, # Banques, TG, CCP
        'C56': 305, 'D56': 308, 'E56': 311, 'F56': 314, # Caisse, régies

        # TOTAL III
        'C57': 316, 'D57': 317, 'E57': 318, 'F57': 319, # Total III

        # TOTAL GENERAL
        'C59': 186, 'D59': 187, 'E59': 188, 'F59': 189, # Total général I+II+III
    }

    # BILAN PASSIF (tableau id = 1 ou 2 selon votre XML)
    # Colonnes : C = année N, D = année N-1
    BilanPassif = {
        # Capitaux propres (A)
        'C8': 13400, 'D8': 13411,   # Capital social
        'C9': 13401, 'D9': 13412,   # Moins : capital souscrit non appelé
        'C10': 13402, 'D10': 13413, # Capital appelé
        'C11': 13403, 'D11': 13414, # Dont versé
        'C12': 13404, 'D12': 13415, # Prime d'émission, fusion, apport
        'C13': 13405, 'D13': 13416, # Ecarts de réévaluation
        'C14': 13406, 'D14': 13417, # Réserve légale
        'C15': 13407, 'D15': 13418, # Autres réserves
        'C16': 13408, 'D16': 13419, # Report à nouveau
        'C17': 14001, 'D17': 14002, # Résultats nets en instance d'affectation
        'C18': 13409, 'D18': 13420, # Résultat net de l'exercice
        'C19': 13410, 'D19': 13421, # Total des capitaux propres (A)

        # Capitaux propres assimilés (B)
        'C20': 13397, 'D20': 13422, # Total capitaux propres assimilés (B)
        'C21': 13398, 'D21': 13423, # Subvention d'investissement
        'C22': 13399, 'D22': 13424, # Provisions réglementées

        # Dettes de financement (C)
        'C23': 13393, 'D23': 13426, # Total dettes de financement (C)
        'C24': 13394, 'D24': 13427, # Emprunts obligataires
        'C25': 13395, 'D25': 13428, # Autres dettes de financement

        # Provisions durables pour risques et charges (D)
        'C26': 13389, 'D26': 13430, # Total provisions durables (D)
        'C27': 13390, 'D27': 13431, # Provisions pour risques
        'C28': 13391, 'D28': 13432, # Provisions pour charges

        # Ecarts de conversion passif (E)
        'C30': 13386, 'D30': 13433, # Total écarts conversion (E)
        'C31': 13387, 'D31': 13434, # Augmentation des créances immobilisées
        'C32': 13388, 'D32': 13435, # Diminution des dettes de financement

        # TOTAL I (A+B+C+D+E)
        'C33': 13385, 'D33': 13436, # Total I

        # Dettes du passif circulant (F)
        'C35': 13376, 'D35': 13437, # Total dettes circulant (F)
        'C36': 13377, 'D36': 13438, # Fournisseurs
        'C37': 13378, 'D37': 13439, # Clients créditeurs
        'C38': 13379, 'D38': 13440, # Personnel
        'C39': 13380, 'D39': 13441, # Organismes sociaux
        'C40': 13381, 'D40': 13442, # Etat
        'C41': 13382, 'D41': 13443, # Comptes d'associés
        'C42': 13383, 'D42': 13444, # Autres créanciers
        'C43': 13384, 'D43': 13445, # Comptes de régularisation passif

        # Autres provisions pour risques et charges (G)
        'C44': 13375, 'D44': 13446, # Autres provisions (G)

        # Ecarts de conversion passif (éléments circulants) (H)
        'C45': 13374, 'D45': 13447, # Ecarts conversion circulant (H)

        # TOTAL II (F+G+H)
        'C46': 13373, 'D46': 13448, # Total II

        # TRESORERIE - PASSIF
        'C49': 13370, 'D49': 13449, # Crédits d'escompte
        'C50': 13371, 'D50': 13450, # Crédits de trésorerie
        'C51': 13372, 'D51': 13451, # Banques (soldes créditeurs)

        # TOTAL III
        'C48': 13369, 'D48': 13452, # Total III (car C48 = SUM(C49:C51))

        # TOTAL GENERAL I+II+III
        'C54': 13368, 'D54': 13453, # Total général
    }

    # CPC
    Cpc = {
    # I. PRODUITS D'EXPLOITATION (lignes 10 à 18)
    'D10': 11181, 'E10': 11182, 'F10': 11183, 'G10': 11184,   # Ventes de marchandises
    'D11': 11186, 'E11': 11187, 'F11': 11188, 'G11': 11189,   # Ventes de biens et services
    'D12': 14021, 'E12': 14022, 'F12': 14023, 'G12': 14024,   # Chiffre d'affaires
    'D13': 11191, 'E13': 11192, 'F13': 11193, 'G13': 11194,   # Variation de stocks
    'D14': 11196, 'E14': 11197, 'F14': 11198, 'G14': 11199,   # Immobilisations produites
    'D15': 11201, 'E15': 11202, 'F15': 11203, 'G15': 11204,   # Subventions d'exploitation
    'D16': 11206, 'E16': 11207, 'F16': 11208, 'G16': 11209,   # Autres produits d'exploitation
    'D17': 11211, 'E17': 11212, 'F17': 11213, 'G17': 11214,   # Reprises d'exploitation
    'D18': 11176, 'E18': 11177, 'F18': 11178, 'G18': 11179,   # Total I

    # II. CHARGES D'EXPLOITATION (lignes 20 à 27)
    'D20': 11221, 'E20': 11222, 'F20': 11223, 'G20': 11224,   # Achats revendus
    'D21': 11256, 'E21': 11257, 'F21': 11258, 'G21': 11259,   # Achats consommés
    'D22': 11261, 'E22': 11262, 'F22': 11263, 'G22': 11264,   # Autres charges externes
    'D23': 11251, 'E23': 11252, 'F23': 11253, 'G23': 11254,   # Impôts et taxes
    'D24': 11266, 'E24': 11267, 'F24': 11268, 'G24': 11269,   # Charges de personnel
    'D25': 11246, 'E25': 11247, 'F25': 11248, 'G25': 11249,   # Autres charges d'exploitation
    'D26': 11241, 'E26': 11242, 'F26': 11243, 'G26': 11244,   # Dotations d'exploitation
    'D27': 11226, 'E27': 11227, 'F27': 11228, 'G27': 11229,   # Total II

    # III. RESULTAT D'EXPLOITATION (ligne 28)
    'D28': 11231, 'E28': 11232, 'F28': 11233, 'G28': 11234,

    # IV. PRODUITS FINANCIERS (lignes 30 à 34)
    'D30': 11271, 'E30': 11272, 'F30': 11273, 'G30': 11274,   # Produits des titres
    'D31': 11276, 'E31': 11277, 'F31': 11278, 'G31': 11279,   # Gains de change
    'D32': 11281, 'E32': 11282, 'F32': 11283, 'G32': 11284,   # Intérêts
    'D33': 11286, 'E33': 11287, 'F33': 11288, 'G33': 11289,   # Reprises
    'D34': 11326, 'E34': 11327, 'F34': 11328, 'G34': 11329,   # Total IV

    # V. CHARGES FINANCIERES (lignes 36 à 40)
    'D36': 11296, 'E36': 11297, 'F36': 11298, 'G36': 11299,   # Charges d'intérêts
    'D37': 11301, 'E37': 11302, 'F37': 11303, 'G37': 11304,   # Pertes de change
    'D38': 11306, 'E38': 11307, 'F38': 11308, 'G38': 11309,   # Autres charges financières
    'D39': 11311, 'E39': 11312, 'F39': 11313, 'G39': 11314,   # Dotations financières
    'D40': 11321, 'E40': 11322, 'F40': 11323, 'G40': 11324,   # Total V

    # VI. RESULTAT FINANCIER (ligne 41)
    'D41': 11331, 'E41': 11332, 'F41': 11333, 'G41': 11334,

    # VII. RESULTAT COURANT (ligne 42)
    'D42': 11336, 'E42': 11337, 'F42': 11338, 'G42': 11339,

    # VIII. PRODUITS NON COURANTS (lignes 55 à 60)
    'D55': 11341, 'E55': 11342, 'F55': 11343, 'G55': 11344,   # Produits des cessions
    'D56': 11346, 'E56': 11347, 'F56': 11348, 'G56': 11349,   # Subventions d'équilibre
    'D57': 11351, 'E57': 11352, 'F57': 11353, 'G57': 11354,   # Reprises sur subventions
    'D58': 11356, 'E58': 11357, 'F58': 11358, 'G58': 11359,   # Autres produits non courants
    'D59': 11361, 'E59': 11362, 'F59': 11363, 'G59': 11364,   # Reprises non courantes
    'D60': 11391, 'E60': 11392, 'F60': 11393, 'G60': 11394,   # Total VIII

    # IX. CHARGES NON COURANTES (lignes 62 à 66)
    'D62': 11371, 'E62': 11372, 'F62': 11373, 'G62': 11374,   # VNA des immobilisations cédées
    'D63': 11376, 'E63': 11377, 'F63': 11378, 'G63': 11379,   # Subventions accordées
    'D64': 11381, 'E64': 11382, 'F64': 11383, 'G64': 11384,   # Autres charges non courantes
    'D65': 11386, 'E65': 11387, 'F65': 11388, 'G65': 11389,   # Dotations non courantes
    'D66': 11396, 'E66': 11397, 'F66': 11398, 'G66': 11399,   # Total IX

    # X. RESULTAT NON COURANT (ligne 67)
    'D67': 11401, 'E67': 11402, 'F67': 11403, 'G67': 11404,

    # XI. RESULTAT AVANT IMPOTS (ligne 68)
    'D68': 11411, 'E68': 11412, 'F68': 11413, 'G68': 11414,

    # XII. IMPOTS SUR LES RESULTATS (ligne 69)
    'D69': 11416, 'E69': 11417, 'F69': 11418, 'G69': 11419,

    # XIII. RESULTAT NET (ligne 70)
    'D70': 11421, 'E70': 11422, 'F70': 11423, 'G70': 11424,

    # XIV. TOTAL DES PRODUITS (ligne 72)
    'D72': 11426, 'E72': 11427, 'F72': 11428, 'G72': 11429,

    # XV. TOTAL DES CHARGES (ligne 73)
    'D73': 11431, 'E73': 11432, 'F73': 11433, 'G73': 11434,

    # RESULTAT NET (total des produits - total des charges) (ligne 74)
    'D74': 11436, 'E74': 11437, 'F74': 11438, 'G74': 11439,
}