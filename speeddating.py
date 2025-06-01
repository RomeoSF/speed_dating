import tkinter as tk
from tkinter import PhotoImage
import random
import os

# Karaktärer med namn och bildvägar
karaktarer = [
    {"namn": "Alex", "poang": 0, "bild": "alex.jpg"},
    {"namn": "Sam", "poang": 0, "bild": "sam.jpg"},
    {"namn": "Jamie", "poang": 0, "bild": "jamie.jpg"}
]

# Globala variabler
index = 0
val_frame = None
timer_id = None
spel_nummer = 1  # Håller koll på vilken omgång det är
aktioner_kvar = 5  # Antal aktioner per dejt (ändrat från 3 till 5)

# Skapa huvudfönster
root = tk.Tk()
root.title("Speeddating Simulator")
root.geometry("500x450")

# Bildlabel
bild_label = tk.Label(root)
bild_label.pack(pady=10)

namn_label = tk.Label(root, text="", font=("Helvetica", 16))
namn_label.pack(pady=10)

svar_label = tk.Label(root, text="", font=("Helvetica", 12))
svar_label.pack(pady=10)

# Räknare för aktioner kvar
aktioner_label = tk.Label(root, text="", font=("Helvetica", 10), fg="blue")
aktioner_label.pack(pady=5)

# Slumpade svar för olika val
positiva_svar = [
    "Bra val!", "Det gillade jag!", "Så charmigt!", "Du är rolig!",
    "Imponerande!", "Härligt att höra!", "Du verkar trevlig!"
]

neutrala_svar = [
    "Hmm, inte imponerad...", "Okej då...", "Intressant...", 
    "Jaha...", "Mm-hm...", "Jo då...", "Aha..."
]

negativa_svar = [
    "Det föll inte i smaken!", "Awkward...", "Ehh... nästa ämne?",
    "Det var ju... speciellt.", "Okej... vi går vidare.", "Hmm... nej.",
    "Det var inte så bra..."
]

# Funktion: Ladda och visa bild
def visa_bild(bildvag):
    try:
        if os.path.exists(bildvag):
            # Ladda bilden
            img = PhotoImage(file=bildvag)
            # Ändra storlek på bilden (om den är för stor)
            # PhotoImage kan bara hantera .png, .gif, .ppm/pgm
            bild_label.config(image=img)
            bild_label.image = img  # Behöver spara referens
        else:
            # Om bilden inte finns, visa placeholder
            bild_label.config(image="", text=f"📷\n(Bild saknas:\n{bildvag})", 
                            font=("Helvetica", 10), fg="gray")
    except Exception as e:
        # Om något går fel med bildladdning
        bild_label.config(image="", text="📷\n(Kunde inte ladda bild)", 
                        font=("Helvetica", 10), fg="gray")

def val1():
    global aktioner_kvar, timer_id
    # Slumpa typ av svar
    svar_typ = random.choice(["positiv", "neutral", "negativ"])
    
    if svar_typ == "positiv":
        karaktarer[index]["poang"] += 1
        svar = random.choice(positiva_svar)
    elif svar_typ == "neutral":
        karaktarer[index]["poang"] += 0
        svar = random.choice(neutrala_svar)
    else:  # negativ
        karaktarer[index]["poang"] -= 1
        svar = random.choice(negativa_svar)
    
    svar_label.config(text=svar)
    
    # Minska aktioner och uppdatera räknare
    aktioner_kvar -= 1
    uppdatera_aktioner_display()
    
    # Kontrollera om inga aktioner kvar
    if aktioner_kvar <= 0:
        if timer_id:
            root.after_cancel(timer_id)  # Avbryt timern
        root.after(1500, byt_dejt)  # Kort paus innan nästa dejt

def val2():
    global aktioner_kvar, timer_id
    # Slumpa typ av svar
    svar_typ = random.choice(["positiv", "neutral", "negativ"])
    
    if svar_typ == "positiv":
        karaktarer[index]["poang"] += 1
        svar = random.choice(positiva_svar)
    elif svar_typ == "neutral":
        karaktarer[index]["poang"] += 0
        svar = random.choice(neutrala_svar)
    else:  # negativ
        karaktarer[index]["poang"] -= 1
        svar = random.choice(negativa_svar)
    
    svar_label.config(text=svar)
    
    # Minska aktioner och uppdatera räknare
    aktioner_kvar -= 1
    uppdatera_aktioner_display()
    
    # Kontrollera om inga aktioner kvar
    if aktioner_kvar <= 0:
        if timer_id:
            root.after_cancel(timer_id)  # Avbryt timern
        root.after(1500, byt_dejt)  # Kort paus innan nästa dejt

def val3():
    global aktioner_kvar, timer_id
    # Slumpa typ av svar
    svar_typ = random.choice(["positiv", "neutral", "negativ"])
    
    if svar_typ == "positiv":
        karaktarer[index]["poang"] += 1
        svar = random.choice(positiva_svar)
    elif svar_typ == "neutral":
        karaktarer[index]["poang"] += 0
        svar = random.choice(neutrala_svar)
    else:  # negativ
        karaktarer[index]["poang"] -= 1
        svar = random.choice(negativa_svar)
    
    svar_label.config(text=svar)
    
    # Minska aktioner och uppdatera räknare
    aktioner_kvar -= 1
    uppdatera_aktioner_display()
    
    # Kontrollera om inga aktioner kvar
    if aktioner_kvar <= 0:
        if timer_id:
            root.after_cancel(timer_id)  # Avbryt timern
        root.after(1500, byt_dejt)  # Kort paus innan nästa dejt

# Funktion: Skippa dejt
def skippa_dejt():
    global timer_id
    if timer_id:
        root.after_cancel(timer_id)  # Avbryt timern
    svar_label.config(text="Du skippade dejten!")
    root.after(1000, byt_dejt)  # Kort paus innan nästa dejt

# Funktion: Uppdatera aktioner display
def uppdatera_aktioner_display():
    if aktioner_kvar > 0:
        aktioner_label.config(text=f"⏱️ Aktioner kvar: {aktioner_kvar}")
    else:
        aktioner_label.config(text="⏱️ Inga aktioner kvar - dejten är över!")

# Funktion: Visa valknappar
def visa_val():
    global val_frame
    val_frame = tk.Frame(root)
    val_frame.pack()

    tk.Button(val_frame, text="♥ Ge komplimang", command=val1).pack(pady=5)
    tk.Button(val_frame, text="☁ Fråga om väder", command=val2).pack(pady=5)
    tk.Button(val_frame, text="• Prata om dig själv", command=val3).pack(pady=5)
    
    # Skippa-knapp med röd färg för att sticka ut
    tk.Button(val_frame, text="» Skippa dejt", command=skippa_dejt, 
              bg="lightcoral", fg="white").pack(pady=10)

# Funktion: Starta dejt
def starta_dejt():
    global index, val_frame, timer_id, aktioner_kvar
    if val_frame:
        val_frame.destroy()
        svar_label.config(text="")

    if index < len(karaktarer):
        person = karaktarer[index]
        aktioner_kvar = 5  # Återställ aktioner för ny dejt (ändrat från 3 till 5)
        namn_label.config(text=f"Du dejtar {person['namn']}")
        visa_bild(person['bild'])  # Visa personens bild
        uppdatera_aktioner_display()  # Visa räknare
        visa_val()
        timer_id = root.after(8000, byt_dejt)  # 8 sekunder per dejt
    else:
        visa_resultat()

# Funktion: Byt till nästa dejt
def byt_dejt():
    global index, timer_id
    timer_id = None
    index += 1
    starta_dejt()

# Funktion: Visa resultat
def visa_resultat():
    global spel_nummer
    
    namn_label.config(text="Dejtingrundan är över!")
    bild_label.config(image="", text="🏆", font=("Helvetica", 30))
    aktioner_label.config(text="")  # Rensa aktioner räknare
    if val_frame:
        val_frame.destroy()

    # Beräkna totalpoäng
    total_poang = sum(person["poang"] for person in karaktarer)
    
    # Hitta bästa match
    bast = max(karaktarer, key=lambda p: p["poang"])
    
    # Skapa statistik text
    statistik_text = f"📊 SLUTRESULTAT - Spel #{spel_nummer}:\n\n"
    
    # Sortera karaktärer efter poäng (högst först)
    sorterade_karaktarer = sorted(karaktarer, key=lambda p: p["poang"], reverse=True)
    
    for i, person in enumerate(sorterade_karaktarer, 1):
        if person["poang"] > 0:
            emoji = "💖"
        elif person["poang"] == 0:
            emoji = "😐"
        else:
            emoji = "💔"
        
        statistik_text += f"{i}. {person['namn']}: {person['poang']} poäng {emoji}\n"
    
    statistik_text += f"\n🏆 Bästa match: {bast['namn']}!\n"
    statistik_text += f"📈 Totalpoäng: {total_poang}\n"
    statistik_text += "\n🔄 Tryck 'Spela igen' för ny runda!"
    
    svar_label.config(text=statistik_text, justify="left")
    
    # Lägg till "Spela igen" knapp
    spela_igen_frame = tk.Frame(root)
    spela_igen_frame.pack(pady=10)
    
    tk.Button(spela_igen_frame, text="🔄 Spela igen", command=starta_om_spel, 
              bg="lightgreen", fg="white", font=("Helvetica", 12)).pack()

# Funktion: Starta om spelet
def starta_om_spel():
    global index, spel_nummer
    
    # Återställ spelet
    index = 0
    spel_nummer += 1
    
    # Återställ alla poäng
    for person in karaktarer:
        person["poang"] = 0
    
    # Ta bort alla "Spela igen" knappar mer noggrant
    widgets_to_remove = []
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            # Kontrollera om framen innehåller en "Spela igen" knapp
            for child in widget.winfo_children():
                if isinstance(child, tk.Button) and "Spela igen" in child.cget("text"):
                    widgets_to_remove.append(widget)
                    break
    
    for widget in widgets_to_remove:
        widget.destroy()
    
    # Starta nytt spel
    starta_dejt()

# Starta första dejten
starta_dejt()

# Starta loopen
root.mainloop()