/*
 * Problem : Print FizzBuzz from 1 to N
 * Plan ID : A88 | P1 · W1 · Day 1 · 15 Oct
 * Source  : Warm-up
 * Link    : https://leetcode.com/problems/fizz-buzz/
 * Level   : Basic
 * Status  : Solved
 *
 * Approach:
 *   Loop 1..N. Check divisibility by 15 first (both 3 and 5),
 *   then 3, then 5, else print the number.
 *
 * Time : O(N)    Space : O(1)
 * Mistake: checked % 3 before % 15, so 15 printed "Fizz".
 */
import java.util.Scanner;

class A88_PrintFizzBuzzFrom1ToN {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) System.out.println("FizzBuzz");
            else if (i % 3 == 0) System.out.println("Fizz");
            else if (i % 5 == 0) System.out.println("Buzz");
            else System.out.println(i);
        }
        sc.close();
    }
}
