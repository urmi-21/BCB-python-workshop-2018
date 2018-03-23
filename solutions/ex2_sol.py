'''
BCBGSO Basic Python workshop
Exercise 2

@author urmi
'''


#Don't change this
codons=['TTT','TTG','CTC','ATT','ATG','GTA','TAC','TAA','TAG','CAT','CAC','CAA','AAC','AAG','GAT','TGC','TGA','TGG','CGA','AGC','AGG','GGG','YYPQ','SDEH','PSDL']
'''
A codon is fundamental unit of the genetic code, defined as sequence of three nucleotides
Given above, "codons" is a list containg some of the 64 total codons.
For the following questions change the list using your code and not by editing the list declaration
'''
#1. The last three elements in the list are not codons. Remove these from the codon list

#2. Add the codons 'GGT', 'TTC' and 'TTA' to the list

#3. How many codons are there in the list

#Don't change this
peptide='MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQDQTSFQKENC'
'''
A protein sequence is written by writing individual amino acids,represented by single letters, in a particular order.
The variable "peptide" contains the protein sequence for the human tumor protein p53. This protein acts as a tumor suppressor by regulating cell division.
'''

#4. Find out how many unique amino acids are present in the human tumor protein p53. Hint use set()
print set(peptide)

#Don't change this
#Thanks Yuan Wang, BCB for the dict code
geneticCode = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
              "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
              "UAU":"Y", "UAC":"Y", "UAG":"STOP",
              "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
              "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
              "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
              "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
              "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
              "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
              "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
              "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
              "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
              "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
              "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
              "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
              "GGU":"G", "GGC":"G", "GGA":"G", }

'''
Above "geneticCode" is a dict which maps an RNA codon to an amino acid letter.
'''

#5. For the sequence GGU GGC AAA CUA UAG UCG CGG print the coressponding amino acid sequence, using the above defined geneticCode.

print geneticCode['GGU']
