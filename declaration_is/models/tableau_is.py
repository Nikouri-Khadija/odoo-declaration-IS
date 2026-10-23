# -*- coding: utf-8 -*-
from xml.etree import ElementTree as ET


class Cellule:

    def __init__(self, code_EDI: int, valeur):
        self.code_EDI = int(code_EDI)
        self.valeur   = valeur

    def to_xml(self, parent: ET.Element):
        """
            <ValeurCellule>
              <cellule><codeEdi>497</codeEdi></cellule>
              <valeur>150000.00</valeur>
            </ValeurCellule>
        """
        
        if self.valeur == 0.0:
            valeur_str = "0.00"
        else:
            valeur_str = f"{self.valeur:.2f}"
        
        vc = ET.SubElement(parent, 'ValeurCellule')
        cellule_el = ET.SubElement(vc, 'cellule')
        ET.SubElement(cellule_el, 'codeEdi').text = str(self.code_EDI)
        ET.SubElement(vc, 'valeur').text = valeur_str


class TableauIS:
    

    id_tableau: int = 0   # à surcharger dans chaque sous-classe

    def __init__(self):
        self.cellules: list = []

    def remplir_valeurs(self, valeurs: dict, mapping: dict):
        """Remplit les cellules à partir des valeurs lues et du mapping DGI."""
        self.cellules.clear()
        for cell_key, code_edi in mapping.items():
            valeur = valeurs.get(cell_key)
            self.cellules.append(Cellule(code_edi, valeur)) 

    def to_xml(self) -> ET.Element:
        """Génère le bloc XML <ValeursTableau> pour ce tableau."""
        vt = ET.Element('ValeursTableau')
        ET.SubElement(ET.SubElement(vt, 'tableau'), 'id').text = str(self.id_tableau)
        groupe = ET.SubElement(vt, 'groupeValeurs')
        for cellule in self.cellules:
            cellule.to_xml(groupe)
        return vt


class BilanActif(TableauIS):
    id_tableau = 2


class BilanPassif(TableauIS):
    id_tableau = 1

class Cpc(TableauIS):
    id_tableau = 6