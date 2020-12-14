use regex::Regex;
use std::collections::HashMap;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    println!("result part 1: {}", decoder(&input, 1));
    println!("result part 2: {}", decoder(&input, 2));
}

fn decoder(input: &str, version: i32) -> isize {
    let mut map: HashMap<isize, isize> = HashMap::new();

    let mut mask = "";
    for line in input.lines() {
        match line.get(..3) {
            Some("mas") => {
                let words: Vec<&str> = line.split_whitespace().collect();
                mask = words[2];
            }
            Some("mem") => {
                let (address, value) = parse_mem(&line);
                if version == 1 {
                    let s = apply_mask(value, &mask, 'X');
                    let b = isize::from_str_radix(&s, 2).unwrap();
                    map.insert(address, b);
                }
                if version == 2 {
                    let s = apply_mask(address, &mask, '0');
                    for a in string_explosion(s)
                        .iter()
                        .map(|x| isize::from_str_radix(&x, 2).unwrap())
                    {
                        map.insert(a, value);
                    }
                }
            }
            _ => (),
        };
    }

    let mut sum = 0;
    for key in map.keys() {
        sum += map.get(key).unwrap();
    }

    sum
}

fn apply_mask(value: isize, mask: &str, ignore_char: char) -> String {
    let value_binary_string = format!("{:036b}", value);
    let mut value_binary_characters: Vec<char> = value_binary_string.chars().collect();

    for (i, mask_char) in mask.chars().enumerate() {
        if mask_char != ignore_char {
            value_binary_characters[i] = mask_char;
        }
    }

    value_binary_characters.iter().collect()
}

fn string_explosion(input: String) -> Vec<String> {
    let mut strings = Vec::new();

    if input.contains('X') {
        strings.extend(string_explosion(input.replacen("X", "0", 1)));
        strings.extend(string_explosion(input.replacen("X", "1", 1)));
    } else {
        strings.push(input);
    }

    strings
}

fn parse_mem(input: &str) -> (isize, isize) {
    let re = Regex::new(r"^mem\[(\d+)\] = (\d+)$").unwrap();
    let caps = re.captures(input).unwrap();

    let address = caps.get(1).unwrap().as_str().parse().unwrap();
    let value = caps.get(2).unwrap().as_str().parse().unwrap();

    (address, value)
}
