public class Woo {
    public static void main(String[] args) {
        Object r = new W<Object>();
        ((W)r).set(2.0, "CFCU");
        // r
        System.out.println("r:");
        System.out.println(r instanceof Object);
        System.out.println(r instanceof W);
        //System.out.println(r instanceof W<Object>);
        //System.out.println(r instanceof W<double>);
        System.out.println(r.getClass());
        // r.get()
        System.out.println("r.get():");
        System.out.println(((W)r).get() instanceof Object);
        System.out.println(((W)r).get() instanceof Double);
        System.out.println(((W)r).get().getClass());
    }
    private static class W<T> {
        private T val;
        private String bank;
        public void set(T v, String b) { val = v; bank = b; }
        public T get() { return val; }
    }
}
