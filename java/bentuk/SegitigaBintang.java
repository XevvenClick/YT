class SegitigaBintang {
  public static void main(String[] args) {
    int T = 6;
    for(int S=T-1, P=1; S>=0; S--, P+=2) {
      System.out.println( " ".repeat(S) + "*".repeat(P) );
    }
  }
}
