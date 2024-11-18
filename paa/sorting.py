import time

# Fungsi Quick Sort dengan penghitung operasi
def quick_sort(arr, operasi=None):
    if operasi is None:
        operasi = {'perbandingan': 0, 'pertukaran': 0}
    if len(arr) <= 1:
        return arr, operasi
    
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    
    for x in arr:
        operasi['perbandingan'] += 2  # Perbandingan dengan pivot
        if x < pivot:
            left.append(x)
            operasi['pertukaran'] += 1
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
            operasi['pertukaran'] += 1
    
    left, operasi = quick_sort(left, operasi)
    right, operasi = quick_sort(right, operasi)
    return left + middle + right, operasi

# Fungsi Bubble Sort dengan penghitung operasi
def bubble_sort(arr):
    operasi = {'perbandingan': 0, 'pertukaran': 0}
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n-i-1):
            operasi['perbandingan'] += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                operasi['pertukaran'] += 1
    return arr, operasi

# Array sesuai gambar
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # Array terurut terbalik
B = [0, 1, 2, 3, 4, 5, 8, 7, 6, 5]  # Array sebagian terurut

def analisis_algoritma(nama_array, arr):
    print(f"\nAnalisis Array {nama_array}: {arr}")
    print("="*50)
    
    # Analisis Bubble Sort
    start_time = time.time()
    hasil_bubble, operasi_bubble = bubble_sort(arr[:])
    waktu_bubble = time.time() - start_time
    
    print("\nBubble Sort:")
    print(f"Hasil          : {hasil_bubble}")
    print(f"Waktu          : {waktu_bubble:.10f} detik")
    print(f"Perbandingan   : {operasi_bubble['perbandingan']}")
    print(f"Pertukaran     : {operasi_bubble['pertukaran']}")
    
    # Analisis Quick Sort
    start_time = time.time()
    hasil_quick, operasi_quick = quick_sort(arr[:])
    waktu_quick = time.time() - start_time
    
    print("\nQuick Sort:")
    print(f"Hasil          : {hasil_quick}")
    print(f"Waktu          : {waktu_quick:.10f} detik")
    print(f"Perbandingan   : {operasi_quick['perbandingan']}")
    print(f"Pertukaran     : {operasi_quick['pertukaran']}")
    
    # Analisis Efisiensi
    print("\nAnalisis Efisiensi:")
    print("-" * 30)
    
    if waktu_quick < waktu_bubble:
        efisiensi_waktu = "Quick Sort"
        persen_lebih_cepat = ((waktu_bubble - waktu_quick) / waktu_bubble) * 100
    else:
        efisiensi_waktu = "Bubble Sort"
        persen_lebih_cepat = ((waktu_quick - waktu_bubble) / waktu_quick) * 100
    
    if operasi_quick['perbandingan'] + operasi_quick['pertukaran'] < operasi_bubble['perbandingan'] + operasi_bubble['pertukaran']:
        efisiensi_operasi = "Quick Sort"
    else:
        efisiensi_operasi = "Bubble Sort"
    
    print(f"Algoritma lebih cepat: {efisiensi_waktu} (lebih cepat {persen_lebih_cepat:.2f}%)")
    print(f"Algoritma lebih efisien dalam operasi: {efisiensi_operasi}")
    
    return efisiensi_waktu, efisiensi_operasi

# Analisis kedua array
print("\nANALISIS EFISIENSI ALGORITMA PENGURUTAN")
print("="*50)

efisiensi_A = analisis_algoritma("A", A)
efisiensi_B = analisis_algoritma("B", B)

# Kesimpulan
print("\nKESIMPULAN AKHIR")
print("="*50)
print(f"\nUntuk Array A (terurut terbalik):")
print(f"- Algoritma lebih efisien berdasarkan waktu: {efisiensi_A[0]}")
print(f"- Algoritma lebih efisien berdasarkan operasi: {efisiensi_A[1]}")

print(f"\nUntuk Array B (sebagian terurut):")
print(f"- Algoritma lebih efisien berdasarkan waktu: {efisiensi_B[0]}")
print(f"- Algoritma lebih efisien berdasarkan operasi: {efisiensi_B[1]}")

print("\nAnalisis:")
print("1. Untuk Array A (terurut terbalik):")
print("   - Quick Sort lebih efisien karena membagi array menjadi bagian-bagian")
print("   - Bubble Sort kurang efisien karena harus melakukan banyak pertukaran")

print("\n2. Untuk Array B (sebagian terurut):")
print("   - Quick Sort tetap lebih efisien dalam kebanyakan kasus")
print("   - Bubble Sort menunjukkan performa lebih baik dibanding kasus A")
print("   - Perbedaan efisiensi tidak terlalu signifikan karena array sudah sebagian terurut")