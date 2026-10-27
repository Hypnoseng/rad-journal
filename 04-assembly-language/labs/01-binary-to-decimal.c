#include <stdio.h>

int main(int argc, char const* argv[]) {
  char binary[17];
  unsigned int value = 0;

  // 0000000000011011 , 0000000000000001 , 1111000011110000 

  printf("Enter 16-bit binary: ");
  scanf("%16s", binary);

  printf("%-8s | %-10s | %s\n", "digit", "old value", "calculation");

  unsigned int old_value = 0;

  for (int i = 0; i < 16; i++) {
    int digit = binary[i] - '0';

    old_value = value;
    value = old_value * 2 + digit;  // value_new = value_old * 2 + digit

    printf("%-8d | %-10u | %u * 2 + %d = %u\n", digit, old_value, old_value,digit, value);
  }

  printf("Decimal = %u\n", value);
  return 0;
}
