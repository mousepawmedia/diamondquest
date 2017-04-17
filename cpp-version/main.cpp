#include <algorithm>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <limits.h>
#include <math.h>
#include <cstdlib>
#include <time.h>
#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

const int DEFAULT_RANGE = 20;

//Game mode.
int gm;

int score = 0;

struct highscore
{
    string player;
    int score;
    bool operator < (const highscore& rhs) const {
        return score > rhs.score;                   //I inverted this logic to show highscores in inverse order (high to low).
    }
};

vector<highscore> highscores;

void showDiamond();
void showCredits();
int showMenu();
int getGameMode();
bool playGame();
void checkHighscore(int);
void showHighscores();

void messageCorrect();
void messageIncorrect();
void messageNotSimplified();

void dig();
void showGem1();
void showGem2();
void showGem3();
void showFossil();
void showCoin();
void showSword();
void showStone();

void writeToHighscores(string, int);
void loadHighscores();

bool compareByScores(const highscore, const highscore);
void sortHighscores();

int cantorPairing(int, int);
int getXFromCantor(int);
int getYFromCantor(int);

float parse(string, bool=true);
bool isSimplestForm(int, int);

int generateNumber(int = -1, int = DEFAULT_RANGE);

float showProblem();

int main()
{
    srand(time(NULL));              //Seed random.

    showDiamond();
    showCredits();
    bool repeat;

    while(true)
    {
        int option = showMenu();
        switch(option)
        {
            case 1:
            {
                gm = getGameMode();
                do                      //This will run once by default.
                {
                    repeat = playGame();
                }
                while(repeat);
                break;
            }
            case 2:
            {
                loadHighscores();
                showHighscores();
                break;
            }
            case 3:
            {
                return 0;
                break;
            }
        }
    }

    return 0;
}

//MAIN DISPLAY SCREENS

//Show diamond ASCII artwork.
void showDiamond()
{
    cout << "      __________________" << endl
        << "    .-'  \\ _.-''-._ /  '-." << endl
        << "  .-/\\   .'.      .'.   /\\-." << endl
        << " _'/  \\.'   '.  .'   './  \\'_" << endl
        << ":======:======::======:======:" << endl
        << " '. '.  \\     ''     /  .' .'" << endl
        << "   '. .  \\   :  :   /  . .'" << endl
        << "     '.'  \\  '  '  /  '.'" << endl
        << "       ':  \\:    :/  :'" << endl
        << "         '. \\    / .'" << endl
        << "           '.\\  /.' " << endl
        << "             '\\/'" << endl;
}

//Display game title and credits.
void showCredits()
{
    cout << "DIAMOND QUEST v1.0" << endl;
    cout << "MousePaw Labs" << endl;
    cout << "http://www.mousepawgames.com/labs" << endl;
    cout << "Concept and Programming by Jason C. McDonald" << endl;
    cout << "Diamond ASCII art by miK" << endl;
    cout << "Most Additional ASCII art by Joan G Stark" << endl << endl;
}

int showMenu()
{
    int option;
    string buffer;

    cout << "---SELECT AN OPTION---" << endl;
    cout << "1: Start New Game" << endl;
    cout << "2: High Scores" << endl;
    cout << "3: Quit" << endl;

    getline(cin, buffer);
    option = atof(buffer.c_str());

    return option;
}

//Display options.
int getGameMode()
{
    int mode, type, gm;
    string buffer;

    //Get game mode.
    cout << "---CHOOSE GAME TYPE---" << endl;
    cout << "1: Add and Subtract" << endl;
    cout << "2: Multiply" << endl;
    cout << "3: Divide" << endl;
    cout << "4: Multiply and Divide" << endl;
    getline(cin, buffer);
    mode = atof(buffer.c_str());

    cout << "---CHOOSE DIFFICULTY---" << endl;
    cout << "1: Positive Numbers Only" << endl;
    cout << "2: Positive and Small Negative Numbers" << endl;
    cout << "3: Positive <> Negative Numbers" << endl;
    getline(cin, buffer);
    type = atof(buffer.c_str());

    //Implement Cantor pairing function. Mode is x and Type is y
    gm = cantorPairing(mode, type);

    cout << endl << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl << endl;

    return gm;
}

bool playGame()
{
    cout << endl << endl << endl;
    int depth;
    bool r;
    float expectedAnswer;
    string input;

    //Ask for depth...
    cout << "How deep you want to dig? (How many math problems?) \nEnter a number between 3 and 20: ";
    getline(cin, input);
    depth = atof(input.c_str());

    //Validate depth.
    while(depth > 20 || depth < 3)
    {
        cout << "You can dig between 3 and 20 math problems deep." << endl;
        cout << "How deep you want to dig? (Between 3 and 20)." << endl;
        getline(cin, input);
        depth = atof(input.c_str());
    }

    cout << endl << endl << "You grab your pickaxe and start digging!" << endl << endl;

    score = 0;

    for(int i = 0; i < depth; i++)
    {
        expectedAnswer = showProblem();

        getline(cin,input);
        float answer = parse(input, true);

        if(answer == NULL)
        {
            answer = parse(input, false);       //Parse again, ignoring simplification.
            if(answer == expectedAnswer)        //If given answer is the calculated answer...
            {
                messageNotSimplified();
                cout << endl;
            }
            else                            //Otherwise...
            {
                messageCorrect();
                cout << endl;
                dig();
            }
        }
        else
        {
            if(answer == expectedAnswer)     //If given answer is the calculated answer...
            {
                messageCorrect();
                cout << endl;
                dig();
            }
            else                            //Otherwise...
            {
                messageIncorrect();
                cout << endl;
            }
        }

        cout << endl << "SCORE: " << score << endl << endl;
    }

    cout << endl << "You return to the surface with your treasures.\nGreat job! Your score is " << score << endl;
    checkHighscore(score);

    cout << endl << "Play again? (Y/N): ";
    getline(cin, input);
    if(input == "Y" || input == "y")
    {
        r = true;
    }
    else
    {
        r = false;
    }

    cout << endl << endl << endl;

    return r;
}

//Check if score is a new highscore, and then save it.
void checkHighscore(int newScore)
{
    stringstream stream;
    string buffer, player;

    for(int i=0; i<highscores.size(); i++)
    {
        if(i==10)               //Don't iterate past 10.
        {
            break;
        }
        if(newScore > highscores[i].score)
        {
            cout << "New high score! Enter your name (no spaces): ";
            getline(cin, buffer);

            stream << buffer;
            player = stream.str();

            writeToHighscores(player, newScore);
        }
    }

    if(highscores.size() == 0)
    {
        cout << "New high score! Enter your name (no spaces): ";
        getline(cin, buffer);

        stream << buffer;
        stream >> player;

        writeToHighscores(player, newScore);
    }
}

void showHighscores()
{
    cout << endl;
    for(int i=0; i<highscores.size(); i++)
    {
        if(i==10)               //Don't iterate past 10.
        {
            break;
        }
        else
        {
            cout << highscores[i].player << ": " << highscores[i].score << " points." << endl;
        }
    }
    cout << endl << endl;
}

//Generate and display a problem based on game data.
float showProblem()
{
    int x = getXFromCantor(gm);

    int firstNum, secondNum, multiplier;

    float expectedAnswer;

    bool whichWay = rand() % 2 == 1;                 //Generate a random true/false.

    switch(x)
    {
        case 1:
        {
            //Addition and subtraction.
            firstNum = generateNumber();
            secondNum = generateNumber(firstNum);

            if(whichWay)    //Add...
            {
                expectedAnswer = firstNum + secondNum;
                cout << firstNum << " + " << secondNum << " = ";
            }
            else            //Subtract...
            {
                expectedAnswer = firstNum - secondNum;
                cout << firstNum << " - " << secondNum << " = ";
            }
            break;
        }
        case 2:
        {
            //Multiplication. Use 1-12 range.
            firstNum = generateNumber(-1, 12);
            secondNum = generateNumber(firstNum, 12);
            expectedAnswer = firstNum * secondNum;
            cout << firstNum << " * " << secondNum << " = ";
            break;
        }
        case 3:
        {
            //Divison. Use 1-12 range.
            firstNum = generateNumber(-1, 12);
            secondNum = generateNumber(firstNum, 12);

            //Get another number to multiply top and bottom by, for simplification practice.
            multiplier = generateNumber(-1, 10);
            firstNum *= multiplier;
            secondNum *= multiplier;

            expectedAnswer = static_cast<float>(firstNum) / static_cast<float>(secondNum);
            cout << firstNum << " / " << secondNum << " = ";
            break;
        }
        case 4:
        {
            //Multiplication and division. Use 1-12 range.
            firstNum = generateNumber(-1, 12);
            secondNum = generateNumber(firstNum, 12);
            if(whichWay)    //Multiply...
            {
                expectedAnswer = firstNum * secondNum;
                cout << firstNum << " * " << secondNum << " = ";
            }
            else            //Divide...
            {
                //Get another number to multiply top and bottom by, for simplification practice.
                multiplier = generateNumber(-1, 10);
                firstNum *= multiplier;
                secondNum *= multiplier;

                expectedAnswer = static_cast<float>(firstNum) / static_cast<float>(secondNum);
                cout << firstNum << " / " << secondNum << " = ";
            }
            break;
        }
    }

    return expectedAnswer;
}


//MESSAGE GENERATORS

void messageCorrect()
{
    string msg;
    int i = rand()%(9-1 + 1) + 1;

    switch(i)
    {
        case 1:
        {
            msg = "Good job!";
            break;
        }
        case 2:
        {
            msg = "That's right!";
            break;
        }
        case 3:
        {
            msg = "Correct!";
            break;
        }
        case 4:
        {
            msg = "Very good!";
            break;
        }
        case 5:
        {
            msg = "Nice work!";
            break;
        }
        case 6:
        {
            msg = "Right on!";
            break;
        }
        case 7:
        {
            msg = "Woo hoo!";
            break;
        }
        case 8:
        {
            msg = "Excellent work!";
            break;
        }
        case 9:
        {
            msg = "Go you!";
            break;
        }
    }

    cout << msg << endl;
}

void messageIncorrect()
{
    string msg;
    int i = rand()%(6-1 + 1) + 1;

    switch(i)
    {
        case 1:
        {
            msg = "Oops, that's wrong.";
            break;
        }
        case 2:
        {
            msg = "Not quite.";
            break;
        }
        case 3:
        {
            msg = "That's not right.";
            break;
        }
        case 4:
        {
            msg = "Uh oh, that's wrong.";
            break;
        }
        case 5:
        {
            msg = "Ouch, that's not it.";
            break;
        }
        case 6:
        {
            msg = "Sorry, that's wrong.";
            break;
        }
    }

    cout << msg << endl;
}

void messageNotSimplified()
{
    string msg;
    int i = rand()%(4-1 + 1) + 1;

    switch(i)
    {
        case 1:
        {
            msg = "While correct, that's not in its simplest form.";
            break;
        }
        case 2:
        {
            msg = "Good, but it should be simplified.";
            break;
        }
        case 3:
        {
            msg = "Right, but remember to simplify!";
            break;
        }
        case 4:
        {
            msg = "That is correct, but not simplified.";
            break;
        }
    }

    cout << msg << endl;
}

//GAMEPLAY FUNCTIONS
void dig()
{
    int i = rand()%(12-1 + 1) + 1;

    cout << "Digging..." << endl;
    switch(i)
    {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        {
            //Dirt
            cout << "Hm. More stone. (1 point)" << endl;
            showStone();
            score += 1;
            break;
        }
        case 6:
        {
            //Coin
            cout << "You found an old coin! (2 points)" << endl;
            showCoin();
            score += 2;
            break;
        }
        case 7:
        {
            //Sword
            cout << "You found an old sword! (3 points)" << endl;
            showSword();
            score += 3;
            break;
        }
        case 8:
        {
            //Fossil
            cout << "You found a fossil! (4 points)" << endl;
            showFossil();
            score += 4;
            break;
        }
        case 9:
        {
            //Emerald
            cout << "You found an emerald! (5 points)" << endl;
            showGem1();
            score += 5;
            break;
        }
        case 10:
        {
            //Sapphire
            cout << "You found a sapphire! (6 points)" << endl;
            showGem2();
            score += 6;
            break;
        }
        case 11:
        {
            //Ruby
            cout << "You found a ruby! (7 points)" << endl;
            showGem3();
            score += 7;
            break;
        }
        case 12:
        {
            //Diamond
            cout << "You found a diamond! (8 points)" << endl;
            showGem3();
            score += 8;
            break;
        }
    }
}

//ARTWORK

//Show narrow pointed gem.
void showGem1()
{
    cout << "  ____" << endl
         << " /___/\\" << endl
         << "//o  \\_\\" << endl
         << "\\\\  // /" << endl
         << " \\\\ / /" << endl
         << "  \\X /" << endl
         << "   \\/" << endl;
}

//Show hexagonal gem.
void showGem2()
{
    cout << "  ____" << endl
         << " /\\__/\\" << endl
         << "/_/  \\_\\" << endl
         << "\\ \\__/ /" << endl
         << " \\/__\\/" << endl;
}

//Show wide pointed gem.
void showGem3()
{
    cout << "   _______" << endl
         << " .'_/_|_\\_'." << endl
         << " \\`\\  |  /`/" << endl
         << "  `\\\\ | //'" << endl
         << "    `\\|/`" << endl
         << "      `" << endl;
}

//Show bone (fossil).
void showFossil()
{
    cout << " .-.               .-." << endl
         << "(   `-._________.-'   )" << endl
         << " >=     _______     =<" << endl
         << "(   ,-'`       `'-,   )" << endl
         << " `-'               `-'" << endl;
}

void showCoin()
{
    cout << "      ..-\"\"\"\"\"-.."  << endl
         << "    .'    ___    '."  << endl
         << "   /    .\"\\  `\\    \\"  << endl
         << "  ;    /, (    |    ;"  << endl
         << " ;    /_   '._ /     ;"  << endl
         << " |     |-  '._`)     |"  << endl
         << " ;     '-;-'  \\      ;"  << endl
         << "  ; \"\"\"\" /    \\\\    ;"  << endl
         << "   \\    '.__..-'   /"  << endl
         << "    '._ 1 9 3 2 _.'"  << endl
         << "       \"\"-----\"\""  << endl;
}

void showSword()
{
    cout << "       |______________" << endl
         << "[======|______________>" << endl
         << "       |" << endl
         << "       '" << endl;
}

void showStone()
{
    cout << "#,,##.###.#" << endl
         << "###.##,####" << endl
         << "##'####',##" << endl
         << "###..###,##" << endl
         << "#.,#.######" << endl;
}

//MATHEMATICAL FUNCTIONS

//Generate a number. If previous number is -1, there was no previous number.
//Previous number should be used to get a second, possibly negative, number.
//Range should be a positive integer defining upper bound.
int generateNumber(int prevNumber, int range)
{
    int y = getYFromCantor(gm);

    int randInt;                                //Variable for a random number.
    bool neg;                                   //Make number negative?
    int r;                                      //Random number for return.

    if(y == 1)                                  //If game mode wants only positive numbers...
    {
        neg = false;
    }
    else
    {
        neg = rand() % 2 == 1;                 //Generate a random true/false.
    }

    if(prevNumber > -1 && y == 2 && neg == true)
    {
        //If we specifically need a smaller negative than previous postive, use this.
        randInt = rand()%(range+(prevNumber-1) + 1) - (prevNumber-1);
    }
    else                                        //Otherwise...
    {
        randInt = rand()%(range-1 + 1) + 1;     //Generate a random number.
    }

    if(neg)             //If it wants a negative number...
    {
        r = -randInt;   //Negate the random number for return.
    }
    else                //Otherwise.
    {
        r = randInt;    //Leave it positive.
    }

    return r;
}

float parse(string input, bool simplestOnly)
{
    float r;

    if(input.find('/') == -1)
    {
        r = atof(input.c_str());
    }
    else
    {
        //Parse as a fraction.
        float num, den;
        bool lineFlag = false;
        string buffer;
        stringstream stream;
        for(int ch=0;ch<input.length();ch++)
        {
            if(input[ch] != '/')            //If the character isn't a slash...
            {
                stream << input[ch];        //Push character to stream.
            }
            else if(!lineFlag)
            {
                //Parse buffer as numerator.
                buffer = stream.str();      //Retrieve string from stringstream.
                num = atof(buffer.c_str()); //Parse string to float.
                buffer = "";                //Clear buffer.
                stream.str(std::string());  //Clear stream.
            }
        }
        //Parse reminaing buffer as denominator.
        buffer = stream.str();              //Retrieve string from stringstream.
        den = atof(buffer.c_str());         //Parse string to float.

        if(simplestOnly && !isSimplestForm(num, den))
        {
            r = NULL;                       //Return as null.
        }
        else
        {
            r = num/den;                    //Return the value as num/den.
        }
    }
    return r;
}

bool isSimplestForm(int num, int den)
{
    bool isSimplest = true;             //Flag is fraction is in simplest form.
                                        //This is true by default, as it will fail the following test otherwise.

    for(int div=2;div<=den;div++)       //For all divisors (div) from 2 to denominator...
    {
        if(num%div==0 && den%div==0)      //If both numerator and denominator divide evenly...
        {
            isSimplest = false;         //Fraction can be simplified. Return false.
            break;                      //Break loop.
        }
    }

    return isSimplest;
}

//FILE SYSTEM FUNCTIONS

void writeToHighscores(string player, int score)
{
    ofstream scoreFile;
    scoreFile.open("diamondquest_highscores.dat", ios::out | ios::app);
    if(scoreFile.is_open())
    {
        scoreFile << player << " " << score << "\n";
        scoreFile.close();
    }
    else
    {
        cout << "Cannot open highscore file." << endl;
        return;
    }
}

void loadHighscores()
{
    ifstream scoreFile;

    highscore buffer;

    highscores.clear();

    scoreFile.open("diamondquest_highscores.dat", ios::in);
    if(scoreFile.is_open())
    {
        highscores.clear();
        while(scoreFile >> buffer.player >> buffer.score)
        {
            highscores.push_back(buffer);
        }
        sortHighscores();
    }
    else
    {
        cout << "No highscores." << endl;
        return;
    }
}

void sortHighscores()
{
    sort(highscores.begin(), highscores.end());
}

//CANTOR FUNCTIONS

//Create cantor pairing.
int cantorPairing(int x, int y)
{
    int z;
    z = 0.5 * (x+y) * (x+y+1) + y;
    return z;
}

//Derive x from cantor pairing.
int getXFromCantor(int z)
{
    int x, y, w;
    float t;

    w = (sqrt(8*z+1) - 1)/2;
    t = (pow(w, 2) + w) / 2;
    y = z - t;
    x = w - y;

    return x;
}

//Derive z from cantor pairing.
int getYFromCantor(int z)
{
    int x, y, w;
    float t;

    w = (sqrt(8*z+1) - 1)/2;
    t = (pow(w, 2) + w) / 2;
    y = z - t;
    x = w - y;

    return y;
}
