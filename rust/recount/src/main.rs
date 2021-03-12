fn naive(string: &str, old: &str, new: &str) -> (String, usize) {
    (string.replace(old, new), string.matches(old).count())
}

fn main() {
    const STRING: &str = "beet";
    const OLD: &str = "e";
    const NEW: &str = "o";
    println!("{:?}", naive(STRING, OLD, NEW));
}
