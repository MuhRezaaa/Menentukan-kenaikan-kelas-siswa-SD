# Menentukan-kenaikan-kelas-siswa-SD
2409076017_Muhammad Reza Aulia

# Input nilai UN siswa dan kehadiran
nilai_ujian = float(input("Masukkan nilai ujian: "))
persentase_kehadiran = float(input("Masukkan persentase kehadiran: "))

# Menentukan persyaratan naik kelas
if nilai_ujian > 60 and persentase_kehadiran > 75:
    print("Siswa LULUS.")
    
    # Menentukan predikat berdasarkan nilai
    if nilai_ujian > 90:
        print("Predikat: A")
    elif 80 <= nilai_ujian <= 89:
        print("Predikat: B")
    elif 75 <= nilai_ujian <= 79:
        print("Predikat: C")
else:
    print("Siswa TIDAK LULUS karena tidak memenuhi syarat.")
