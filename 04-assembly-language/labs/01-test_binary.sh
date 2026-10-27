#!/bin/bash

check_test() {
    input="$1"
    expected="$2"

    output=$(printf "%s\n" "$input" | ./01-binary-to-decimal)
    actual=$(printf "%s\n" "$output" | grep "Decimal =" | awk '{print $3}')

    if [ "$actual" = "$expected" ]; then
        echo "PASS: $input -> $expected"
    else
        echo "FAIL: $input -> expected $expected, got $actual"
    fi
}

check_test "0000000000000000" 0
check_test "0000000000000001" 1
check_test "0000000000001010" 10
check_test "0000000000011011" 27
check_test "1111111111111111" 65535
check_test "1000000000000000" 32768