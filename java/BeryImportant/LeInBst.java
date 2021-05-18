public class LeInBst {
    public static void main(String[] args) {
        BST head = new BST(
            8,
            new BST(
                3,
                new BST(1, null, null),
                new BST(
                    6,
                    new BST(4, null, null),
                    new BST(7, null, null)
                )
            ),
            new BST(
                10,
                null,
                new BST(
                    14,
                    new BST(13, null, null),
                    null
                )
            )
        );
        System.out.println(BST.numLE(head, 13));
    }
    public static class BST {
        public int val;
        public BST left, right;
        public BST(int val, BST left, BST right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
        public static int numLE(BST t, int v) {
            if (t != null) {
                if (t.val > v) {
                    return numLE(t.left, v);
                } else {
                    return 1 + numLE(t.left, v) + numLE(t.right, v);
                }
            } else {
                return 0;
            }
        }
    }
}
