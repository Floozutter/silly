public class NumTest {
    public static void main(String[] args) {
        check(6, 3);
        check(753, 2);
        check(6, 6);
        check(33353, 3);
        check(645222, 2);
        check(0, 0);
        check(10, 0);
        check(100, 0);
    }
    public static void check(int n, int d) {
        System.out.printf("num(%d, %d) == %d%n", n, d, num(n, d));
    }
    private static int num(int n, int d) {
        if (n != 0 && n % 10 == d) {
            return 1 + num(n / 10, d);
        } else {
            return 0;
        }
    }
}
