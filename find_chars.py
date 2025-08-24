import os

def find_unusual_chars():
    unusual_chars = set()
    
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(('.htm', '.html')):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='windows-1252') as f:
                    content = f.read()
                
                for char in content:
                    if not char.isprintable() or ord(char) > 127:
                        unusual_chars.add((char, ord(char), hex(ord(char))))
    
    if unusual_chars:
        print("Unusual characters found:")
        for char, decimal, hexval in sorted(unusual_chars, key=lambda x: x[1]):
            print(f"'{char}' (decimal: {decimal}, hex: {hexval})")
    else:
        print("No unusual characters found.")

if __name__ == "__main__":
    find_unusual_chars()
