from rdkit import Chem
m1 = Chem.MolFromSmiles('CO(C)C')
print(m1)

# drawing a single molecule
from rdkit.Chem import Draw
# img = Draw.MolToImage(m2)
# img.save('test.png')


# drawing microviridin J macrocycle
m3 = Chem.MolFromSmiles('CC[C@H](C)[C@@H](C(=O)N[C@@H](CO)C(=O)N[C@H]1[C@H](OC(=O)C[C@H]2C(=O)N[C@H](C(=O)N[C@H]3CC[C](OC[C@@H](C(=O)N2)NC(=O)[C@@H]4CCCN4C(=O)[C@@H](NC(=O)[C@H](CCCC[NH2+]C(=O)CC[C@H](NC3=O)C(=O)N[C@@H](Cc5c[nH]c6c5cccc6)C(=O)O)NC(=O)[C@@H](NC1=O)CCCNC(=[NH2+])N)Cc7ccc(cc7)O)O)Cc8c[nH]c9c8cccc9)C)NC(=O)C')
# img3 = Draw.MolToImage(m3)
# img3.save('microviridin.png')

m = Chem.MolFromSmiles('Cc1ccccc1')
# img = Draw.MolToImage(m)
# img.save('trial2.png')

# reading a set of molecules
suppl = Chem.SDMolSupplier('RDKit-Tutorial/5ht3ligs.sdf')
for mol in suppl:
    print(mol.GetNumAtoms())

mols = [x for x in suppl]
print(len(mols))
print(suppl[0].GetNumAtoms())

mol4 = Chem.MolFromSmiles('C[C@H](O)c1ccccc1')
# img4 = Draw.MolToImage(mol4)
# img4.save('mol4.png')

# Print several forms of molecules
print(Chem.MolToSmiles(mol4))
print(Chem.MolToSmiles(mol4, isomericSmiles=False))
print(Chem.MolToSmiles(mol4, isomericSmiles=True))
print(Chem.MolToSmiles(mol4, kekuleSmiles=True))

print('----------------------------------')
m2 = Chem.MolFromSmiles('C1CCC1')
m2.SetProp("_Name", "cyclobutane")
print(Chem.MolToMolBlock(m2))

