
# DC4 Codefights 2024 Solutions

## Warm-up Round

### Challenge 1

#### Problem Statement
Employees are required to update their passwords periodically. However, some employees accidentally enable the Caps Lock key while typing their passwords, causing all characters to be altered.

A password typed with the Caps Lock key accidentally enabled may exhibit one of the following characteristics:
1. All characters are uppercase.
2. All characters are uppercase except the first character, which is lowercase.

In such cases, we need to correct the password by toggling the case of all characters (uppercase to lowercase and vice versa). If the password is unaffected by the Caps Lock issue, it should remain unchanged.

#### Approach and Solution
We need to determine whether a given password was typed with the Caps Lock key accidentally enabled. If so, we toggle the case of all characters. Otherwise, the password remains as is.

To identify such a password, we use the following rules:
1. The password consists of all uppercase letters.
2. The password consists of all uppercase letters except the first one, which is lowercase.

Special cases include passwords containing a single character. Regardless of whether it's uppercase or lowercase, it satisfies both conditions and must be toggled.

Instead of examining the first character, focus on characters starting from the second position. If all these characters are uppercase, the password qualifies as having been typed with Caps Lock enabled. If any lowercase character is found, the password does not require correction.

#### Optimization
To toggle the case of each character efficiently, we use bit manipulation:
- XOR the character with `0x20` (space character in ASCII).

**Explanation:**
- The ASCII code for the space character (`0x20`) is `0010 0000`.
- XORing any character with `0x20` flips the 6th bit.
- Uppercase and lowercase letters differ by exactly `0x20` in ASCII. For example:
  - `A` = `0100 0001`
  - `a` = `0110 0001`
  - XORing `A` with `0x20` yields `a`, and vice versa.

This method is faster and avoids manual comparisons.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
Where `n` is the length of the password string.

---

### Java Implementation

```java
public class PasswordCorrection {
    public static String correctPassword(String password) {
        int n = password.length();
        if (n == 1) {
            return toggleCase(password);
        }
        
        boolean capsLockMode = true;
        for (int i = 1; i < n; i++) {
            if (Character.isLowerCase(password.charAt(i))) {
                capsLockMode = false;
                break;
            }
        }
        
        return capsLockMode ? toggleCase(password) : password;
    }
    
    private static String toggleCase(String str) {
        char[] chars = str.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            chars[i] ^= 0x20; // Flip the 6th bit to toggle case
        }
        return new String(chars);
    }
    
    public static void main(String[] args) {
        System.out.println(correctPassword("cAPSLOCK")); // Output: Capslock
        System.out.println(correctPassword("CAPSLOCK")); // Output: capslock
        System.out.println(correctPassword("CapsLock")); // Output: CapsLock
    }
}
```
