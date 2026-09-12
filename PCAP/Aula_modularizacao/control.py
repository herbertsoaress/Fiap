from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# Create
# Read
# Upadte
# Delete

#Read
def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return[]

#Create 
def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

#Upadate
def upadate_leads(email, new_status):
    leads = read_leads()
    for lead in leads:
        if lead["email"] == email:
            lead["status"] = new_status
            DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")
            return True
    return False

#Delete
def delete_lead(email):
    leads = read_leads()
    novos_leads = [lead for lead in leads if lead["email"] != email]
    if len(novos_leads) == len(leads):
        return False
    DB_PATH.write_text(json.dumps(novos_leads, ensure_ascii=False, indent=2), encoding="utf-8")
    return True
    

