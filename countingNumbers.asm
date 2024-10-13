
//counting the number of -1 in the array of 50 elements

I = 100   // Set the value of register I to 100 (address of the array)
D = A   // Copy the value in register A to register D (initialize counter)
@I //   Jump to the memory address stored in register I (start of the array)
M = D   // Store the value in register D in the memory address (store counter)
@50 // Jump to memory address 50 (end of the array)
D = A // Copy the value in register A to register D (reset counter)
@n // Jump to the memory address stored in register n (next element in the array)
M = D // Store the value in register D in the memory address (store counter)
@C // Jump to the memory address stored in register C (counter for 4s)
M = 0 // Store the value 0 in the memory address (initialize 4s counter)
@I // Jump to the memory address stored in register I (start of the array)
A = M // Copy the value in memory address to register A (load current element)
D = M // copy the value of memory to register D 
@1 // Jump to memory address 1 (value to compare)
D = D + A // Subtract the value in register A from the value in register D (compare current element to 1)
@A negative_one // Jump to label "negative_one" if the result is 0 (current element is -1)
D; JEQ // Jump if equal to 0
@continue // Jump to label "continue" if not equal
0; JMP // Jump to address 0 (not used, but required for syntax)
(A negative_one) // Label for when current element is -1
@R0 // Jump to memory address stored in register R0 (not used, but required for syntax)
M = M + 1 // Increment the value in memory address (increment -1s counter)
(continue) // Label for continuing the loop
@C // Jump to the memory address stored in register C (counter for -1s)
M = M + 1 // Increment the value in memory address (increment loop counter)
@I // Jump to the memory address stored in register I (start of the array)
A = M // Copy the value in memory address to register A (load next element)
A = A + D // Add the value in register D to the value in register A (increment array index) - the A does not change
M = A // Store the value in register A in the memory address (store next element index)
@loop // Jump to label "loop" to continue the loop
0; JEQ // Jump if equal to 0 (not used, but required for syntax)








//initialize array

@100
D = A
@array //(array = 100) (@16)
M = D 
@50
D = A
@size  //(size = 50) (@17)
M = D
@0
D = A
@element //(element = 0) (@18)
M = D

@found (found = 0)
M = D

//loop through the array and look for -1s

(loop)
@element
D = M 
@array 
A = D + M

D = M
D = D+1
@MINUSONE
D;JEQ

@NEXT
0;JMP

(MINUSONE)
@found //update the counter
M = M+1

(NEXT)
@size
D = M
@element
M = M+1
D = M-D
@EXIT
D;JGE
@LOOP
0;JMP
(EXIT)
D=M
@R0
M=D
(END)
0;JMP



