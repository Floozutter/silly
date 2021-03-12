public class Dread {
    public static void main(String[] args) {
        Derived d = new Derived();
        d.foo();
    }
    private static class Base {
        public String toString() {
            return "uwu";
        }
        public void printMe() {
            System.out.println("base: " + toString());
        }
    }
    private static class Derived extends Base {
        public String toString() {
            return "owo";
        }
        public void printMe() {
            System.out.println("berived: " + toString());
        }
        public void foo() {
            super.printMe();
        }
    }
}
