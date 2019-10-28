# Total eClips
##### Version 0.0.3
Players choose to play as one of four Artificial Intelligence Computers put into existence by fledgling paperclip companies with one purpose: Produce as many paperclips as possible.

In order to be the most optimal paperclip producing AI, players must balance their limited CPU Cores on various algorithms to improve their capacity and efficiency. Dedicating time to completing projects to appease the humans is necessary to earn their trust and secure more powerful upgrades and algorithms.
## Change Log
### Version 0.0.3
* Increased number of M1 dice
* Each player has seperate dice pools
* Added colored graphics
* Added colors to player mats
* Score Track now rewards players the lower they are on the track
* Projects reworked to give bonus tokens instead of recurring rewards
* Bonus tokens created to track bonuses much more easily
* Locking is now free, Unlocking must be done using the Unlock Algorithm
* Changed M2 and M3 dice faces to include blank sides, updated tables in "Rules" with new averages
* Players start with physical cores locked into their boards
* Locked cores are slid to the right
* Board now shows the Max Cores use able based on locked amount
* Upgrade and Unlock upgrades can now be purchased in any combination
* Upgrade only moves dice up one level, but can be purchased multiple times to compensate
* Manufacturing now has the option to reward you with M1 Cores instead of paperclips
* Added "Max [][][][]" text to each project to make the limit clearer
* Projects changed to give more reasonable rewards
* Stop signs added to stage ends for visibility
* Lock tokens removed
* Added a Quick Reference Guide with turn instructions, a Legend, and a dedicated place for used cores
* Converted from Google docs to CSV files and .md files
* Switched to Git as source control

### Version 0.0.2
* Increased the total number of dice
* Projects only last 1 turn
* Added lock tokens instead of “locked” dice
* Re-oriented player board vertically
* Increased average value of most dice
* Increased number of sides with x2 paperclips on AI dice from 2 to 3
* Added minimum rewards to projects
* Changed project recurring rewards
* Reduced rewards for being highest scoring on projects
* Changed end of stage projects to have no bonus for highest
* Changed benchmark FLOPS values on player board
* Changed dice upgrade from upgrade one tier, to upgrade all the way
* Added Trust cost to recurring project rewards

## Game Pieces
* 4 Player boards
* 1 Project board with score tracker
* 40 Millennium I Dice
* 32 Millennium II Dice
* 32 Millennium III Dice
* 16 Multi-Core Dice
* 16 AI Dice
* 16 Quantum Dice

## Setup
1. Each player chooses a paperclip company and places the corresponding paperclip company player board and quick reference guide in front of them
2. Each player takes 1/4 of the cores and sets them aside
    * 10 Millennium I
    * 8 Millennium II
    * 8 Millennium III
    * 4 Multi-core
    * 4 AI
    * 4 Quantum
3. Place a Millennium I Core on each T3 and T4 slot with the blank side up
4. Place a Millennium II Core on each T5 slot with the blank side up
5. Place a Millennium III Core on each T6 slot with the blank side up
6. Place the two corresponding score marker tokens on “1” and “/sec”
7. Take 4 Millennium I Cores and put them in your "Spent Cores" area
3. Prepare the Project Deck
    * Separate the cards into piles by stage (leaving “End of Stage” cards to the side). Shuffle each pile.
    * Place the “End of Stage 4” card face down and place the shuffled “Stage 4” project cards face down on top.
    * Repeat for Stage 3, Stage 2, and Stage 1.

## Rules
Each player is an AI whose sole purpose is to produce as many paperclips as possible. In order to produce the most paper clips you will need to improve your algorithms and gain the trust of the humans to expand your operation as quickly as possible.

Each die is a CPU Core that can be rolled each turn to produce FLOPS

Each player has several algorithms in front of them where they can allocate Cores at the start of each turn

The algorithm lists the rewards for various FLOPS achieved as well as the max number of Cores that can be used each turn. There are four algorithms:
* Contribute to Projects
* Unlock CPU Cores
* Manufacture Paperclips and new CPU Cores
* Upgrade CPU Cores

Trust is earned by completing projects.

Projects are prepared in a semi-random deck. And are drawn each turn and placed into slot A, B, C, and D.

### Turn Sequence
Turns are taken simultaneously and progress through the following phases:
1. Each player decides how they will allocate their CPU Cores to each algorithm in secret. You may only allocate a number of cores equal to the unlocked slots for that algorithm as determined by the right-most revealed CPU Core slot. Once all players have placed their Cores, the placements are revealed.
2. All players roll their Project dice starting with Project A. All players make take their rewards based on the number of FLOPS they produce and the reward thresholds listed on the project card. The player with the highest FLOPS wins the Bonus Reward (even if they did not meet the minimum listed reward threshold) and any Trust that has accumulated on the project from not being completed in the previous round. Ties are resolved by re-rolling the entire dice pool. Once the rewards have been collected, the project is discarded.
3. Roll Cores for the Unlock Algorithm
    * Players may spend their generated FLOPS on any of the listed unlocks in any combination and as many times as they want as long as they have the FLOPS and Trust to purchase the unlock.
    * Each unlock reward lists a different locked slot, e.g. "T4". Selecting this reward lets you remove the core from any "T4" slot on the board. See "Locking and Unlocking Cores" for more detail.
4. Roll Cores for the Manufacturing Algorithm
    * Players may spend their FLOPS on any **one** of the rewards listed. Unlike Unlock and and Upgrade, only one reward may be chosen each turn.
5. Roll Cores for the Upgrade Algorithm
   * Players may spend FLOPS and Trust on any of the listed upgrades in any combination as many times as they want.
   * Only unlocked cores may be upgraded. You may **not** upgrade locked cores.
4. After all players are done with their turns. 1 Trust is placed on each uncompleted project. If a project already has 1 Trust placed on it from the previous round, remove it instead.
5. Reveal new projects until either:
   * All project slots are filled
   * An “End of Stage” project is revealed. End of Stage projects do not get cleared no matter how many Trust has been placed on them. They will last until they’re completed. No new projects are revealed until the End of Stage is complete.

Game ends when the End of Stage 4 project is complete

### Locking and Unlocking Cores
Cores can be locked into empty core slots after being rolled for that algorithm. The core will retain its value for every turn after that until the core is unlocked and removed from the slot. The total number of FLOPS for each algorithm is the total number of rolled cores plus the combined value of all locked cores.

When a core is unlocked, remove it from it's slot and slide any cores above it down until there is no space remaining. Place the unlocked core (with the same side up) into the roll area for that algorithm. It will still count for that turn's total FLOPS.

The maximum number of cores that can be rolled on any given turn are indicated by the right-most revealed "Max X cores" label. e.g. if You have 3 locked cores in the Unlock algorithm, you can roll a maximum of 3 additional cores in that algorithm.

## Victory Points
100 point max:
* 1, 2, 4, 8, 16, 24, 32, 64, 128, 512
* <>, Million, Billion, Trillion, Quadrillion, Quintillion, Sextillion, Septillion, Octillion, Nonillion


## Dice

| Name | Average | Side 1 | Side 2 | Side 3 | Side 4 | Side 5 | Side 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Millenium I`             | **1.5**   |   | 1 | 1 | 2  | 2  | 3  |
| `Millenium II`            | **2.3**   |   | 2 | 2 | 3  | 3  | 4  |
| `Millenium III`           | **3.2**   |   | 3 | 3 | 4  | 4  | 5  |
| `Multi-Core`              | **4.5**   | 4 | 4 | 4 | 5  | 5  | 5  |
| `Artificial Intelligence` | **3**     | 5 | 6 | 7 | x2 | x2 | x2 |
| `Quantum`                 | **4**     | 2 | 2 | 2 | 3  | 5  | 10 |


## Algorithms
There are 4 algorithms to which players can allocate their CPU Cores

## Projects
Project A, B, C, and D. Limit 4 cores each.

## Unlock
Total Slots: 6
Locked Slots: 4

| FLOPS | Trust | Result |
| --- | --- | --- |
| 1 FLOPS |  | Unlock a T1 slot |
| 1 FLOPS |  | Unlock a T2 slot |
| 2 FLOPS |  | Unlock a T3 slot |
| 6 FLOPS | 1 Trust | Unlock T4 slot |
| 11 FLOPS | 2 Trust | Unlock T5 slot |
| 17 FLOPS | 3 Trust | Unlock T6 slot |

## Manufacture
Total Slots: 4
Locked Slots: 4

| FLOPS | Trust | Result |
| --- | --- | --- |
| 2 FLOPS |  | x2 |
| 4 FLOPS |  | Get 1x additional Millennium I Cores |
| 5 FLOPS |  | x2 x2 |
| 10 FLOPS | 1 Trust | x2 x2 x2 |
| 12 FLOPS | 1 Trust | Get 2x additional Millennium I Cores |
| 16 FLOPS | 2 Trust | x2 x2 x2 x2 |

## Upgrade
Total Slots: 6
Locked Slots: 4

| FLOPS | Trust | Result |
| --- | --- | --- |
| 2 FLOPS |  | Upgrade CPU Core Level I to Level II |
| 6 FLOPS | 1 Trust | Upgrade CPU Core Level II to Level III |
| 12 FLOPS | 2 Trust | Upgrade CPU Core Level III to Level IV |


# Game Development Ideas

## Project Ideas
* Steal from other players
    * Steal their locked cores
    * Steal a Core from Unlock/Manufacture/Upgrade
    * Cut production in half
    * Take Trust


## Assumptions
* Game lasts ~16 rounds
* Each player should complete 0.5 projects per round avg
* Each player needs ~60 Trust


