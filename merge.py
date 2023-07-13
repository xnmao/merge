from PyPDF2 import PdfReader, PdfWriter


stream = {
    'acs.jpclett.2c02873.pdf': [0],
    's41524-021-00514-8.pdf': [0],
    'acs.jpcc.0c01070.pdf': [0],
    's12274-022-5128-2.pdf': [0],
    'Advanced Optical Materials - 2022 - Chen - Kinetics‐Controlled Interfacial Synthesis of Janus and Patchy Heterostructures.pdf': [0, 6],
    's41467-022-30523-0.pdf': [0, 7],
    'd1ee03687d.pdf': [0],
    'Angew Chem Int Ed - 2022 - Zhang - Superlattice in a Ru Superstructure for Enhancing Hydrogen Evolution.pdf': [0],
    's41467-021-26316-6.pdf': [0, 8],
    'Advanced Materials - 2021 - Wu - 2D Molecular Sheets of Hydrogen‐Bonded Organic Frameworks for Ultrastable Sodium‐Ion.pdf': [0, 5],
    'Angew Chem Int Ed - 2021 - Jin - A Top‐Down Strategy to Realize Surface Reconstruction of Small‐Sized Platinum‐Based.pdf': [0],
    'Angew Chem Int Ed - 2021 - Huang - Size‐Dependent Selectivity of Electrochemical CO2 Reduction on Converted In2O3.pdf': [0],
}

writer = PdfWriter()
for fn, index in stream.items():
    reader = PdfReader(fn)
    for i in index:
        writer.add_page(reader.pages[i])
writer.write(open('My_Publications.pdf', 'wb'))
