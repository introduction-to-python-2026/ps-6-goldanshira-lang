def create_codon_dict(file_path):
    f = open(path,"r")
    rows = f.readlines()
    f.close()
    codon_dict = {}
    for lines in rows:
        parts = lines.strip().split('\t')
        codon = parts[0]
        amino = parts[2]
        codon_dict [codon] = amino
    return codon_dict
