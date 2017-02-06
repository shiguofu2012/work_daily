#include<stdio.h>
#include<stdlib.h>
#include<sys/time.h>

int count_bits(int num)
{
    int ret = 0;
    while(num != 0)
    {
        if(num % 2 != 0)
            ret += 1;
        num /= 2;
    }
    return ret;
}

inline int count_bits_1(int num)
{
    int ret = 0;
    while(num != 0)
    {
        num = num & (num - 1);
        ret++;
    }
    return ret;
}

int count_bits_2(int num)
{

}

int main(int args, char **argv)
{
    int a = 15;
    unsigned int i;
    int ret[16] = {0};
    struct timeval start, end;
    gettimeofday(&start, NULL);
    /*for(i = 0; i <= a; i++)*/
    /*{*/
        /*ret[i] = count_bits_1(i);*/
    /*}*/
    ret[0] = 0;
    for(i = 1; i <= a; i++)
    {
        printf("(i: %d, ret[%d]:%d  %d&1:%d)", i, i>>1, ret[i>>1], i, i & 1);
        ret[i] = ret[i>>1] + (int)(i & 1);
    }
    printf("\n");
    for(i = 0; i <= a; i++)
    {
        printf("%d\t", ret[i]);
    }
    gettimeofday(&end, NULL);
    printf("%ldus", (end.tv_usec - start.tv_usec) / 1000);

    return 0;
}
