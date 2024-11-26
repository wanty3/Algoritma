import random
from conquer import bubble_sort, insertion_sort, selection_sort

# Informasi Mahasiswa
NAMA = "Sri Aswanti"
NIM = "F551123075"
NIM_QUIZ = "F551123075"

# Set seed untuk reproducibility
random.seed(40)

# Generate 50 bilangan acak antara 0 dan 100
numbers = [random.randint(0, 100) for _ in range(50)]

# Best case input: bilangan sudah terurut
best_case = sorted(numbers)

# Perform sorting
bubble_sorted, bubble_time = bubble_sort(best_case.copy())
insertion_sorted, insertion_time = insertion_sort(best_case.copy())
selection_sorted, selection_time = selection_sort(best_case.copy())

# Tulis hasil analisis ke README pertama (NIM + Analisis)
with open("README_quiz.md", "w") as readme_quiz:
    readme_quiz.write(f"# Analisis Sorting untuk Quiz\n\n")
    readme_quiz.write(f"**NIM untuk Quiz:** {NIM_QUIZ}\n\n")
    readme_quiz.write("## Analisis Best Case\n\n")
    readme_quiz.write(f"**Input (Best Case):** {best_case}\n\n")
    readme_quiz.write("### Bubble Sort\n")
    readme_quiz.write(f"- Execution Time: {bubble_time:.8f} seconds\n\n")
    readme_quiz.write("### Insertion Sort\n")
    readme_quiz.write(f"- Execution Time: {insertion_time:.8f} seconds\n\n")
    readme_quiz.write("### Selection Sort\n")
    readme_quiz.write(f"- Execution Time: {selection_time:.8f} seconds\n\n")

# Tulis hasil analisis ke README utama (Nama + NIM)
with open("README.md", "w") as readme_main:
    readme_main.write(f"# Program Analisis Sorting\n\n")
    readme_main.write(f"**Nama:** {NAMA}\n")
    readme_main.write(f"**NIM:** {NIM}\n\n")
    readme_main.write("## Deskripsi Program\n")
    readme_main.write("Program ini melakukan analisis sorting (Bubble Sort, Insertion Sort, dan Selection Sort) "
                      "untuk best case menggunakan 50 bilangan acak antara 0 hingga 100.\n\n")
    readme_main.write("## Hasil Analisis\n\n")
    readme_main.write(f"**Input (Best Case):** {best_case}\n\n")
    readme_main.write("### Bubble Sort\n")
    readme_main.write(f"- Execution Time: {bubble_time:.8f} seconds\n\n")
    readme_main.write("### Insertion Sort\n")
    readme_main.write(f"- Execution Time: {insertion_time:.8f} seconds\n\n")
    readme_main.write("### Selection Sort\n")
    readme_main.write(f"- Execution Time: {selection_time:.8f} seconds\n\n")
