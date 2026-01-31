import json

# Deine Datenbank - hier fügen wir die Produkte ein
# Wenn du einen Affiliate-Link hast, ersetzt du "DEIN_LINK"
products = [
    {
        "title": "Pro Gaming Mechanical Keyboard",
        "price": "$59.99",
        "desc": "Ultra-fast response for competitive gaming. Global shipping.",
        "link": "DEIN_LINK_VON_AMAZON",
        "cat": "Electronics"
    },
    {
        "title": "Industrial Grade Concrete Drill",
        "price": "$285.00",
        "desc": "Heavy duty tool for professional masonry work.",
        "link": "DEIN_LINK_VON_FIRMA_X",
        "cat": "Tools"
    },
    {
        "title": "Smart AI Home Controller",
        "price": "$129.00",
        "desc": "The brain for your smart home setup. Compatible with AEGIS nodes.",
        "link": "DEIN_LINK",
        "cat": "Tech"
    }
]

def build_db():
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4)
    print("✅ products.json wurde erstellt! Lade diese Datei jetzt auch auf GitHub hoch.")

if __name__ == "__main__":
    build_db()