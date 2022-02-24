import re
from typing import Text
import unicodedata

text = '    CLEANS ing  によりテキストデータを変換すると　トラブルが少なくなります。'
print('Before:', text)

translation_table =str.maketrans(dict(zip('()!', '（）！')))
text = unicodedata.normalize('NFKC',text).translate(translation_table)
text = re.sub(r'\s+','　',text)
print('After:',text)