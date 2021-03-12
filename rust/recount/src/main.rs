fn naive(string: &str, old: &str, new: &str) -> (String, usize) {
    (string.replace(old, new), string.matches(old).count())
}

// thank you, KerfuffleV2!
// https://www.reddit.com/r/rust/comments/m39ybn//gqnsqym/
fn adapted(string: &str, old: &str, new: &str) -> (String, usize) {
    let mut result = String::new();
    let mut last_end = 0;
    let mut count = 0;
    for (start, part) in string.match_indices(old) {
        result.push_str(string.get(last_end..start).unwrap());
        result.push_str(new);
        last_end = start + part.len();
        count = count + 1;
    }
    result.push_str(string.get(last_end..string.len()).unwrap());
    (result, count)
}

fn main() {
    const STRING: &str = "beet";
    const OLD: &str = "e";
    const NEW: &str = "o";
    println!("{:?}", naive(STRING, OLD, NEW));
    println!("{:?}", adapted(STRING, OLD, NEW));
}
