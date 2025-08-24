import os

replacements = {
    'á': '&aacute;', 'é': '&eacute;', 'í': '&iacute;', 'ó': '&oacute;', 'ú': '&uacute;',
    'ñ': '&ntilde;', 'Á': '&Aacute;', 'É': '&Eacute;', 'Í': '&Iacute;', 'Ó': '&Oacute;',
    'Ú': '&Uacute;', 'Ñ': '&Ntilde;', '¿': '&iquest;', '¡': '&iexcl;', 'à': '&agrave;',
    'â': '&acirc;', 'ä': '&auml;', 'è': '&egrave;', 'ê': '&ecirc;', 'ë': '&euml;',
    'î': '&icirc;', 'ï': '&iuml;', 'ô': '&ocirc;', 'ö': '&ouml;', 'ù': '&ugrave;',
    'û': '&ucirc;', 'ü': '&uuml;', 'ç': '&ccedil;', 'À': '&Agrave;', 'Â': '&Acirc;',
    'È': '&Egrave;', 'Ê': '&Ecirc;', 'Ç': '&Ccedil;', 'œ': '&oelig;', 'Œ': '&OElig;',
    '«': '&laquo;', '»': '&raquo;', '’': '&rsquo;', '‘': '&lsquo;', '“': '&ldquo;',
    '”': '&rdquo;', '—': '&mdash;', '–': '&ndash;', '…': '&hellip;', chr(160): '&nbsp;',    # Non-breaking space (0xa0)
'©': '&copy;',         # Copyright symbol (0xa9)
'±': '&plusmn;',       # Plus-minus sign (0xb1)
'Ë': '&Euml;',         # Capital E with diaeresis (0xcb)
'Ï': '&Iuml;',         # Capital I with diaeresis (0xcf)
    # German umlauts and ß
    'Ä': '&Auml;', 'Ö': '&Ouml;', 'Ü': '&Uuml;', 'ä': '&auml;', 'ö': '&ouml;', 'ü': '&uuml;', 'ß': '&szlig;'
}

def replace_text(text):
    for char, entity in replacements.items():
        text = text.replace(char, entity)
    return text

def main():
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(('.htm', '.html')):
                filepath = os.path.join(root, file)
                print(f"Processing {filepath}")
                with open(filepath, 'r', encoding='windows-1252') as f:
                    content = f.read()
                new_content = replace_text(content)
                with open(filepath, 'w', encoding='windows-1252') as f:
                    f.write(new_content)

if __name__ == "__main__":
    main()
