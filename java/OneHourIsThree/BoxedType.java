public class BoxedType {
    public static void main(String[] args) {
        Box<Object> b = new Box<>();
        b.put(5 + 2);
        System.out.println(b.get() instanceof Object);
        System.out.println(b.get() instanceof Integer);
        System.out.println(b.get().getClass());
    }
    private static class Box<T> {
        private T value;
        public void put(T x) { value = x; }
        public T get() { return value; }
    }
}
