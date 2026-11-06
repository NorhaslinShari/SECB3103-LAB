import streamlit as st
from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def retrieve_data(id):
    Entrez.email = "norhaslinshari05@gmail.com"
    handle = Entrez.efetch(db='protein', id=id, rettype='fasta', retmode='text')

    record = SeqIO.read(handle, 'fasta')

    return record

def get_basic_analysis(sequence):
    seq_analysis = ProteinAnalysis(str(sequence))

    length = len(sequence)
    amino_acid_composition = seq_analysis.count_amino_acids()
    molecular_weight = seq_analysis.molecular_weight()
    isoelectric_point = seq_analysis.isoelectric_point()

    return length, amino_acid_composition, molecular_weight, isoelectric_point

st.title('🧬 Lab 1 - NORHASLIN BINTI SHARI')

protein_id = st.text_input('Enter Uniprot ID')
retrieve = st.button('Retrieve')


if retrieve:
    if protein_id!="":
        data = retrieve_data(protein_id)
        length, composition, mol_w, pi = get_basic_analysis(data.seq)

        col1, col2 = st.columns([2,1.5])

        with col1:
            st.subheader("Retrieved Protein")

            st.write("Name:", data.name)
            st.write("Description:", data.description)
            st.write("Sequence:", str(data.seq))

        with col2:
            st.subheader('Basic Protein Analysis')

            st.write("Sequence Length:", str(length))
            st.write("Amino Acid Composition:", str(composition))
            st.write("Molecular Weight:", str(mol_w))
            st.write("Isoelectric Point:", str(pi))
    else: 
        st.warning('Please enter Uniprot ID')
