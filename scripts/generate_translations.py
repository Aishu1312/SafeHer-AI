import os
import json
import shutil

# Mapping of language names to ISO codes
LANG_CODES = {
    "Hindi": "hi", "Marathi": "mr", "Gujarati": "gu", "Punjabi": "pa",
    "Bengali": "bn", "Assamese": "as", "Odia": "or", "Tamil": "ta",
    "Telugu": "te", "Kannada": "kn", "Malayalam": "ml", "Urdu": "ur",
    "Sanskrit": "sa", "Konkani": "gom", "Nepali": "ne", "Manipuri": "mni-Mtei",
    "Dogri": "doi", "Kashmiri": "ks", "Sindhi": "sd", "Maithili": "mai",
    "Bhojpuri": "bho",
    "Bodo": "hi", "Santali": "hi", "Tulu": "kn", "Rajasthani": "hi", 
    "Chhattisgarhi": "hi", "English (International)": "en"
}

def generate_all_translations():
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    translations_dir = os.path.join(app_dir, "localization", "translations")
    
    en_path = os.path.join(translations_dir, "en.json")
    
    for lang_name, lang_code in LANG_CODES.items():
        if lang_code == "en":
            continue
            
        out_path = os.path.join(translations_dir, f"{lang_code}.json")
        if not os.path.exists(out_path):
            shutil.copy(en_path, out_path)
            print(f"Created fallback translations for {lang_name} ({lang_code})")

if __name__ == "__main__":
    generate_all_translations()
    print("Done generating JSON architecture.")
