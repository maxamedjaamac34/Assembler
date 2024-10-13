// Write a program that draws a rectangle, with a width of
// 16 pixels, and a height of @R0 pixels.

// Initialize @height (target height) to @R0
@R0
D=M
@height
M=D

// Initialize counter to 0
@0
D=A
@counter
M=D

// Initialise screen address
@SCREEN
D=A
@address
M=D

(LOOP)

  // Point to the correct place in screen memory
  // and draw a black line
  @address
  A=M
  M=-1

  // Increase counter by 1 (we have draw a 32 pixel line)
  // Increase address by 32 (to advance to the next line)
  @counter
  M=M+1
  @32
  D=A
  @address
  M=M+D

  // Check to see if we have drawn enough lines
  // by comparing height and counter
  @height
  D=M
  @counter
  D=D-M
  @END
  D;JEQ

  @LOOP
  0;JMP

(END)
  @END
  0;JMP
