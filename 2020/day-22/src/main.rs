use std::collections::{HashSet, VecDeque};
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let decks = read_cards(&input);

    println!(
        "result from part 1: {:#?}",
        game(&decks[0], &decks[1], false)
    );
    println!(
        "result from part 2: {:#?}",
        game(&decks[0], &decks[1], true)
    );
}

fn game(
    deck1_input: &VecDeque<usize>,
    deck2_input: &VecDeque<usize>,
    recursive_game: bool,
) -> (usize, usize) {
    let mut deck1: VecDeque<usize> = deck1_input.clone();
    let mut deck2: VecDeque<usize> = deck2_input.clone();

    let mut history1: HashSet<VecDeque<usize>> = HashSet::new();
    let mut history2: HashSet<VecDeque<usize>> = HashSet::new();

    'outer: loop {
        if deck1.is_empty() || deck2.is_empty() {
            break 'outer;
        }
        if history1.contains(&deck1) || history2.contains(&deck2) {
            return (score(&deck1), 0);
        }

        history1.insert(deck1.clone());
        history2.insert(deck2.clone());

        let card1 = deck1.pop_front().unwrap();
        let card2 = deck2.pop_front().unwrap();

        let player1_wins: bool;

        if recursive_game && deck1.len() >= card1 && deck2.len() >= card2 {
            let mut subdeck1 = deck1.clone();
            subdeck1.truncate(card1);
            let mut subdeck2 = deck2.clone();
            subdeck2.truncate(card2);

            let (score1, score2) = game(&subdeck1, &subdeck2, recursive_game);

            player1_wins = score1 > score2;
        } else {
            player1_wins = card1 > card2;
        }

        if player1_wins {
            deck1.push_back(card1);
            deck1.push_back(card2);
        } else {
            deck2.push_back(card2);
            deck2.push_back(card1);
        }
    }

    (score(&deck1), score(&deck2))
}

fn score(deck: &VecDeque<usize>) -> usize {
    let mut s = 0;
    for (i, card) in deck.iter().rev().enumerate() {
        s += (i + 1) * card;
    }
    s
}

fn read_cards(input: &str) -> Vec<VecDeque<usize>> {
    let mut cards = Vec::new();
    let chunks: Vec<&str> = input.split("\n\n").collect();
    for chunk in chunks {
        let mut q = VecDeque::new();
        for line in chunk.lines().skip(1) {
            q.push_back(line.parse().unwrap());
        }
        cards.push(q);
    }
    cards
}
