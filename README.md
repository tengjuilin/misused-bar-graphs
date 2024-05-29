# ML prediction with AuNP protein corona

## Raw data acquisition (`raw_data`)

Refer to [README for raw data](raw_data/README.md). Briefly, protein accession ID of detected proteins are given. The detected protein's log2(fold change) and -log10(p-value) of AuNP experimental group compared to control group without AuNP is reported.

## Data collection (`data-acquisition.ipynb`)

The data acquired here is only used for prediction *of* protein corona based on [Ouassil et al. (2022)](https://www.science.org/doi/10.1126/sciadv.abm0898).

### Uniport

- Amino acid sequence, protein name, gene name, entry name, organism, and comments are acquired from Uniport using protein accession ID.
  - **Intermediate output**: `uniport_data/<ACCESSION_ID>.json` - protein information from Uniport data base
  - **Intermediate output**: `fasta_data/batch_<i>.fasta` - FASTA file containing amino acid sequences for NetSurfP 3.0 analysis
  - Amino acid sequences are used for BioPython calculations.
- Quality control
  - Proteins with amino acid sequence X (unknown amino acid X cannot give molecular weight) and U (nonstandard amino acid U "selenocysteine") are discarded
  - Proteins must have 10-5000 amino acids (required by NetSurfP 3.0)

- **Output**: `properties_data/text_properties.csv` - Text-based properties
- **Output**: `properties_data/log2_fold_change.csv` - log2 fold changes of 4968 proteins of interest
- **Output**: `properties_data/log10_pvalue.csv` - -log10 p-value of 4968 proteins of interest

### BioPython

- Protein properties based on amino acid sequences are calculated with BioPython

### NetSurfP 3.0

- NetSurfP data is acquired in batches
  - Data acquisition is time consuming (cloud-connection and queue)
  - Resulting data is large in size (MB - GB) because property is based on every amino acid
- Polarity, secondary structure, and exposed amino acid properties are calculated
- **Intermediate output**: `netsurfp_data/batch_<i>/<iiii>_<ACCESSION_ID>` - folder contains predicted properties of proteins

### Protein property merging

- **Output**: `numerical_properties.csv` - numerical properties of proteins derived from BioPython and NetSurfP

## Data exploration and machine learning (`data-exploration.ipynb`)
