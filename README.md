# Wikihow Dungeon

### An AI Dungeon inspired game trained using Wikihow to generate puzzles

Project Description: Our project idea is to create a AI-Dungeon like gaming experience where the player will try to solve Wikihow-generated puzzles

- In the beginning of the game, the game will generate an initial situation for the player such as “You are (generate name). You are in (generate location). You have (generate description and items) nearby. You want (generate goal). What do you do?”.
- As the player types commands, depending on the chosen action, the game will generate a text that describes the consequences of the action and the next situation/puzzle. The puzzles themselves will be derived from Wikihow articles by parsing and extracting information from the given article.
- If the player manages to reach the goal state (complete the chore/puzzle), they will win. 

Proposed Method: After talking to Daphne, we decided to split the problem into two parts. The first part will have an interactive game component which will take inputs from WikiHow articles and build interactive educational experiences around it. The second part will involve fine-tuning a GPT-2 model for generating WikiHow articles and passing these generated articles to our first component to generate stories and puzzles.
- The first part will involve parsing and extracting information from WikiHow articles. The player will be presented scenarios and will be asked to pick the right action. Here is one example that Daphne provided us from a WikiHow article:
  - Your goal is to put on a step-in harness. Nearby, you see a harness and a dog. Which action should you take first?
    - Place the unbuckled harness on the ground
    - Pick up the right paw and move it forward into the appropriate loop
    - Reward your pup with a treat and praise
- If the player picks the false action, they will be warned by a ‘Please try again message.’, once they pick the correct action our component will take this action and generate the next problem. The 3 options provided to the player will be generated through taking the correct next action and filling the remaining two false actions by parsing the rest of the article and picking a random possible action.
- Once this first component works properly, we will fine-tune a GPT-2 model for generating WikiHow articles. When these articles are generated, we can simply pass them to our problem-solution puzzle component and have interesting sequences of puzzles.

Data: We’re planning to use Wikihow dataset and other possible sources similar to Wikihow such as eHow.
The dataset exists online and are:
- https://www.wikihow.com/Main-Page
- https://www.ehow.com
- https://www.howstuffworks.com

Related work: The most similar existing game experience to our project is AI Dungeon.
- Our game will likely follow similar training, text generation and game state structures as AI Dungeon.
- Similar to how new puzzles and scenarios are created in AI Dungeon after each action, we’re expecting to be able to create new settings for the player to explore

Team members and tasks:
- Gizem Dal: Will work on WikiHow article parsing and extracting scenario puzzles for the first component
- Sri Sanjeevini Ganni: Web scraping, Changing sentences to second person perspective 
- Andrew Martin: Will work on fine-tuning GPT-2 model to generate new articles

References:
Clark, E., Ji, Y. and Smith, N.A., 2018, June. Neural text generation in stories using entity representations as context. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers) (pp. 2250-2260). Yao, L., Peng, N., Weischedel, R., Knight, K., Zhao, D. and Yan, R., 2019, July. Plan-and-write: Towards better automatic storytelling. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 33, pp. 7378-7385).
