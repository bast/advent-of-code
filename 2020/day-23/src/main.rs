fn main() {
    let mut cups = vec![9, 2, 5, 1, 7, 6, 8, 3, 4];

    let connections = game(&cups, *cups.last().unwrap(), 100);

    let mut result = Vec::new();
    let mut current = 1;
    for _ in 0..8 {
        current = connections[current];
        result.push(current);
    }

    println!("result from part 1: {:?}", result);

    let num_cups = cups.len();
    for i in (num_cups + 1)..=1_000_000 {
        cups.push(i);
    }

    let connections = game(&cups, *cups.last().unwrap(), 10_000_000);
    let a = connections[1];
    let b = connections[a];

    println!("result from part 2: {:?}", a * b);
}

// one way to look at this problem is using positions
// possibly many numbers change places
//     (3) 8  9  1  2  5  4  6  7
//      3 (2) 8  9  1  5  4  6  7
//      3  2 (5) 4  6  7  8  9  1
//      7  2  5 (8) 9  1  3  4  6
//      3  2  5  8 (4) 6  7  9  1
//      9  2  5  8  4 (1) 3  6  7
//      7  2  5  8  4  1 (9) 3  6
//      8  3  6  7  4  1  9 (2) 5
//      7  4  1  5  8  3  9  2 (6)
//     (5) 7  4  1  8  3  9  2  6
//      5 (8) 3  7  4  1  9  2  6

// better way is in terms of connectivity (linked list)
// only 3 numbers are changing position each round
// independently of the number of cups
//
//      1  2  3  4  5  6  7  8  9    destination    moves (a->b b->c c->a)
//      -------------------------------------------------
//      2  5  8  6  4  7 (3) 9  1    2              1->3 3->2 2->1
//      5  8 (2) 6  4  7  3  9  1    7              1->2 2->7 7->1
//      3 (5) 2  6  4  7  8  9  1    3              7->5 5->3 3->7
//      3  5  4  6 (8) 7  2  9  1    7              3->8 8->7 7->3
//      3  5  2  6  8  7  9 (4) 1    3              9->4 4->3 3->9
//      3  5  6 (1) 8  7  9  4  2    9              7->1 1->9 9->7
//     (9) 5  6  1  8  7  2  4  3    8              7->9 9->8 8->7
//      9  5  6  1  8  7  4  3 (2)   1              3->2 2->1 1->3
//      5 (6) 9  1  8  7  4  3  2    5              1->6 6->5 5->1
//      8  6  9  1  7 (5) 4  3  2    3              1->5 5->3 3->1
//      9  6  7  1 (8) 5  4  3  2
fn game(cups: &[usize], starting_neighbor: usize, num_rounds: usize) -> Vec<usize> {
    let num_cups = cups.len();
    let mut connections = position_to_connection(&cups);
    let mut current = starting_neighbor;

    for _ in 0..num_rounds {
        let b = connections[current];
        current = b;

        let mut picked_up = Vec::new();
        picked_up.push(connections[b]);
        picked_up.push(connections[picked_up[0]]);
        picked_up.push(connections[picked_up[1]]);

        let a = connections[picked_up[1]];
        let c = find_destination(num_cups, b, &picked_up);

        // moves: a->b b->c c->a
        let tc = connections[c];
        connections[c] = connections[b];
        connections[b] = connections[a];
        connections[a] = tc;
    }

    connections
}

fn find_destination(num_cups: usize, current_cup: usize, picked_up: &[usize]) -> usize {
    let mut destination = current_cup - 1;

    loop {
        if destination == 0 {
            destination = num_cups;
        }
        if !picked_up.contains(&destination) {
            break;
        }
        destination -= 1;
    }

    destination
}

fn position_to_connection(cups: &[usize]) -> Vec<usize> {
    // adding zero in front to be able to index without subtracting 1 every time
    let mut connections = vec![0; cups.len() + 1];

    for pair in cups.windows(2) {
        connections[pair[0]] = pair[1];
    }
    connections[cups[cups.len() - 1]] = cups[0];

    connections
}
