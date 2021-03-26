public class NoZeros {
    public static void main(String[] args) {
        check(-50);
        check(0);
        check(603);
        check(5);
        check(-34);
    }
    public static boolean bn0(int n) {
        if (-10 < n && n < 10) {
            return n != 0;
        } else {
            return bn0(n % 10) && bn0(n / 10);
        }
    }
    public static void check(int n) {
        System.out.printf("bn0(%d) == %b%n", n, bn0(n));
    }
}
