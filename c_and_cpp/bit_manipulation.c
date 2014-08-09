
#include <stdio.h>

void displayBits(unsigned);

int main(){
  unsigned num = 960;
  printf("\n The result of left shifting\n");
  displayBits(num);
  printf("8 bit position using the left shift operator << is\n");
  displayBits(num<<8);
  
  printf("The result of right shifting\n");
  displayBits(num);
  printf("8 bit position using the right shift operator >> is\n");
  displayBits(num>>8);

  return 0;
}

void displayBits(unsigned value){
  unsigned c, displayMask = 1 << 15;
  printf("%7u = ", value);
  
  for(c=1; c<=16; c++){
    putchar(value & displayMask ? '1' : '0');
    value <<= 1;
    
    if( c%8 == 0)
      putchar(' ');
  }//For
  putchar('\n');
}//displayBits

short getBit(unsigned value, unsigned i){
  unsigned ret = 0;
  if ((value & (1 << i)) != 0)
    ret = 1;
  
  return ret;
}


