class CompressedGene:
    def __init__(self, gene: str):
        # Every generated gene is stored in its compressed form
        self.bit_string: int = self._compress(gene)

    # Compress method
    def _compress(self, gene: str) -> int:
        # Sentinel one to avoid losing the left zeros
        self.bit_string: int = 1
        # Check every sequence character
        for nucleotide in gene.upper():
            # Displace to places to the left. Ex: 0b1 -> 0b100
            self.bit_string <<= 2
            # Apply and OR to the last 2 created digits. Ex: 0b100 |= 0b11 -> 0b111 
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide:{nucleotide}")
        return self.bit_string
    
    def decompress(self) -> str:
        # String to save the uncompressed sequence
        gene: str = ""
        # Check from right to left the bit_string in pairs
        for i in range(0, self.bit_string.bit_length()-1, 2):
            # Get the i-th bit pair: bit_string >> i
            # apply an AND door with [11] to that pair: (bit_string >> i) & 0b11
            # Ex: (29 >> 2) & 0b11 = (0b11101 >> 2) & 0b11 = (0b111) & 0b011 = 0b11
            bits: int = self.bit_string >> i & 0b11
            # Dependeing on the current value of bits append a char to gene
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits: {bits}")
        # Since the gene sequence is stored backwards, return the reversed version
        return gene[::-1]
    
    # When called via the print method, print the uncompressed version
    def __str__(self) -> str:
        return self.decompress()
    
if __name__ == "__main__":
    # library
    from sys import getsizeof
    # Original equence gene
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA"*100
    # original size in bytes
    print(f"original size in bytes: {getsizeof(original)}")

    # Compress the sequence
    compressed = CompressedGene(original)
    # Size of the compressed sequence
    print(f"Size of the compressed sequence in bytes: {getsizeof(compressed)}")
    # Comparison: origina vs decompressed
    print(f"original and decompressed are the same? {original == compressed.decompress()}")