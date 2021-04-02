public class Hmm {
    private static interface K {
        public void p();
    }
    private static class M {
        //public void p() { K o = new M(); }
        public void p() { K o = (K)(new M()); }
    }
}
