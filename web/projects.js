// One entry per day folder. Only each folder's main.py is shown and run.
// `imports` lists the local modules main.py imports, so they can be loaded
// alongside it. Set `main: false` for folders that have no main.py yet.
export const PROJECTS = [
  { folder: "day01", title: "Band Name Generator" },
  { folder: "day02", title: "Tip Calculator" },
  { folder: "day03", title: "Treasure Island Game" },
  { folder: "day04", title: "Rock Paper Scissors Game" },
  { folder: "day05", title: "Password Generator" },
  { folder: "day06", title: "Python Functions", main: false },
  { folder: "day07", title: "Hangman Game", imports: ["hangman_art.py", "hangman_words.py"] },
  { folder: "day08", title: "Caesar Cipher", imports: ["caesar_art.py"] },
  { folder: "day09", title: "Silent Bidding Auction", imports: ["art.py"] },
  { folder: "day10", title: "Calculator", imports: ["art.py"] },
  { folder: "day11", title: "Blackjack Game", main: false },
  { folder: "day12", title: "Number Guessing Game", imports: ["art.py"] },
];
