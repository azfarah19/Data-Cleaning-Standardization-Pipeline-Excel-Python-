import pandas as pd
import re
import os

# Define input and output 
input_file = "sample_data/sample_input.xlsx"
output_file = "outputs/standardized_output.xlsx"

df = pd.read_excel(input_file)

def clean_text(text):
    if pd.isna(text) or not str(text).strip():
        return ""
    text = str(text).lower().strip().replace("-", " ")
    text = re.sub(r'\s+', ' ', text)
    return text

def adjust_building(pm_raw, pf_raw):
    pm_clean = clean_text(pm_raw)
    pf_clean = clean_text(pf_raw)

    if not pm_clean or not pf_clean:
        return pm_clean, pf_clean

    pm_has_tower = "tower" in pm_clean
    pf_has_tower = "tower" in pf_clean

    def fix(text, other_has_tower):
        cleaned = clean_text(text)
        if 'tower' not in cleaned and other_has_tower:
            if re.search(r' (?<!tower )(\d)$', cleaned):
                cleaned = re.sub(r' (?<!tower )(\d)$', r' tower \1', cleaned)
            else:
                cleaned += ' tower'
        return cleaned.strip()

    adj_pm = fix(pm_raw, pf_has_tower)
    adj_pf = fix(pf_raw, pm_has_tower)
    return adj_pm, adj_pf

adjusted = df.apply(lambda row: adjust_building(
    row['PM Building Level'],
    row['PF Data.PF Building Level']
), axis=1)

df[['PM Building Adjusted', 'PF Building Adjusted']] = pd.DataFrame(adjusted.tolist(), index=df.index)

# Save to OUTPUT file 
df.to_excel(output_file, index=False)

print("Saved output to:", output_file)
print(df[['PM Building Level', 'PF Data.PF Building Level', 'PM Building Adjusted', 'PF Building Adjusted']].head(10))
