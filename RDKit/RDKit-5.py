from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from io import StringIO
import pickle
from rdkit.Chem.Draw import rdMolDraw2D

m = Chem.MolFromSmiles('CC[C@H](F)Cl')
print(m.HasSubstructMatch(Chem.MolFromSmiles('C[C@H](F)Cl')))
print(m.HasSubstructMatch(Chem.MolFromSmiles('C[C@@H](F)Cl')))
print(m.HasSubstructMatch(Chem.MolFromSmiles('CC(F)Cl')))

# change this with chirality 
print(m.HasSubstructMatch(Chem.MolFromSmiles('C[C@H](F)Cl'), useChirality=True))
print(m.HasSubstructMatch(Chem.MolFromSmiles('C[C@@H](F)Cl'),  useChirality=True)) # when chiral query and non-chiral molecule does not match
print(m.HasSubstructMatch(Chem.MolFromSmiles('CC(F)Cl'),  useChirality=True))

print(m.HasSubstructMatch(Chem.MolFromSmiles('CC(F)Cl')))
m2 = Chem.MolFromSmiles('CCC(F)Cl')
print(m2.HasSubstructMatch(Chem.MolFromSmiles('C[C@H](F)Cl'), useChirality=True))

# Atom Map Indices in SMARTS
qmol = Chem.MolFromSmarts( '[cH0:1][c:2]([cH0])!@[CX3!r:3]=[NX2!r:4]' )
ind_map ={}
for atom in qmol.GetAtoms():
    map_num = atom.GetAtomMapNum()
    if map_num:
        ind_map[map_num-1] = atom.GetIdx()
print(ind_map)

map_list = [ind_map[x] for x in sorted(ind_map)]
print(map_list)

# using this query on a certain or target molecule to get indices of the matching atoms
mol = Chem.MolFromSmiles('Cc1cccc(C)c1C(C)=NC')
for match in mol.GetSubstructMatches( qmol ):
    mas = [match[x] for x in map_list]
    print(mas)
    