
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
 * @brief depth first search to find the word
 * @param board: A list of pair coordinates to check for the next move in s
 * @param s: The string to check for
 * @param board: A map of the board to check for the next move in s
 * @param path: The path taken so far, do not repeat
 * @param boardKeys: The keys of the board, used to find adjacent points
 * @return: A boolean indicating if the string can be found on the board
 */
bool dfs(set<pairs> &points, string s, map<pairs, char> &board, set<pairs> &path, set<pairs> &boardKeys)
{
    // cout << s << ' ';
    // for (auto it = points.begin(); it != points.end(); it++)
    // {
    //     cout << '(' << it->first << ',' << it->second << ") ";
    // }
    // cout << endl;
    if (s.length() == 0)
        return true;
    for (auto it = points.begin(); it != points.end(); it++)
    {
        // cout << "checking " << it->first << ',' << it->second << " '" << board[*it] << endl;
        if (board[*it] == s[0])
        {
            path.insert(*it);
            // find all points that are adjacent to it LRUD
            set<pairs> adj;
            adj.insert(pairs(it->first - 1, it->second));
            adj.insert(pairs(it->first + 1, it->second));
            adj.insert(pairs(it->first, it->second - 1));
            adj.insert(pairs(it->first, it->second + 1));
            // find the intersection of adj and all possible points on the board
            set<pairs> intersection;
            // get the keyset of board
            set_intersection(adj.begin(), adj.end(), boardKeys.begin(), boardKeys.end(), inserter(intersection, intersection.begin()));
            // remove the points that are already in the path
            set<pairs> new_points;
            set_difference(intersection.begin(), intersection.end(), path.begin(), path.end(), inserter(new_points, new_points.begin()));
            if (dfs(new_points, s.substr(1), board, path, boardKeys))
                return true;
            path.erase(*it);
        }
    }
    return false;
}

class Solution
{
public:
    bool exist(vector<vector<char>> &board, string word)
    {
        set<pairs> points;
    set<pairs> boardKeys;
    map<pairs, char> board_map;
    map<char, int> board_char_count;
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

    return dfs(points, word, board_map, path, boardKeys);
    }
};