#include <iostream>
#include <cmath>
#include <climits>

/*
Funtion Declaration
*/
int winningcondition(const char* pMarked);
void printingwinner(int wincon, const char* pMarked);
void boardvisual(const char* marked);
void drawXvisual(char *pmarked, int row);
void ComputerMove(char *pmarked, int row,int& posible);
int minimax(char *pmarked,int depth,bool maximizer, int& posible);
void copyBoard(const char* source, char* destination);
int posible;

int main(){
    srand(time(0));
    char marked[9] = {
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ',
    };
    //POINTER
    char *pMarked = marked;
    int pin;
    int row = 1;

    boardvisual(pMarked);
    do{

        ComputerMove(pMarked,0,posible);
        std::cout << posible - 2 << " Outcome dicek" << "\n";
        if (winningcondition(pMarked) != 20){
            printingwinner(winningcondition(pMarked),pMarked);
            break;
        }
        std::cout << "X : masukan kolom : "; std::cin >> pin;
        drawXvisual(pMarked, pin );
        if (winningcondition(pMarked) != 20){
            printingwinner(winningcondition(pMarked),pMarked);
            break;
        }

        }while(true);
    return 0;
}

void boardvisual(const char *marked){
    using namespace std;
    cout << " -----------------\n";
    cout << "|  " <<marked[0]<< "  |" << "  " <<marked[1]<< "  " << "|  " <<marked[2]<< "  |\n";
    cout << "|-----|-----|-----|\n";
    cout << "|  " <<marked[3]<< "  |" << "  " <<marked[4]<< "  " << "|  " <<marked[5]<< "  |\n";
    cout << "|-----|-----|-----|\n";
    cout << "|  " <<marked[6]<< "  |" << "  " <<marked[7]<< "  " << "|  " <<marked[8]<< "  |\n";
    cout << " -----------------\n";

}
void drawXvisual(char* pmarked, int row){
    pmarked[row-1] = 'X';
    system("cls");
    boardvisual(pmarked);
}
void ComputerMove(char* pmarked, int row,int& posible){
    int bestmove = INT_MIN;
    int move = -1;
    pmarked[move] = 'O';
    system("cls");
    boardvisual(pmarked);
    posible = 0;

    for(int i =  0  ; i < 9 ; i++){
        if(pmarked[i] == ' '){
            pmarked[i] = 'O';
            int temp = minimax(pmarked, 0 , false, posible);
            pmarked[i] = ' ';
                if (temp > bestmove){
                    bestmove = temp;
                    move = i;
                }
            }
        }
        pmarked[move] = 'O';
        system("cls");
        boardvisual(pmarked);

}

int winningcondition(const char *pMarked){

    //horizontal
    if ((pMarked[0] == 'X' && pMarked[1] == 'X' && pMarked[2] == 'X') || 
        (pMarked[3] == 'X' && pMarked[4] == 'X' && pMarked[5] == 'X') || 
        (pMarked[6] == 'X' && pMarked[7] == 'X' && pMarked[8] == 'X')  )
        {return -10;}
        

    //vertical
    if((pMarked[0] == 'X' && pMarked[3] == 'X' && pMarked[6] == 'X')||
        (pMarked[1] == 'X' && pMarked[4] == 'X' && pMarked[7] == 'X')||
        (pMarked[2] == 'X' && pMarked[5] == 'X' && pMarked[8] == 'X'))
        {return -10;}

    //diagonal
    if((pMarked[0] == 'X' && pMarked[4] == 'X' && pMarked[8] == 'X')||
            (pMarked[2] == 'X' && pMarked[4] == 'X' && pMarked[6] == 'X'))
        {return -10;}

    //horizontal
    if ((pMarked[0] == 'O' && pMarked[1] == 'O' && pMarked[2] == 'O') || 
        (pMarked[3] == 'O' && pMarked[4] == 'O' && pMarked[5] == 'O') || 
        (pMarked[6] == 'O' && pMarked[7] == 'O' && pMarked[8] == 'O')  )
        {return 10;}

    //vertical
    if((pMarked[0] == 'O' && pMarked[3] == 'O' && pMarked[6] == 'O')||
        (pMarked[1] == 'O' && pMarked[4] == 'O' && pMarked[7] == 'O')||
        (pMarked[2] == 'O' && pMarked[5] == 'O' && pMarked[8] == 'O'))
        {return 10;}

    //diagonal
    if((pMarked[0] == 'O' && pMarked[4] == 'O' && pMarked[8] == 'O')||
        (pMarked[2] == 'O' && pMarked[4] == 'O' && pMarked[6] == 'O'))
        {return 10;}
        
    if ((pMarked[0] == 'X' || pMarked[0] == 'O') && (pMarked[1] == 'X' || pMarked[1] == 'O') && 
        (pMarked[2] == 'X' || pMarked[2] == 'O') &&(pMarked[3] == 'X' || pMarked[3] == 'O') && 
        (pMarked[4] == 'X' || pMarked[4] == 'O') && (pMarked[5] == 'X' || pMarked[5] == 'O') &&
        (pMarked[6] == 'X' || pMarked[6] == 'O') && (pMarked[7] == 'X' || pMarked[7] == 'O') && 
        (pMarked[8] == 'X' || pMarked[8] == 'O'))
        {return 0;}


    return 20;
}
void printingwinner(int wincon, const char* pMarked){
        if (winningcondition(pMarked) == 1){
            std::cout << "Hore Player Win : ) ";
        }
        else if (winningcondition(pMarked)== -1){
            std::cout << "shit the com win, we have a terminator problem : ) ";
        }
        else if (winningcondition(pMarked)== 0){
            std::cout << "Draw duh";
        }
}

void copyBoard(const char* source, char* destination) {
    for (int i = 0; i < 9; ++i) {
        destination[i] = source[i];
    }
}

int minimax(char *pmarked,int depth,bool maximizer, int& posible){
    int wincon = winningcondition(pmarked);
    int count = 0;
    if (wincon != 20){
        posible ++;
        return winningcondition(pmarked) + depth;
    }
    
    if (maximizer){

        int bestposible = INT_MIN;
        for (int i = 0; i < 9 ; i++){
            if(pmarked[i] == ' '){
                pmarked[i] = 'O';
                bestposible = std::max(bestposible,minimax(pmarked,depth + 1, !maximizer,posible));
                pmarked[i] = ' ';
                }
            }
        return bestposible;
        }
    else{

        int bestposible = INT_MAX;
        for (int i = 0; i < 9 ; i++){
            if(pmarked[i] == ' '){
                pmarked[i] = 'X';
                bestposible = std::min(bestposible,minimax(pmarked,depth + 1, maximizer,posible));
                pmarked[i] = ' ';
                }
        }
        return bestposible;
    }


    
}
    
