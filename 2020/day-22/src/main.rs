use std::collections::VecDeque;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();

    let mut cards = read_cards(&input);

    println!("result from part 1: {}", game(&mut cards));
}

fn game(cards: &mut [VecDeque<usize>]) -> usize {
    loop {
        if cards[0].is_empty() || cards[1].is_empty() {
            break;
        }
        let card1 = cards[0].pop_front().unwrap();
        let card2 = cards[1].pop_front().unwrap();
        if card1 > card2 {
            cards[0].push_back(card1);
            cards[0].push_back(card2);
        } else {
            cards[1].push_back(card2);
            cards[1].push_back(card1);
        }
    }

    score(&cards[0]) + score(&cards[1])
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
