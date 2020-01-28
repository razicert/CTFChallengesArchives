# riceteacatpanda CTF 2020 <br/>
**category: Cryptography** <br/>
**Challenge Name:** <br/>
Code On

**Points:** <br/>
500

**Description:** <br/>

My houseplant and I were working on a biology assignment together. Yes, my houseplant. Don't question it. Anyways, she ended up giving me a new cipher to use in my next project! So I'm giving it to my biology friends to see if they can solve it. They are, after all, studying DNA and mRNA right now.

AUGCAAGGUCUCUUGACCCAGUGGAUACUAAAUGCCUGGAAGGUAGCAUACUAG

Key: 6, 3, 4, 3, 1, 9, 8, 3, 3, 2, 7, 4, 1, 2, 4, 1


**Hint:** <br/>
Make sure to encase the plaintext with rtcp{} Spaces are represented by a underscore, (_)

**Solution:** <br/>
Codon

AUG CAA GGU CUC UUG ACC CAG UGG AUA CUA AAU GCC UGG AAG GUA GCA UAC UAG <br/>
Index of Amino Acids <br/>
Index	Codon	Amino Acid <br/>
01	CAA	Glutamine <br/>
02	GGU	Glycine <br/>
03	CUC	Leucine <br/>
04	UUG	Leucine <br/>
05	ACC	Threonine <br/>
06	CAG	Glutamine <br/>
07	UGG	Tryptophan <br/>
08	AUA	Isoleucine <br/>
09	CUA	Leucine <br/>
10	AAU	Asparagine <br/>
11	GCC	Alanine <br/>
12	UGG	Tryptophan <br/>
13	AAG	Lysine <br/>
14	GUA	Valine <br/>
15	GCA	Alanine <br/>
16	UAC	Tyrosine <br/>
Applying key <br/>
Key	Amino Acid	Char <br/>
6	Glutamine	m <br/>
3	Glycine	y <br/>
4	Leucine	c <br/>
3	Leucine	u <br/>
1	Threonine	T <br/>
9	Glutamine	e <br/>
8	Tryptophan	h <br/>
3	Isoleucine	o <br/>
3	Leucine	u <br/>
2	Asparagine	s <br/>
7	Alanine	e <br/>
4	Tryptophan	p <br/>
1	Lysine	L <br/>
2	Valine	a <br/>
4	Alanine	n <br/>
1	Tyrosine	T <br/>
Flag: `rtcp{my_cute_houseplant}`
