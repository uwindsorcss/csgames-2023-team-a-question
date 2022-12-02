
// include sets
#include <set>
#include <map>
#include <iterator>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;
typedef pair<int, int> pairs;
typedef unsigned int uint;

/**
 * @brief depth first search to find the word. For each potential point, we recursively scheck valid next points that are not visited yet.
 * @param board: A list of pair coordinates to check for the next move in s
 * @param s: The string to check for
 * @param board: A map of the board to check for the next move in s
 * @param path: The path taken so far, do not repeat
 * @param boardKeys: The keys of the board, used to find adjacent points
 * @return: A boolean indicating if the string can be found on the board
 */
bool dfs(set<pairs> &points, string s, map<pairs, char> &board, set<pairs> &path, set<pairs> &boardKeys)
{
    if (s.length() == 0)
        return true;
    for (auto it : points)
    {
        if (board[it] == s[0])
        {
            path.insert(it);
            set<pairs> adj;
            adj.insert(pairs(it.first - 1, it.second));
            adj.insert(pairs(it.first + 1, it.second));
            adj.insert(pairs(it.first, it.second - 1));
            adj.insert(pairs(it.first, it.second + 1));
            set<pairs> intersection;
            set_intersection(adj.begin(), adj.end(), boardKeys.begin(), boardKeys.end(), inserter(intersection, intersection.begin()));
            set<pairs> new_points;
            set_difference(intersection.begin(), intersection.end(), path.begin(), path.end(), inserter(new_points, new_points.begin()));
            if (dfs(new_points, s.substr(1), board, path, boardKeys))
                return true;
            path.erase(it);
        }
    }
    return false;
}

bool exist(vector<vector<char>> &board, string word)
{
    // reverse the word
    string rword = word;
    reverse(rword.begin(), rword.end());

    set<pairs> points;               // points to check for the next move
    set<pairs> boardKeys;            // keys of the board, for checking for valid adjacent points
    map<pairs, char> board_map;      // coordinate -> char map of the board
    map<char, int> board_char_count; // char -> count map of the board
    for (uint i = 0; i < board.size(); i++)
    {
        for (uint j = 0; j < board[i].size(); j++)
        {
            points.insert(make_pair(i, j));
            board_map[make_pair(i, j)] = board[i][j];
            boardKeys.insert(make_pair(i, j));
            if (board_char_count.find(board[i][j]) == board_char_count.end())
                board_char_count[board[i][j]] = 1;
            else
                board_char_count[board[i][j]]++;
        }
    }
    set<pairs> path;

    map<char, int> word_char_count;
    for (uint i = 0; i < word.length(); i++)
    {
        if (word_char_count.find(word[i]) == word_char_count.end())
            word_char_count[word[i]] = 1;
        else
            word_char_count[word[i]]++;
    }

    // check the case where any character in the word does not appear on the board
    for (uint i = 0; i < word.size(); i++)
    {
        if (board_char_count.find(word[i]) == board_char_count.end())
            return false;
        else if (board_char_count[word[i]] < word_char_count[word[i]])
            return false;
    }

    // use word if the first character has less occurences than the reverse of the word
    if (board_char_count[word[0]] > board_char_count[rword[0]])
        word = rword;

    return dfs(points, word, board_map, path, boardKeys);
}

int main(void)
{
    // assume input comes from stdin
    // board input is single characters, space separated for columns and newlines for rows
    // word is on its own line
    // example input:
    // ```
    // A B C E
    // S F C S
    // A D E E
    // word
    // ```

    // read board and word
    vector<vector<char>> board = {{'A', 'A', 'A', 'A', 'A', 'A'},
                                  {'A', 'A', 'A', 'A', 'A', 'A'},
                                  {'A', 'A', 'A', 'A', 'A', 'A'},
                                  {'A', 'A', 'A', 'A', 'A', 'A'},
                                  {'A', 'A', 'A', 'A', 'A', 'B'},
                                  {'A', 'A', 'A', 'A', 'B', 'A'}};

    string word = "AAAAAAAAAAAAABB";

    // print the board and word
    cout << "Board:" << endl;
    for (uint i = 0; i < board.size(); i++)
    {
        for (uint j = 0; j < board[i].size(); j++)
        {
            cout << board[i][j];
        }
        cout << endl;
    }
    cout << "Word: " << word << endl;

    // print result
    cout << exist(board, word) << endl;
}
