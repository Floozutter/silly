public class LGH {
    interface L2 {
        void m();
    }
    interface L1 {
        public void m();
        public void q();
    }
    class G implements L1 {
        public void m() {}
        public void q() {}
    }
    class H extends G implements L2, L1 {
        public void q() {}
    }
}
