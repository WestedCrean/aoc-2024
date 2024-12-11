use std::env;

fn main() {
    let day_number = String::from("1");
    let prefix = String::from("https://adventofcode.com/2024/day");
    let postfix = String::from("input");

    let s = format!("{prefix}/{day_number}/{postfix}");
    println!("The link is: {s}");

    let args: Vec<String> = env::args().collect();
    let day = &args[1];
    //dbg!(args);
    println!("The first arg is: {day}");
}

struct Config {
    query: String,
    file_path: String
}

fn parse_config(args: &[String]) -> Config {
    let day
}