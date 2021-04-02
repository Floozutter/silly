public class NumGTest {
    public static void main(String[] args) {
        check(6, 3);
        check(6, 14);
        check(753, -4);
        check(55535, 3);
        check(652757, 4);
    }
    public static void check(int n, int d) {
        System.out.printf("numG(%d, %d) == %d%n", n, d, numG(n, d));
    }
    private static int numG(int n, int d) {
        if (n != 0 && n % 10 > d) {
            return 1 + numG(n / 10, d);
        } else {
            return 0;
        }
    }
}
