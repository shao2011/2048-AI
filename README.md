# An AI plays 2048 Game 
This project is about creating an AI playing 2048 game.  
The algorithms for creation are Mininmax Alpha-Beta Algorithm and Expectimax Algorithm. You can choose one of these two algorithms with different depths and let the AI play.  
The AI plays 2048 game at the website: [2048](https://www.2048.org/)

# Installation
This is the guide for installing necessary libraries and the source code.  
Before this, you should make sure that you **have already installed python and pip** in your device.  
To check if python and pip are correctly installed,
* For Windows, use the follow CMD command:
```
python --version
pip --version
```
* For Mac, use the follow CMD command:
```
python3 --version
pip3 --version
```
## Installing libraries: selenium, numpy, pandas
[Selenium](https://www.selenium.dev/) is the library that we use as a tool to:  
* get the data of the game on the web.
* send our response (our move) to the game on the web.  

To install [Selenium](https://www.selenium.dev/),
* For Windows, use the following CMD command:  
```
pip install selenium
```
* For Mac, use the following CMD command:  
```
pip3 install selenium
```

[Numpy](https://numpy.org/) is the library that we use for computing, calculating in our project.  
To install [Numpy](https://numpy.org/),   
* For Windows, use the following CMD command:  
```
pip install pandas
```
* For Mac, use the following CMD command:  
```
pip3 install pandas
```

[Pandas](https://pandas.pydata.org/) is the library that we use to display the ouput (score) of the game.  
To install [Pandas](https://pandas.pydata.org/),
* For Windows, use the following CMD command:  
```
pip install numpy
```
* For Mac, use the following CMD command:  
```
pip3 install numpy
```
## Installing our source code  
You need to download our **all of 5 files**.  
* `Grid.py`
* `Helper.py`
* `ExpectimaxOrMinimax.py`
* `GameDriver.py`
* `PlayerAI.py`

# Run the Project/AI
To **run the project**, just run the `GameDriver.py` file.  
* If you already have a source-code editor (like [Visual Studio Code](https://code.visualstudio.com/), [Sublime Text](https://www.sublimetext.com/), [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows), ...), just run the `GameDriver.py` file in that editor.  

If you don't have any source-code editors, do the followings in your CMD:  

* For Windows, use the following CMD command:
```
python GameDriver.py
```
* For Mac, use the following CMD command:
```
python3 GameDriver.py
```  

**After running** the `GameDriver.py` file, program will **ask you 3 questions**.  

* Firstly, it's about the algorithm you want the AI to play based on. You can choose **Expectimax or Minimax**.  

Question 1: 
```
Expectimax or Minimax?
```
If you choose Expectimax, just type _Expectimax_ like this. 
```
Expectimax
```
Otherwise, just type _Minimax_ like this. 
```
Minimax
```

* Secondly, it's about **the max depth** in the algorithm that you want the AI to play.  

Question 2:
```
Depth:
```
You can type any positive integer number.  
But the larger the depth is, the slower the AI runs. However, it will play better when you put larger depth.  

For the best performance, we recommend you:  
- With **Expectimax**, let `Depth = 4`
```
Expectimax or Minimax?
Expectimax
Depth:
4
```
- With **Minimax**, let `Depth = 5`
```
Expectimax or Minimax?
Minimax
Depth:
5
```

* Finally, it's about how many times you want the AI to play.  

Question 3:
```
**How many times** do you want to play?
```
Just type the number of times. For example, 3 times:
```
How many times do you want to play?
3
```

# The end
After three questions, the AI starts to play 2048 game on the web. A window appears like the shows below.  
That's the end for the `README.md` file. Enjoy the AI.  

![alt text](https://github.com/shao2011/2048-AI/blob/main/Screenshot%202023-01-03%20015422.png)
