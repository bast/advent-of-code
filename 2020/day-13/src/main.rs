use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let (time, bus_order) = parse_input(&input);

    let waiting_times: Vec<i64> = bus_order
        .iter()
        .map(|&x| minutes_to_wait(time, x.0))
        .collect();

    // we take the waiting time - bus combination with minimal waiting time
    let result = waiting_times.iter().zip(&bus_order).min().unwrap();

    println!("result (part 1): {}", result.0 * (result.1).0);

    let perfect_time = find_timestamp(&bus_order);

    println!("timestamp (part 2): {}", perfect_time);
}

fn minutes_to_wait(time: i64, bus_number: i64) -> i64 {
    let multiple = bus_number * (time / bus_number);
    if multiple < time {
        return multiple + bus_number - time;
    }
    0
}

fn find_timestamp(bus_order: &[(i64, i64)]) -> i64 {
    // this is done using the Chinese remainder theorem
    // for a nice explanation, see https://www.dave4math.com/mathematics/chinese-remainder-theorem/
    // here using the same notation n_i, a_i, \bar{n}_i, u_i, and x

    let n = bus_order.iter().fold(1, |product, i| product * i.0);

    let mut x = 0;
    for &(bus, minute) in bus_order {
        // we add one to minutes to avoid a zero a_i
        // at the end we need to add one minute to the result
        let n_i_bar = n / bus;
        x += (minute + 1) * n_i_bar * solve_u(n_i_bar, bus);
    }

    n - (x % n) + 1
}

fn solve_u(n_i_bar: i64, n_i: i64) -> i64 {
    let mut k = 1;
    loop {
        if (n_i_bar * k % n_i) == 1 {
            break;
        }
        k += 1;
    }
    k
}

fn parse_input(input: &str) -> (i64, Vec<(i64, i64)>) {
    let lines: Vec<&str> = input.lines().collect();

    let time: i64 = lines[0].parse().unwrap();

    let mut bus_order = Vec::new();
    for (minute, bus) in lines[1].split(',').enumerate() {
        if bus != 'x'.to_string() {
            bus_order.push((bus.parse().unwrap(), minute as i64));
        }
    }

    (time, bus_order)
}
