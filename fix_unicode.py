"""Fix Unicode characters in all Python files"""
import os
import glob

# Unicode replacements
replacements = {
    '+': '+',
    'X': 'X',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
}

# Get all Python files
py_files = glob.glob('*.py')

for file in py_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace all Unicode characters
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed: {file}")
    except Exception as e:
        print(f"Error fixing {file}: {e}")

print("\nAll files fixed!")
