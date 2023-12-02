use std::collections::HashMap;

fn main() {
    let input = std::fs::read_to_string("../input-2.txt").unwrap();
    let lines = input.lines();

    let limits: HashMap<&str, i32> = [("red", 12), ("green", 13), ("blue", 14)]
        .iter()
        .cloned()
        .collect();

    let mut score_part1 = 0;
    let mut score_part2 = 0;

    for line in lines {
        let (game_number, draw_parts) = parse_game(line);

        let mut game_valid = true;
        let mut min_required = std::collections::HashMap::new();
        let mut game_score: i32 = 1;

        for draw in draw_parts {
            let counts = get_counts(draw);
            // Part 1
            for (color, count) in &counts {
                let limit = limits.get(color).unwrap();

                if count > limit {
                    game_valid = false;
                    break;
                }
            }

            // Part 2
            for (color, count) in &counts {
                let current_min = min_required.entry(*color).or_insert(0);

                if count > current_min {
                    *current_min = *count;
                }
            }
        }

        // Part 1
        if game_valid {
            score_part1 += game_number;
        }

        // Part 2
        for (_, &count) in &min_required {
            game_score *= count;
        }

        score_part2 += game_score;
    }

    println!("Part 1: {}", score_part1);
    println!("Part 2: {}", score_part2);
}

// Parse a line into a game number and a vector of draws
fn parse_game(line: &str) -> (i32, Vec<&str>) {
    let mut parts = line.split(": ");

    let game_number = parts
        .next()
        .unwrap()
        .split(" ")
        .nth(1)
        .unwrap()
        .parse::<i32>()
        .unwrap();

    let draws = parts.next().unwrap();

    let draw_parts = draws.split("; ");

    (game_number, draw_parts.collect())
}

// Get the counts from a draw
fn get_counts(draw: &str) -> std::collections::HashMap<&str, i32> {
    let mut counts = std::collections::HashMap::new();

    let color_parts = draw.split(", ");

    for color_part in color_parts {
        let mut color_count_parts = color_part.split(" ");
        let count = color_count_parts.next().unwrap().parse::<i32>().unwrap();
        let color = color_count_parts.next().unwrap();

        counts.insert(color, count);
    }

    counts
}
