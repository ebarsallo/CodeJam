/************************************************************************/
/* Cracking the Code Interview, Chapter 5, Examples			*/
/* Date created: 2014.08.03 	         				*/
/* File: bit_manipulation.c 						*/
/************************************************************************/
#include <stdio.h>

void displayBits(unsigned);
short getBit(unsigned value, unsigned i);
unsigned setBit(unsigned value, unsigned i);
unsigned clearBit(unsigned value, unsigned i);
unsigned clearBitsMSBthrough0(unsigned value, unsigned i);
unsigned updateBit(unsigned value, unsigned i, unsigned v);

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

  printf("Getting i Bit from value\n");
  displayBits(num);
  printf("8th bit position is: ");
  if(getBit(num,8)==0)
    printf("0\n");
  else 
    printf("1\n");

  printf("Setting ith Bit to value\n");
  displayBits(num);
  printf("setting 5th bit is: ");
  displayBits(setBit(num,5));

  printf("Clearing ith Bit to value\n");
  displayBits(num);
  printf("Clearing 5th bit is: ");
  displayBits(clearBit(num,5));

  printf("Clearing all bits from the most sig bit through i\n");
  displayBits(num);
  printf("Clearing 8th bits is: ");
  displayBits(clearBitsMSBthrough0(num,8));

  return 0;
}

/************************************************************************/
/* Displaying number in bit's format                                    */
/************************************************************************/

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

/************************************************************************/
/* Getting ith bit from unsigned number                                 */
/************************************************************************/

short getBit(unsigned value, unsigned i){
  unsigned ret = 0;
  if ( (value & (1 << i)) != 0 )
    ret = 1;
  
  return ret;
}

/************************************************************************/
/* Setting ith bit from unsigned number                                 */
/************************************************************************/
unsigned setBit(unsigned value, unsigned i){
  return value | (1 << i);
}

/************************************************************************/
/* Setting ith bit to zero                                              */
/************************************************************************/

unsigned clearBit(unsigned value, unsigned i){
  return value & (~(1 << i));
}


/************************************************************************/
/* Clearing set of bits to zero                                         */
/************************************************************************/
unsigned clearBitsMSBthrough0(unsigned value, unsigned i){
  unsigned mask = (1 << i) - 1;
  return value & mask;
}

unsigned updateBit(unsigned value, unsigned i, unsigned v){
  unsigned mask = ~(1 << i);
  return (value & mask) | (v << i);
}
