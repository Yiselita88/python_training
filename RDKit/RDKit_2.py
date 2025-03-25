from rdkit import Chem
from rdkit.Chem import AllChem
m2 = Chem.MolFromSmiles('C1=CC=C(C=C1)C[C@@H](C(=O)O)N')

# to compute 2D coordinates
print(AllChem.Compute2DCoords(m2))

m2.SetProp("Name", "phenylalanine")
print(Chem.MolToMolBlock(m2))

# # for 3D structures
# add H
m3 = Chem.AddHs(m2)
params = AllChem.ETKDGv3()
params.randomSeed = 0xf00d
print(AllChem.EmbedMolecule(m3, params))

print(Chem.MolToMolBlock(m3))

from rdkit.Chem import Draw
img3 = Draw.MolToImage(m3)
img3.save('phenylalanine.png')

# to remove H
m4 = Chem.RemoveHs(m3)
print(Chem.MolToMolBlock(m4))
img4 = Draw.MolToImage(m4)
img4.save('Phe_noH.png')
# to save data into file
print(Chem.MolToMolBlock(m4), file=open('Phe_noH.mol', 'w+'))


# write multiple molecules to a file
mols = [m2, m3, m4]
with Chem.SDWriter('all.sdf') as w:
    for m in mols:
        w.write(m)

# initialize with SDWriter
from io import StringIO
sio = StringIO()
with Chem.SDWriter(sio) as w:
    for m in mols:
        w.write(m)
print(sio.getvalue())

# # WORKING WITH MOLECULES # #
# Looping over Atoms and Bonds

m5  = Chem.MolFromSmiles('C1OC1')
for atom in m5.GetAtoms():
    print(atom.GetAtomicNum())

print(m5.GetBonds()[0].GetBondType())

# request individual bonds or atoms:
print(m5.GetAtomWithIdx(0).GetSymbol())
print(m5.GetAtomWithIdx(0).GetExplicitValence())
print(m5.GetBondBetweenAtoms(0,1).GetBondType())
print(m5.GetBondWithIdx(0).GetBeginAtomIdx())
print(m5.GetBondWithIdx(0).GetEndAtomIdx())

# atoms keep track of their neighbors
atom = m5.GetAtomWithIdx(0)
print([x.GetAtomicNum() for x in atom.GetNeighbors()])
atom = m5.GetAtomWithIdx(1)
print([x.GetAtomicNum() for x in atom.GetNeighbors()])
print(len(atom.GetNeighbors()[-1].GetBonds()))

# Ring information
m6 = Chem.MolFromSmiles('OC1C2C1CC2')
print(m6.GetAtomWithIdx(0).IsInRing())
print(m6.GetAtomWithIdx(1).IsInRing())
print(m6.GetAtomWithIdx(2).IsInRingSize(3))
print(m6.GetAtomWithIdx(2).IsInRingSize(4))
print(m6.GetAtomWithIdx(2).IsInRingSize(5))
print(m6.GetBondWithIdx(1).IsInRing())
print(m6.GetBondWithIdx(1).IsInRingSize(3))

# more info about the smallest set of smallest rings (SSSR):
ssr = Chem.GetSymmSSSR(m6)
print(len(ssr))
print(list(ssr[0]))
print(list(ssr[1]))

# to know the number of true SSSR
print(len(Chem.GetSSSR(m6)))

# RingInfo class

m7 = Chem.MolFromSmiles('OC1C2C1CC2')
ri = m7.GetRingInfo()
print(ri.NumAtomRings(0))
print(ri.NumAtomRings(1))
print(ri.NumAtomRings(2))
print(ri.IsAtomInRingOfSize(1, 3))
print(ri.IsBondInRingOfSize(1, 3))

# Modifying molecules
m8 = Chem.MolFromSmiles('CCO')
print(m8.GetNumAtoms())
m9 = Chem.AddHs(m8)
print(m9.GetNumAtoms())

m10 = Chem.RemoveHs(m9)
print(m10.GetNumAtoms())

# using KEKULIZE function to change aromatic bond types

m11 = Chem.MolFromSmiles('c1ccccc1')
print(m11.GetBondWithIdx(0).GetBondType())
Chem.Kekulize(m11)
print(m11.GetBondWithIdx(0).GetBondType())
print(m11.GetBondWithIdx(1).GetBondType())
print(m11.GetBondWithIdx(1).GetIsAromatic())

# kekulize initial molecule to avoid aromatic flag
m12 = Chem.MolFromSmiles('c1ccccc1')
Chem.Kekulize(m12, clearAromaticFlags=True)
print(m12.GetBondWithIdx(0).GetIsAromatic())

# restoring bond to aromatic bond type
Chem.SanitizeMol(m11)
print(m11.GetBondWithIdx(1).GetBondType())

# # WORKING with 2D molecules : Generating Depictions
m13 = Chem.MolFromSmiles('c1nccc2n1ccc2')
print(AllChem.Compute2DCoords(m13))

# printing 2D molecules with common template
template = Chem.MolFromSmiles('c1nccc2n1ccc2')
print(AllChem.Compute2DCoords(template))

ms = [Chem.MolFromSmiles(smi) for smi in ('OCCc1ccn2cnccc12','C1CC1Oc1cc2ccncn2c1','CNC(=O)c1nccc2cccn12')]
for m in ms:
    _ = AllChem.GenerateDepictionMatching2DStructure(m, template)

img5 = Draw.MolsToGridImage(ms, molsPerRow=3, subImgSize=(300, 300))
img5.save('mol_w_tmplt.png')

# # Working with 3D Molecules # #
# embedding molecules
m14 = Chem.MolFromSmiles('C1CCC1OC')
m15 = Chem.AddHs(m14)
print(AllChem.EmbedMolecule(m15))
print(AllChem.MMFFOptimizeMolecule(m15))   

