# Caesar Cipher – Classic Encryption Tool

  SkillCraft Cybersecurity Internship – Task 1    
  Author:   B S Namith Kumar  
  Domain:   Cybersecurity

---

## Project Overview

This is a Python-based Caesar Cipher tool developed as part of my internship at SkillCraft Technology. It demonstrates classical encryption, brute-force decryption, and the fundamentals of cryptography using clean, readable code.

  Features:  

- Encrypt a message using a key  
- Decrypt a message with a known key  
- Crack a message using brute-force when the key is unknown

---

## Learning Outcomes

- Understood classical substitution cipher mechanisms  
- Implemented encryption and decryption logic in Python  
- Practiced ethical brute-force decryption  
- Improved code structure and user interaction in CLI-based tools

---

## Sample Run

### Encrypt a Message
```bash
python main.py encrypt --text "HELLO WORLD" --key 3
```
  Output:  
```
Original Text : HELLO WORLD  
Encrypted Text: KHOOR ZRUOG
```

---

### Decrypt with Known Key
```bash
python main.py decrypt --text "KHOOR ZRUOG" --key 3
```
  Output:  
```
Encrypted Text: KHOOR ZRUOG  
Decrypted Text: HELLO WORLD
```

---

### Brute-force Decryption (Unknown Key)
```bash
python main.py brute --text "KHOOR ZRUOG"
```
  Output:  
```
Trying all possible keys...  
Key 1: JGNNQ YQTNF  
Key 2: IFMMP XPSME  
Key 3: HELLO WORLD  <-- Most likely correct  
Key 4: GDKKN VNQKC  
Key 5: FCJJM UMPJB  
...
Key 25: IDMMN XPTME
```

---

## Notes

- Works with   uppercase English letters (A–Z)   only  
- Spaces and symbols remain unchanged  
- Key must be between 1 and 25 (due to 26-letter rotation logic)
