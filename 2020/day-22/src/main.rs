use std::collections::VecDeque;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let (mut cards_player1, mut cards_player2) = read_cards(&input);

    loop {
        if cards_player1.is_empty() || cards_player2.is_empty() {
            break;
        }
        let card1 = cards_player1.pop_front().unwrap();
        let card2 = cards_player2.pop_front().unwrap();
        if card1 > card2 {
            cards_player1.push_back(card1);
            cards_player1.push_back(card2);
        } else {
            cards_player2.push_back(card2);
            cards_player2.push_back(card1);
        }
    }

    println!(
        "result from part 1: {}",
        score(&cards_player1) + score(&cards_player2)
    );
}

fn score(cards: &VecDeque<usize>) -> usize {
    let mut s = 0;
    for (i, card) in cards.iter().rev().enumerate() {
        s += (i + 1) * card;
    }
    s
}

fn read_cards(input: &str) -> (VecDeque<usize>, VecDeque<usize>) {
    let chunks: Vec<&str> = input.split("\n\n").collect();

    let mut cards_player1 = VecDeque::new();
    for line in chunks[0].lines().skip(1) {
        cards_player1.push_back(line.parse().unwrap());
    }

    let mut cards_player2 = VecDeque::new();
    for line in chunks[1].lines().skip(1) {
        cards_player2.push_back(line.parse().unwrap());
    }

    (cards_player1, cards_player2)
}
