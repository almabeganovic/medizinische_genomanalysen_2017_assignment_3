#! /usr/bin/env python2

import vcf
from vcf import utils
import hgvs

__author__ = 'Alma Beganovic'


class Assignment3:
    def __init__(self):
        # Check if pyvcf is installed
        print ("PyVCF version: %s") % vcf.VERSION
        # Check if hgvs is installed
        print ("HGVS version: %s") % hgvs.__version__

        # Initialize reader for the three vcf files
        self.vcf_reader_mother = vcf.Reader(open('AmpliseqExome.20141120.NA24143.vcf','r'))
        self.vcf_reader_father = vcf.Reader(open('AmpliseqExome.20141120.NA24149.vcf','r'))
        self.vcf_reader_son = vcf.Reader(open('AmpliseqExome.20141120.NA24385.vcf','r'))

    # the total number of identified variants in the mother
    def get_total_number_of_variants_mother(self):

        number_of_variants_mother = 0
        for record in self.vcf_reader_mother:
            number_of_variants_mother += 1

        print ("-total_number_of_variants_mother:")
        print (number_of_variants_mother)


    # the total number of identified variants in the father
    def get_total_number_of_variants_father(self):

        number_of_variants_father = 0
        for record in self.vcf_reader_father:
            number_of_variants_father += 1

        print ("-total_number_of_variants_father:")
        print (number_of_variants_father)

    
    # the number of identified variants shared by father and son
    def get_variants_shared_by_father_and_son(self):

        records = 0
        for record in self.vcf_reader_father:
            if record in self.vcf_reader_son:
                records += 1

        print ("-variants_shared_by_father_and_son:")
        print (records)

    # the number of identified variants shared by mother and son
    def get_variants_shared_by_mother_and_son(self):

        records = 0
        for record in self.vcf_reader_mother:
            if record in self.vcf_reader_son:
                records += 1

        print ("-variants_shared_by_mother_and_son:")
        print (records)

    # the number of identified variants shared by trio
    def get_variants_shared_by_trio(self):

        records = 0
        for record in self.vcf_reader_father:
            if record in self.vcf_reader_son and record in self.vcf_reader_mother:
                records += 1

        print ("-variants_shared_by_trio:")
        print (records)

    # VCF containing all variants of the trio
    def merge_mother_father_son_into_one_vcf(self):

        merge_file = open("merge_file.vcf", "w")
        writer = vcf.Writer(merge_file, self.vcf_reader_mother, "\n")
        for records in utils.walk_together(self.vcf_reader_mother, self.vcf_reader_father, self.vcf_reader_son):
            for entry in records:
                if entry is not None:
                    writer.write_record(entry)
        print ("-merge_mother_father_son_into_one_vcf:")
        print("merge VCF successfull")


    # Convert the first 100 variants identified in the son into the corresponding transcript HGVS.
    # Each variant should be mapped to all corresponding transcripts.
    # Pointer:- https://hgvs.readthedocs.io/en/master/examples/manuscript-example.html#project-genomic-variant-to-a-new-transcript
    def convert_first_variants_of_son_into_HGVS(self):

        print("-first_variants_of_son:")
        print ("to do")


    def print_summary(self):
        print("All results:")
        self.get_total_number_of_variants_mother()
        self.get_total_number_of_variants_father()
        self.get_variants_shared_by_father_and_son()
        self.get_variants_shared_by_mother_and_son()
        self.get_variants_shared_by_trio()
        self.merge_mother_father_son_into_one_vcf()
        self.convert_first_variants_of_son_into_HGVS()



if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
    assignment1.print_summary()

