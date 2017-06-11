#!/usr/local/bin/python

import sys

def count_kmers(kmer_length, genome_text):
    count = {}
    for i in range(len(genome_text)-kmer_length+1):
        pattern = genome_text[i:i+kmer_length]
        count[i] = pattern_count(pattern, genome_text)
    return count

def pattern_count(pattern, genome_text):
    count = 0
    for i in range(len(genome_text)-len(pattern)+1):
        if genome_text[i:i+len(pattern)] == pattern:
            count = count+1
    return count

def main(kmer_length, genome_text):
    kmer_dict = count_kmers(kmer_length, genome_text)
    print(kmer_dict)

if __name__ == "__main__":
    main(int(sys.argv[1]), sys.argv[2])
