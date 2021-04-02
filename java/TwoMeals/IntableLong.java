public class IntableLong {
    public static void main(String[] args) {
        check((long)Math.pow(2, 31));
        check((long)Math.pow(2, 31) - 1);
    }
    private static void check(long z) {
        System.out.printf("intable(%d) == %b%n", z, intable(z));
    }
    private static boolean intable(long z) {
        return (Integer.MIN_VALUE <= z) && (z <= Integer.MAX_VALUE);
    }
}
