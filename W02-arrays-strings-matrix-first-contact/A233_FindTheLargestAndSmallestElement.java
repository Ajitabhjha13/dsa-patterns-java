
// File: W02-arrays-strings-matrix-first-contact/A233_FindTheLargestAndSmallestElement.java
/*
 * Problem : Find the largest and smallest element.
 * Plan ID : A233 | P1 · W2 · Day 8 · 22 Oct
 * Source  : Warm-up + Striver + Babbar
 * Link    : https://www.google.com/search?q=takeuforward+Largest+Element
 * Level   : Basic
 * Status  : Solved
 *
 * Approach:
 *   Pehle element ko max aur min dono maan lo.
 *   Baaki array ek baar traverse karo: bada mila toh max update,
 *   chhota mila toh min update. Sorting ki zaroorat nahi (wo O(n log n) hota).
 *
 * Time : O(n)    Space : O(1)
 * Galti: max/min ko 0 se start karna galat hai — saare numbers negative
 *        hon toh max 0 aa jayega. Isliye arr[0] se start kiya.
 */
import java.util.Scanner;

class A233_FindTheLargestAndSmallestElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int max = arr[0];
        int min = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > max)
                max = arr[i];
            if (arr[i] < min)
                min = arr[i];
        }

        System.out.println("Largest: " + max);
        System.out.println("Smallest: " + min);
        sc.close();
    }
}