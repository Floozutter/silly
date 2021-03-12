public class OneHourIsThree {
    public static void main(String[] args) {
        System.out.printf(
            "You will have to wait %d hours.%n",
            rayanHours(1)
        );
    }
    private static int rayanHours(int normalHours) {
        return 3 * normalHours;
    }
}
