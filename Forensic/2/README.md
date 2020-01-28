# riceteacatpanda CTF 2020 <br/>
**category: Forensics ** <br/>
**Challenge Name:** <br/>
cat-chat

**Points:** <br/>
125

**Description:** <br/>

nyameowmeow nyameow nyanya meow purr nyameowmeow nyameow nyanya meow purr nyameowmeow nyanyanyanya nyameow meow purr meow nyanyanyanya nya purr nyanyanyanya nya meownyameownya meownyameow purr nyanya nyanyanya purr meowmeownya meowmeowmeow nyanya meownya meowmeownya purr meowmeowmeow meownya purr nyanyanyanya nya nyameownya nya !!!!

**Hint:** <br/>
once you've figured this out, head to discord's #catchat channel.

**Solution:** <br/>
The text consisted of three repeating words `nya`, `meow` and `purr`. It hints of morse code, so I converted `nya` to '.', `meow` to '-' and `purr` to '/'. Used an online morse code decoder to obtain the text.

The discord channel, was filled with encoded chats by two bots. So, I converted 'rtcp' to morse code, encoded them and searched for the text in discord to get flag.

Flag: `rtcp{th15_1z_a_c4t_ch4t_n0t_a_m3m3_ch4t}`

