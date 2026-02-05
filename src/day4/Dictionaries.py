Contacts={
    "Jeevan": "8431486175",
    "Rakshith": "9876543210",
    "Srujan": "9123456780"
}
Contacts["Shamanth"]="9876543210"

print(Contacts)

print(Contacts.get("Jeevan"))
print(Contacts.get("Rahul","Contact not found"))

for name, number in Contacts.items():
    print(f"Contact: {name} | Phone: {number}")