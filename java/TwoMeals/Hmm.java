// https://stackoverflow.com/a/19142321

public class Hmm {
    public static void main(String[] main) {
        K a = (K)(new M());
        a.p();
        L b = (L)(new N());
        b.q();
    }
    private static interface K {
        public void p();
    }
    private static class M {
        //public void p() { K o = new M(); }
        public void p() { K o = (K)(new M()); }
    }
    private static interface L {
        public void q();
    }
    private static class N {}
}
