
# riceteacatpanda CTF 2020 <br/>
**Category: Forensics** <br/>
**Challenge Name:** <br/>
BASmati ricE 64

**Points:** <br/>
150

**Description:** <br/>
here's a flag in that bowl somewhere... <br/>
Replace all zs with _ in your flag and wrap in rtcp{...}. <br/>
[rice-bowl.jpg](rice-bowl.jpg)



**Solution:** <br/>
Using steghide, we get a txt file.
```
steghide --extract -sf rice-bowl.jpg
```
consisting of the text
```
³I··Y·ç;aÖx9Ì
÷ÏyÜÐ=Ý
```
The title hints at base64, so we encode the text to base 64 to get the flag.
```
s0m3t1m35zth1ng5zAr3z3nc0D3d
```
Don't forget to replace the z's with _'s

Flag: `rtcp{s0m3t1m35_th1ng5_Ar3_3nc0D3d}`
