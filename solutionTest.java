import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class solutionTest {

    @Test
    void test0() {
        char[][] a = {{'A','S','E','R'},
                      {'Y','U','T','O'},
                      {'G','H','I','L'}};
        String word = "SEROLITUHGYA";
        assertTrue(main.solution(word, a));
    }

    @Test
    void test1() {
        char[][] a = {{'A','S','E','R'},
                      {'Y','U','T','O'},
                      {'G','H','I','L'}};
        String word = "ASER";
        assertTrue(main.solution(word, a));
    }

    @Test
    void test2() {
        char[][] a = {{'A','S','E','R'},
                {'Y','U','T','O'},
                {'G','H','I','L'}};
        String word = "CAT";
        assertFalse(main.solution(word, a));
    }

    @Test
    void test3() {
        char[][] a = {{'A','A','A','A'},
                      {'A','T','A','A'},
                      {'A','A','B','A'}};
        String word = "BAT";
        assertTrue(main.solution(word, a));
    }

    @Test
    void test4() {
        char[][] a = {{'A','A','A','A'},
                      {'T','A','A','A'},
                      {'A','A','B','A'}};
        String word = "BAT";
        assertFalse(main.solution(word, a));
    }

    @Test
    void test5() {
        char[][] a = {{'A','A','A','A'},
                      {'T','A','A','A'},
                      {'A','A','B','A'}};
        String word = "BAAT";
        assertTrue(main.solution(word, a));
    }

    @Test
    void test6() {
        char[][] a = {{'T','T','A','T'},
                      {'T','A','B','A'},
                      {'T','T','A','T'}};
        String word = "BAT";
        assertTrue(main.solution(word, a));
    }

    @Test
    void test7() {
        char[][] a = {{'A','S','E','R'},
                {'Y','U','T','O'},
                {'G','H','I','L'}};
        String word = "AYA";
        assertFalse(main.solution(word, a));
    }

    @Test
    void test8() {
        char[][] a = {{'A','S','E','R'},
                {'Y','U','T','O'},
                {'G','H','I','L'}};
        String word = "ASA";
        assertFalse(main.solution(word, a));
    }

    @Test
    void test9() {
        char[][] a = {{'A','S','E','R'},
                {'Y','U','T','O'},
                {'G','H','I','L'}};
        String word = "SER";
        assertTrue(main.solution(word, a));
    }

    @Test
    void test10() {
        char[][] a = {{'A','S','A','R'},
                {'Y','U','T','O'},
                {'G','H','I','L'}};
        String word = "AR";
        assertTrue(main.solution(word, a));
    }

    @Test
    void test11() {
        char[][] a = {{'A','F','U','S'},
                {'D','U','Y','I'},
                {'F','N','M','P'}};
        String word = "FUN";
        assertTrue(main.solution(word, a));
    }
}