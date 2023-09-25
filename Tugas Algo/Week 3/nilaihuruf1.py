def nilaiHuruf (nilai):
    nilai = float(nilai)
    if nilai >= 85 and nilai <= 100:
        return "A"
    elif nilai >= 80 and nilai <= 84.99:
        return "A-"
    elif nilai >= 75 and nilai <= 79.99:
        return "B+"
    elif nilai >= 70 and nilai <= 74.99:
        return "B"
    elif nilai >= 65 and nilai <= 69.99:
        return "B-"
    elif nilai >= 60 and nilai <= 64.99:
        return "C+"
    elif nilai >= 50 and nilai <= 59.99:
        return "C"
    elif nilai >= 40 and nilai <= 49.99:
        return "D"
    elif nilai >= 0 and nilai <= 39.99:
        return "E"


print (nilaiHuruf(input()))