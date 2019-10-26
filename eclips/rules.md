# Total eClips
##### Version 0.0.2
Players choose to play as one of four Artificial Intelligence Computers put into existence by fledgling paperclip companies with one purpose: Produce as many paperclips as possible.

In order to be the most optimal paperclip producing AI, players must balance their limited CPU Cores on various algorithms to improve their capacity and efficiency. Dedicating time to completing projects to appease the humans is necessary to earn their trust and secure more powerful upgrades and algorithms.
## Change Log
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
* 12 T1 Lock Tokens
* 12 T2 Lock Tokens
* 12 T3 Lock Tokens
* 12 T4 Lock Tokens
* 32 Millennium I Dice
* 32 Millennium II Dice
* 32 Millennium III Dice
* 16 Multi-Core Dice
* 16 AI Dice
* 16 Quantum Dice

## Setup
1. Each player chooses a paperclip company and places the corresponding paperclip company player board in front of them.
   * Place a Lock Token on the corresponding T1, T2, T3 and T4 slots
   * Take 4 Millennium I cubes and place them on your player board.
2. Place the two corresponding score marker tokens on “1” and “/sec”.
3. Prepare the Project Deck
   * Separate the cards into piles by stage (leaving “End of Stage” cards to the side). Shuffle each pile.
   * Place the “End of Stage 4” card face down and place the shuffled “Stage 4” project cards face down on top. Repeat for Stage 3, Stage 2, and Stage 1.

## Rules
Each person plays as an AI whose sole purpose is to produce as many paperclips as possible. In order to produce the most paper clips you will need to improve your algorithms and gain the trust of the humans.

Each die is a CPU Core that can be rolled each turn to produce FLOPS

Each player has several algorithms in front of them where they can allocate Cores at the start of each turn

The algorithm lists the rewards for various FLOPS achieved as well as the max number of Cores that can be used each turn. There are four algorithms
* Unlock CPU Cores
* Upgrade CPU Cores
* Contribute to Project A, B, C, D...
* Improve Manufacturing

Trust is earned by completing projects.


Projects are prepared in a semi-random deck. And are drawn each turn and placed into slot A, B, C, D etc.

Each project has a minimum FLOPS cost to complete and will have a random amount added to it with the roll of a dice.

Turns are taken simultaneously and progress through the following phases:
1. Each player decides how they will allocate their CPU Cores to each algorithm in secret. You may only allocate a number of cores equal to the unlocked slots for that algorithm. Once all players have placed their Cores the placements are revealed.
2. All players roll their Project dice starting with Project A. Any players that meet the minimum FLOPS requirement get the Base Reward. The player with the highest FLOPS wins the Bonus Reward. Ties are resolved by re-rolling the entire dice pool. Completed projects are removed
3. Players then roll their other dice pools starting with Expand, Improve and Industry
   * After rolling, players can spent 1 trust to dedicate a CPU core to that activity. This can be done as many times
   * Collect rewards based on FLOPS produced, some rewards may require spending trust to upgrade
4. After players are done rolling cores, 1 Trust is placed on each uncompleted project. If a project already has 1 Trust placed on it from the previous round, remove it instead.
5. Reveal new projects until either:
   * All project slots are filled
   * An “End of Stage” project is revealed. End of Stage projects do not get cleared no matter how many Trust has been placed on them. They will last until they’re completed. No new projects are revealed until the End of Stage is complete.

Game ends when the End of Stage 4 project is complete

## Victory Points
100 point max:
* 1, 2, 4, 8, 16, 24, 32, 64, 128, 512
* <>, Million, Billion, Trillion, Quadrillion, Quintillion, Sextillion, Septillion, Octillion, Nonillion


## Dice

| Name | Average | Side 1 | Side 2 | Side 3 | Side 4 | Side 5 | Side 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Millenium I` | **1.5** | | 1 | 1 | 2 | 2 | 3 |
| `Millenium II` | **2.5** | 1 | 2 | 2 | 3 | 3 | 4 |
| `Millenium III` | **3.5** | 2 | 3 | 3 | 4 | 4 | 5 |
| `Multi-Core` | **4.5** | 4 | 4 | 4 | 5 | 5 | 5 |
| `Artificial Intelligence` | **3** | 5 | 6 | 7 | x2 | x2 | x2 |
| `Quantum` | **4** | 2 | 2 | 2 | 3 | 5 | 10 |


## Algorithms
There are 4 algorithms to which players can allocate their CPU Cores
## Projects
Project A, B, C, and D. Limit 4 cores each.
## Expand
Total Slots: 6
Locked Slots: 4

| FLOPS | Trust | Result |
| --- | --- | --- |
| 3+ FLOPS | *Free* | Unlock a T1 slot |
| 7+ FLOPS | Spend 1 Trust | Unlock a T2 slot |
| 12+ FLOPS | Spend 2 Trust | Unlock T3 slot |
| 18+ FLOPS | Spend 3 Trust | Unlock T4 slot |
## Improve
Total Slots: 6
Locked Slots: 4

| FLOPS | Trust | Result |
| --- | --- | --- |
| 3+ FLOPS | *Free* | Upgrade CPU Core 1 Grade to max Grade II |
| 6+ FLOPS | Spend 1 Trust | Upgrade CPU Core 1 Grade to max Grade III |
| 10+ FLOPS | Spend 1 Trust | Upgrade CPU Core 1 Grade to max Grade IV |
| 15+ FLOPS | Spend 2 Trust | Upgrade CPU Core 1 Grade to max Grade IV |
## Industry
Total Slots: 4
Locked Slots: 4

| FLOPS | Trust | Result |
| --- | --- | --- |
| 2+ FLOPS | *Free* | x2 |
| 5+ FLOPS | *Free* | x2 |
| 9+ FLOPS | *Free* | x2 |
| 14+ FLOPS | Spend 1 Trust | x2 |
| 20+ FLOPS | Spend 1 Trust | x2 |

## Projects
Projects should primarily reward Trust but can provide other rewards as well.
* Paperclip production x2
* Upgrade Cores
* Unlock Cores
In the competitive version where only one player wins there could be other rewards
* Card can be used to re-roll dice in the future (or every turn)
* Can be used as one-time-use bonus FLOPS (anywhere, or just for certain algorithms)
* Permanent increase in FLOPS for certain algorithm
* Card kept as new algorithm where dice can be assigned to produce various rewards
* Give permanent FLOPS bonuses to certain classes or combinations of CPU core types. E.g. if an AI Core and Quantum Core are used in the same algorithm: +1 FLOPS


## Assumptions
* Game lasts ~16 rounds
* Each player should complete 0.5 projects per round avg
* Each player needs ~60 Trust


