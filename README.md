## 🔐 Caesar Cipher Tool

A sleek, interactive Python implementation of the classic Caesar Cipher encryption algorithm with multiple attack modes and a user-friendly CLI interface.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **🔒 Encryption**: Securely encrypt messages using a custom shift value
- **🔓 Decryption**: Decrypt messages when you know the shift key
- **🔎 Brute Force Attack**: Test all 26 possible Caesar Cipher combinations automatically
- **🎯 User-Friendly CLI**: Interactive menu-driven interface
- **✅ Input Validation**: Safe handling of user inputs with error checking
- **⚡ Efficient**: Handles large shift values with modular arithmetic
- **🔤 Preserves Formatting**: Maintains spaces, punctuation, and case sensitivity

## 🚀 Installation

### Requirements
- Python 3.6 or higher

### Steps

1. Clone the repository:
```bash
git clone https://github.com/Shamirali/caesar-cipher.git
cd caesar-cipher
```

2. Verify Python installation:
```bash
python3 --version
```

## 💻 Usage

Run the program from the command line:

```bash
python3 caesar_cipher.py
```

### Interactive Menu

The program presents four options:

```
===== Caesar Cipher Tool =====
1. Encrypt
2. Decrypt
3. Brute Force Attack
4. Exit
```

## 📚 How It Works

### Caesar Cipher Basics

The Caesar Cipher is one of the simplest encryption techniques, dating back to Julius Caesar. It works by:

1. **Shifting letters**: Each letter is shifted by a fixed number of positions in the alphabet
2. **Wrapping around**: When reaching the end of the alphabet, it wraps to the beginning
3. **Preserving case**: Uppercase and lowercase letters maintain their case
4. **Keeping non-letters**: Spaces, punctuation, and numbers remain unchanged

**Example**: With a shift of 3:
- A → D
- B → E
- X → A
- Y → B
- Z → C

### Algorithm Explanation

```python
(char_position + shift) mod 26 = new_position
```

## 🎯 Examples

### Encrypt a Message
```
Choose an option (1-4): 1
Enter message to encrypt: HELLO WORLD
Enter shift value: 3

✅ Encrypted Message: KHOOR ZRUOG
```

### Decrypt a Message
```
Choose an option (1-4): 2
Enter message to decrypt: KHOOR ZRUOG
Enter shift value: 3

✅ Decrypted Message: HELLO WORLD
```

### Brute Force Attack
```
Choose an option (1-4): 3
Enter message for brute force: KHOOR ZRUOG

🔎 Brute Force Results:
Shift  0: KHOOR ZRUOG
Shift  1: JGNNQ YQTNF
Shift  2: IFMMP XPSME
Shift  3: HELLO WORLD    ← Original message!
Shift  4: GDKKN VNQKC
...
```

## 🔬 Code Structure

### Main Functions

- **`encrypt_caesar(text, shift)`**: Encrypts text with given shift value
- **`decrypt_caesar(text, shift)`**: Decrypts text (calls encrypt with negative shift)
- **`brute_force(text)`**: Tests all 26 possible shifts
- **`get_shift_value()`**: Safely validates integer input
- **`main()`**: Manages the interactive menu loop

## 🎓 Learning Resources

- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Cryptography Basics](https://www.khanacademy.org/computing/computer-science/cryptography)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## ⚠️ Security Note

**⚠️ This tool is for educational purposes only!** The Caesar Cipher is extremely weak by modern cryptography standards and should never be used for real data protection. Modern encryption uses sophisticated algorithms like AES-256.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Potential Enhancements

- [ ] Support for multiple languages
- [ ] Vigenère Cipher implementation
- [ ] Frequency analysis tool
- [ ] GUI version using tkinter
- [ ] File encryption/decryption
- [ ] Unit tests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shamirali**

- GitHub: [@Shamirali](https://github.com/Shamirali)

## 🙏 Acknowledgments

- Inspired by classical cryptography
- Built for educational purposes
- Thanks to everyone learning cryptography!
