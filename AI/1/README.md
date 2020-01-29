# riceteacatpanda CTF 2020 <br/>
**category: Cryptography** <br/>
**Challenge Name:** <br/>
Meta-Dreams

**Points:** <br/>
1750

**Description:** <br/>

In 2015, computer scientists made Deep Dreams. I dreamed of the arctic pandas. They could reconstruct the style of anything.

But now, I've been dreaming in color- starting from the farthest, blackest corners of my imagination. Can you tell me which one?


**Hint #1:** <br/>
Flag is to be submitted in hex:

FFFFFF or rtcp{FFFFFF}

**Hint #2:** <br/>
https://github.com/JEF1056/riceteacatpanda/tree/master/Meta-Dreams (750)

**Solution:** <br/>
A pth file is given which is a pytorch save file.
We use the program in https://github.com/JEF1056/Reconstruction-Style which created by challenge designer.
We use the following command:
```
python src/main.py test --content-image input.png --output-image output.png --model Dream.pth --content-size 224 --original-colors 0 --cuda 0
```
The RGB value of the image in HEX is the flag.

Flag: `rtcp{78857C}`
