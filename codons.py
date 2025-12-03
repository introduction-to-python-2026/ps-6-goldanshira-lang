def create_codon_dict(file_path):
    with open(file_path, "r") as f:
        rows = f.readlines()

    codon_dict = {}
    for line in rows:
        parts = line.strip().split('\t')
        codon = parts[0]
        amino = parts[2]
        codon_dict[codon] = amino

    return codon_dict
