use regex::Regex;
use std::collections::HashSet;
use std::fs;

fn chop_input(input: &str) -> Vec<&str> {
    // passports are separated by one empty line
    let passports: Vec<&str> = input.split("\n\n").collect();
    passports
}

fn passport_is_valid1(text: &str) -> bool {
    let required_keys: HashSet<_> = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        .iter()
        .cloned()
        .collect();

    let mut keys = HashSet::new();
    for entry in text.split_whitespace() {
        let chunks: Vec<&str> = entry.split(':').collect();
        keys.insert(chunks[0]);
    }

    // compute difference between the two sets
    let diff: Vec<_> = required_keys.difference(&keys).cloned().collect();

    // if the difference is empty, then all required entries are there
    diff.is_empty()
}

#[test]
fn test_policy1() {
    let input = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in";

    let passports = chop_input(&input);
    let valid_passports = passports.iter().filter(|x| passport_is_valid1(x));
    assert_eq!(valid_passports.count(), 2);
}

fn is_year_in_range(regex: &str, text: &str, min: usize, max: usize) -> bool {
    let re = Regex::new(regex).unwrap();
    if re.is_match(text) {
        let caps = re.captures(text).unwrap();
        let year: usize = caps.get(1).unwrap().as_str().parse().unwrap();
        return min <= year && year <= max;
    }
    false
}

// byr (Birth Year) - four digits; at least 1920 and at most 2002.
fn byr_valid(text: &str) -> bool {
    is_year_in_range(r"byr:([0-9]{4})(\s+|$)", &text, 1920, 2002)
}

// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
fn iyr_valid(text: &str) -> bool {
    is_year_in_range(r"iyr:([0-9]{4})(\s+|$)", &text, 2010, 2020)
}

// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
fn eyr_valid(text: &str) -> bool {
    is_year_in_range(r"eyr:([0-9]{4})(\s+|$)", &text, 2020, 2030)
}

// hgt (Height) - a number followed by either cm or in:
// If cm, the number must be at least 150 and at most 193.
// If in, the number must be at least 59 and at most 76.
fn hgt_valid(text: &str) -> bool {
    let re = Regex::new(r"hgt:(\d+)(cm|in)(\s+|$)").unwrap();
    if re.is_match(text) {
        let caps = re.captures(text).unwrap();
        let height: usize = caps.get(1).unwrap().as_str().parse().unwrap();
        let unit: String = caps.get(2).unwrap().as_str().parse().unwrap();
        match unit.as_str() {
            "cm" => return 150 <= height && height <= 193,
            "in" => return 59 <= height && height <= 76,
            _ => return false,
        }
    }
    false
}

// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
fn hcl_valid(text: &str) -> bool {
    Regex::new(r"hcl:\#[0-9a-f]{6}(\s+|$)")
        .unwrap()
        .is_match(text)
}

// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
fn ecl_valid(text: &str) -> bool {
    Regex::new(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s+|$)")
        .unwrap()
        .is_match(text)
}

// pid (Passport ID) - a nine-digit number, including leading zeroes.
fn pid_valid(text: &str) -> bool {
    Regex::new(r"pid:[0-9]{9}(\s+|$)").unwrap().is_match(text)
}

fn passport_is_valid2(text: &str) -> bool {
    passport_is_valid1(&text)
        && byr_valid(&text)
        && iyr_valid(&text)
        && eyr_valid(&text)
        && hgt_valid(&text)
        && hcl_valid(&text)
        && ecl_valid(&text)
        && pid_valid(&text)
}

#[test]
fn test_policy2() {
    let input = "eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007";

    let passports = chop_input(&input);
    let valid_passports = passports.iter().filter(|x| passport_is_valid2(x));
    assert_eq!(valid_passports.count(), 0);

    let input = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719";

    let passports = chop_input(&input);
    let valid_passports = passports.iter().filter(|x| passport_is_valid2(x));
    assert_eq!(valid_passports.count(), 4);
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let passports = chop_input(&input);

    println!(
        "number of valid passports in part 1: {}",
        passports.iter().filter(|x| passport_is_valid1(x)).count()
    );

    println!(
        "number of valid passports in part 2: {}",
        passports.iter().filter(|x| passport_is_valid2(x)).count()
    );
}
