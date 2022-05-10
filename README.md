# Altob

Abundance learning for ToBRFV variants. The primary purpose of the tool is:

* Estimating abundace of variants of concern from wastewater sequencing data

You can read more about how Altob works in the Alcov preprint, __[Alcov: Estimating Variant of Concern Abundance from SARS-CoV-2 Wastewater Sequencing Data](https://www.medrxiv.org/content/10.1101/2021.06.03.21258306v1)__

The tool can also be used for:

* Converting nucleotide and amino acid mutations for SARS-CoV-2 such as those found on https://covariants.org/variants/S.N501
* Determining the frequency of mutations of interest in BAM files
* Plotting the depth for each ARTIC amplicon (https://github.com/artic-network/artic-ncov2019/tree/master/primer\_schemes/nCoV-2019/V3)
* Comparing amplicon GC content with its read depth (as a measure of degredation)

The tool is under active development. If you have questions or issues, please open an issue on GitHub or email me (email in setup.py).

## Installing

The latest release can be downloaded from PyPI

`pip install altob`

This will install the Python library and the CLI.

To install the development version, clone the repository and run

`pip install .`

## Usage example

### Preprocessing

Altob expects a BAM file of reads aligned to the SARS-CoV-2 reference genome. For an example of how to process Illumina reads, check the `prep` directory.

### Estimating relative abundance of variants of concern:

```
altob find_lineages reads.bam
```

Finding lineages in BAM files for multiple samples:

```
altob find_lineages samples.txt
```

Where `samples.txt` looks like:

```
reads1.bam	Sample 1 name
reads2.bam	Sample 2 name
...
```

Optionally specify which VOCs to look for

```
altob find_lineages reads.bam lineages.txt
```

Where `lineages.txt` looks like:

```
Omicron
Delta
...
```

Optionally change minimum read depth (default 40)

```
altob find_lineages --min_depth=5 reads.bam
```

Optionally show how predicted mutation rates agree with observed mutation rates

```
altob find_lineages --show_stacked=True reads.bam
```

Use mutations which are found in multiple VOCs (can help for low coverage samples)

```
altob find_lineages --unique=False reads.bam
```

Plotting change in lineage distributions over time for multiple sites

```
altob find_lineages --ts samples.txt
```

Where `samples.txt` looks like:

```
reads1.bam	SITE1_2021-09-10
reads2.bam	SITE1_2021-09-12
...
reads3.bam	SITE2_2021-09-10
reads4.bam	SITE2_2021-09-12
...
```

### Converting mutation names:

```
$ altob nt A23063T
A23063T causes S:N501Y
$ altob aa S:E484K
G23012A causes S:E484K
```

### Finding mutations in BAM file:

```
altob find_mutants reads.bam
```

Finding mutations in BAM files for multiple samples:

```
altob find_mutants samples.txt
```

Where `samples.txt` looks like:

```
reads1.bam	Sample 1 name
reads2.bam	Sample 2 name
...
```

Running `find_mutants` will print the number of reads with and without each mutation in each sample and then generate a heatmap showing the frequencies for all samples.

You can also specify a custom mutations file:

```
altob find_mutants samples.txt mutations.txt
```

Where `mutations.txt` looks like:

```
S:N501Y
G23012A
...
```

### Getting the read depth for each amplicon

```
altob amplicon_coverage reads.bam
```

or

```
altob amplicon_coverage samples.txt
```

### Plotting amplicon GC content against amplicon depth

```
altob gc_depth reads.bam
```

or

```
altob gc_depth samples.txt
```
