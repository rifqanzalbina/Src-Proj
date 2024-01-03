# Program Tcl sederhana untuk penjumlahan dan perkalian

# Fungsi untuk meminta input dari pengguna
proc getInput {prompt} {
    puts -nonewline "$prompt: "
    flush stdout
    gets stdin
}

# Meminta pengguna untuk memasukkan dua angka
set num1 [getInput "Masukkan angka Pertama"]
set num2 [getInput "Masukkan angka Kedua"]
set num3 [getInput "Masukkan angak Ketiga"]
set num4 [getInput "Masukkan angka Keeempat"]

# Konversi input ke dalam bentuk angka
set num1 [expr $num1]
set num2 [expr $num2]
set num3 [expr $num3]
set num4 [expr $num4]

# Melakukan penjumlahan dan perkalian
set hasilPenjumlahan [expr $num1 + $num2 + $num3 + $num4]
set hasilPerkalian [expr $num1 * $num2 * $num3 * $num4]
set hasilPembagian [expr $num1 + $num2 - $num3 * $num4]
set hasilKeempat [expr $num1 + $num2 * $num4 - $num1]
# Menampilkan hasil
puts "Hasil penjumlahan: $hasilPenjumlahan"
puts "Hasil perkalian: $hasilPerkalian"
puts "Hasil pembagian: $hasilPembagian"
