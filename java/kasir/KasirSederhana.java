/*
    =====================
    == KASIR SEDERHANA ==
    =====================
    Input Harga Barang
    Input Jumlah Barang
    Output Total Belanja
    Input Jumlah Bayar
    Output Kembalian
*/
import java.util.Scanner;
public class KasirSederhana {
    public static void main(String[] args) {
        System.out.println("=====================\n" +
"== KASIR SEDERHANA ==\n" +
"=====================");
        Scanner scn = new Scanner(System.in);
        System.out.print("Masukan Harga Barang : ");
        long harga = scn.nextLong();
        
        System.out.print("Masukan Jumlah Barang : ");
        int jumlah = scn.nextInt();
        long total = harga * jumlah;
        System.out.println("Total Belanja : " + total);
        
        System.out.print("Masukan Jumlah Bayar :");
        long bayar = scn.nextLong();
        long kembali = bayar - total;
        System.out.println("Total Kembalian : " + kembali);
    }
}
