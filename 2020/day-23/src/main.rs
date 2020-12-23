fn main() {
    let mut cups = vec![9, 2, 5, 1, 7, 6, 8, 3, 4];

    for i in 0..100 {
        let current_index = i % cups.len();
        cups = round(cups, current_index);
    }

    println!("result from part 1: {:?}", cups);
}

fn round(cups: Vec<i32>, current_index: usize) -> Vec<i32> {
    let current_cup = cups[current_index];

    let mut it = cups.iter().cycle();

    // find current cup
    let mut i = 0;
    while i % cups.len() != current_index {
        let _ = it.next().unwrap();
        i += 1;
    }

    let mut keep: Vec<i32> = Vec::new();
    keep.push(*it.next().unwrap());

    // pick up 3 cups after
    let mut pick_up = Vec::new();
    pick_up.push(*it.next().unwrap());
    pick_up.push(*it.next().unwrap());
    pick_up.push(*it.next().unwrap());

    // collect the remaining cups
    while (keep.len() + pick_up.len()) < cups.len() {
        keep.push(*it.next().unwrap());
    }

    let destination = find_destination(&keep, current_cup);

    let mut cups_reordered = Vec::new();
    for cup in keep {
        cups_reordered.push(cup);
        if cup == destination {
            cups_reordered.extend(pick_up.clone());
        }
    }

    // finally make sure that current cup remains at current index
    let mut cups_new = vec![0; cups.len()];
    let offset = cups.iter().position(|&c| c == current_cup).unwrap();
    for (i, cup) in cups_reordered.iter().enumerate() {
        // cups_new.push(cups_reordered[(i - offset + cups.len()) % cups.len()]);
        cups_new[(i + offset) % cups.len()] = *cup;
    }

    cups_new
}

fn find_destination(cups: &[i32], current_cup: i32) -> i32 {
    for i in (1..current_cup).rev() {
        if cups.contains(&i) {
            return i;
        }
    }
    *cups.iter().max().unwrap()
}
