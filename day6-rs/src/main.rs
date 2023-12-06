fn main() {
    let input = std::fs::read_to_string("../input-6.txt").unwrap();

    // part 1
    let mut lines = input.lines().map(|line| {
        line.split_once(':')
            .unwrap()
            .1
            .trim()
            .split_whitespace()
            .filter_map(|num| num.parse().ok())
            .collect::<Vec<i32>>()
    });

    let times = lines.next().unwrap();
    let distances = lines.next().unwrap();

    let mut all_ways = Vec::new();

    for (t, d) in times.iter().zip(distances.iter()) {
        let ways = (1..*t).filter(|x| x * (*t - x) > *d).count() as i64;
        all_ways.push(ways);
    }

    println!("{}", all_ways.iter().product::<i64>());

    // part 2
    let lines: Vec<i64> = input
        .lines()
        .map(|line| line.split_whitespace().skip(1).collect::<String>())
        .map(|s| s.parse::<i64>().unwrap())
        .collect();

    let time = lines[0];
    let distance = lines[1];

    let from = (time as f64 - ((time.pow(2) - 4 * distance) as f64).sqrt()) / 2.0;
    let to = (time as f64 + ((time.pow(2) - 4 * distance) as f64).sqrt()) / 2.0;

    println!("{}", (to - from) as i64);
}
