import os
import re
import json

def extract_strings(directory):
    pattern = re.compile(r"_\(['\"](.*?)['\"]\)")
    strings = set()
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and 'site-packages' not in root and '.venv' not in root:
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    for match in matches:
                        strings.add(match)
                        
    # Add a few manual ones that might be dynamically generated
    strings.update([
        "Mother", "Father", "Sister", "Brother", "Friend", "Husband", "Wife", "Office", "Police", "Security", "Other",
        "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Unknown",
        "Incoming Call", "Mobile", "Accept", "Decline", "Call Ended", "Call Declined",
        "Safe", "Unsafe", "Emergency Message", "Directions", "Distance"
    ])
    
    return sorted(list(strings))

if __name__ == "__main__":
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    extracted = extract_strings(app_dir)
    
    # Create the en.json dictionary
    en_dict = {key: key for key in extracted}
    
    # Also add languages to translation dictionary
    languages = [
        "English", "Hindi", "Marathi", "Gujarati", "Punjabi", "Bengali", "Assamese",
        "Odia", "Tamil", "Telugu", "Kannada", "Malayalam", "Urdu", "Sanskrit",
        "Konkani", "Nepali", "Manipuri", "Bodo", "Dogri", "Kashmiri", "Santali",
        "Sindhi", "Maithili", "Bhojpuri", "Tulu", "Rajasthani", "Chhattisgarhi", "English (International)"
    ]
    for lang in languages:
        en_dict[lang] = lang
        
    out_path = os.path.join(app_dir, "localization", "translations", "en.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(en_dict, f, indent=4, ensure_ascii=False)
        
    print(f"Extracted {len(en_dict)} strings to {out_path}")
