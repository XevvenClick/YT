/*
    =====================
      TOKO ABC
    =====================
    Voucher : diskon 40% s/d 20.000 minimum pembelian 40.000
*/
import java.util.Scanner;
public class VoucherPembelian {
    public static void main(String[] args) {
        System.out.println("=====================\n" +
"   TOKO ABC\n" +
"=====================");
        Scanner scn = new Scanner(System.in);
        
        // Voucher : diskon 40% s/d 20.000 minimum pembelian 40.000
        int[] voucher = {40, 20000, 40000};

        System.out.print("Harga Barang : ");
        long harga = scn.nextLong();
        
        System.out.print("Jumlah Pesan : ");
        int jumlah = scn.nextInt();
        long total_beli = harga * jumlah;
        System.out.println("=====================");
        System.out.println("Total Pembelian : " + total_beli);

        long diskon = 0;
        if(total_beli >= voucher[2]) {
          diskon = total_beli * voucher[0] / 100;
          if(diskon > voucher[1]) {
            diskon = voucher[1];
          }
          total_beli -= diskon;
          System.out.println("Total Diskon : " + diskon);
        }
        System.out.println("TOTAL ( " + total_beli + " )");
        System.out.println("=====================");
        
        System.out.print("Jumlah Bayar : ");
        long bayar = scn.nextLong();
        long kembali = bayar - total_beli;
        System.out.println("Jumlah Kembalian : " + kembali);
    }
}
