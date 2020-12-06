fn look_and_say(input: String) -> String {
    let digits_previous: Vec<char> = input.chars().collect();

    let mut result = String::from("");

    let mut current_digit = digits_previous[0];
    let mut how_often = 1;

    for (a, b) in digits_previous.iter().zip(&digits_previous[1..]) {
        if a == b {
            how_often += 1;
        } else {
            result.push(how_often.to_string().parse().unwrap());
            result.push(current_digit.to_string().parse().unwrap());
            current_digit = *b;
            how_often = 1;
        }
    }
    result.push(how_often.to_string().parse().unwrap());
    result.push(current_digit.to_string().parse().unwrap());

    result
}

fn apply(input: &str, how_often: usize) -> String {
    let mut s = input.to_string();

    for _ in 0..how_often {
        s = look_and_say(s.clone());
    }

    s
}

fn main() {
    println!(
        "length of the result (part 1): {}",
        apply("1321131112", 40).len()
    );
    println!(
        "length of the result (part 2): {}",
        apply("1321131112", 50).len()
    );
}
