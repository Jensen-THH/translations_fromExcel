import pandas as pd
import json
from googletrans import Translator


df = pd.read_excel('excel.xlsx')

translations_vi = {}
translations_lo = {}
def translate_language(language,key):
    key = key.replace('\n', ' ').replace('\r', ' ').replace('\"', "'").replace('_', ' ')
    translator = Translator()
    translation = translator.translate(key, dest=language)
    translated_text = translation.text
    print(f"Translated text: {key} - {translated_text} - {language} ")
    if translated_text == '':
        translated_text = key
    return translated_text

for index, row in df.iterrows():
    key = str(row[0]).strip().replace('\n', '_').replace('\"', "'").replace(':', '_') if isinstance(row[0], str) else str(row[0])
    key = ''.join(key.split())
    value_vi = str(row[1]).replace('\n', '').strip().replace('\r', '').replace('\"', "'").replace("' ", "'")  if pd.notnull(row[1]) else translate_language('vi',key)
    value_lo = str(row[2]).replace('\n', '').strip().replace('\r', '').replace('\"', "'").replace("' ", "'")  if pd.notnull(row[2]) else translate_language('lo',key)
    value_vi = ' '.join(value_vi.split())
    value_lo = ' '.join(value_lo.split())
    translations_vi[key] = value_vi
    translations_lo[key] = value_lo

translations = {
    'translations_vi': translations_vi,
    'translations_lo': translations_lo
}

file_path = 'translations.json'

json_data = json.dumps(translations, indent=4, ensure_ascii=False)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(json_data)

print(f"The translations have been exported to {file_path} successfully!")



