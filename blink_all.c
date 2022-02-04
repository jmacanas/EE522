#include <bcm2835.h>
#include <stdio.h>
 
// Blinks on RPi Plug P1 pin 11 (which is GPIO pin 17)
#define PIN0 RPI_BPLUS_GPIO_J8_03
#define PIN1 RPI_BPLUS_GPIO_J8_05
#define PIN2 RPI_BPLUS_GPIO_J8_07
#define PIN3 RPI_BPLUS_GPIO_J8_08
#define PIN4 RPI_BPLUS_GPIO_J8_10
#define PIN5 RPI_BPLUS_GPIO_J8_11
#define PIN6 RPI_BPLUS_GPIO_J8_12
#define PIN7 RPI_BPLUS_GPIO_J8_13
#define PIN8 RPI_BPLUS_GPIO_J8_15
#define PIN9 RPI_BPLUS_GPIO_J8_16
#define PIN10 RPI_BPLUS_GPIO_J8_18
#define PIN11 RPI_BPLUS_GPIO_J8_19
#define PIN12 RPI_BPLUS_GPIO_J8_21
#define PIN13 RPI_BPLUS_GPIO_J8_22
#define PIN14 RPI_BPLUS_GPIO_J8_23
#define PIN15 RPI_BPLUS_GPIO_J8_24
#define PIN16 RPI_BPLUS_GPIO_J8_26
#define PIN17 RPI_BPLUS_GPIO_J8_29
#define PIN18 RPI_BPLUS_GPIO_J8_31
#define PIN19 RPI_BPLUS_GPIO_J8_32
#define PIN20 RPI_BPLUS_GPIO_J8_33
#define PIN21 RPI_BPLUS_GPIO_J8_35
#define PIN22 RPI_BPLUS_GPIO_J8_36
#define PIN23 RPI_BPLUS_GPIO_J8_37
#define PIN24 RPI_BPLUS_GPIO_J8_38
#define PIN25 RPI_BPLUS_GPIO_J8_40
 
int main(int argc, char **argv)
{
    if (!bcm2835_init())
      return 1;
 
    // configure all pins as outputs.
    bcm2835_gpio_fsel(PIN0, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN1, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN2, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN3, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN4, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN5, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN6, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN7, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN8, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN9, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN10, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN11, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN12, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN13, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN14, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN15, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN16, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN17, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN18, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN19, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN20, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN21, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN22, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN23, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN24, BCM2835_GPIO_FSEL_OUTP);
    bcm2835_gpio_fsel(PIN25, BCM2835_GPIO_FSEL_OUTP);
    // Blink
    while (1)
    {
        // set all pins high
        bcm2835_gpio_write(PIN0, HIGH);
        bcm2835_gpio_write(PIN1, HIGH);
        bcm2835_gpio_write(PIN2, HIGH);
        bcm2835_gpio_write(PIN3, HIGH);
        bcm2835_gpio_write(PIN4, HIGH);
        bcm2835_gpio_write(PIN5, HIGH);
        bcm2835_gpio_write(PIN6, HIGH);
        bcm2835_gpio_write(PIN7, HIGH);
        bcm2835_gpio_write(PIN8, HIGH);
        bcm2835_gpio_write(PIN9, HIGH);
        bcm2835_gpio_write(PIN10, HIGH);
        bcm2835_gpio_write(PIN11, HIGH);
        bcm2835_gpio_write(PIN12, HIGH);
        bcm2835_gpio_write(PIN13, HIGH);
        bcm2835_gpio_write(PIN14, HIGH);
        bcm2835_gpio_write(PIN15, HIGH);
        bcm2835_gpio_write(PIN16, HIGH);
        bcm2835_gpio_write(PIN17, HIGH);
        bcm2835_gpio_write(PIN18, HIGH);
        bcm2835_gpio_write(PIN19, HIGH);
        bcm2835_gpio_write(PIN20, HIGH);
        bcm2835_gpio_write(PIN21, HIGH);
        bcm2835_gpio_write(PIN22, HIGH);
        bcm2835_gpio_write(PIN23, HIGH);
        bcm2835_gpio_write(PIN24, HIGH);
        bcm2835_gpio_write(PIN25, HIGH);
        
        // wait 0.5seconds
        bcm2835_delay(500);
        
        // turn it off
        bcm2835_gpio_write(PIN0, LOW);
        bcm2835_gpio_write(PIN1, LOW);
        bcm2835_gpio_write(PIN2, LOW);
        bcm2835_gpio_write(PIN3, LOW);
        bcm2835_gpio_write(PIN4, LOW);
        bcm2835_gpio_write(PIN5, LOW);
        bcm2835_gpio_write(PIN6, LOW);
        bcm2835_gpio_write(PIN7, LOW);
        bcm2835_gpio_write(PIN8, LOW);
        bcm2835_gpio_write(PIN9, LOW);
        bcm2835_gpio_write(PIN10, LOW);
        bcm2835_gpio_write(PIN11, LOW);
        bcm2835_gpio_write(PIN12, LOW);
        bcm2835_gpio_write(PIN13, LOW);
        bcm2835_gpio_write(PIN14, LOW);
        bcm2835_gpio_write(PIN15, LOW);
        bcm2835_gpio_write(PIN16, LOW);
        bcm2835_gpio_write(PIN17, LOW);
        bcm2835_gpio_write(PIN18, LOW);
        bcm2835_gpio_write(PIN19, LOW);
        bcm2835_gpio_write(PIN20, LOW);
        bcm2835_gpio_write(PIN21, LOW);
        bcm2835_gpio_write(PIN22, LOW);
        bcm2835_gpio_write(PIN23, LOW);
        bcm2835_gpio_write(PIN24, LOW);
        bcm2835_gpio_write(PIN25, LOW);
        
        // wait a bit
        bcm2835_delay(500);
    }
    bcm2835_close();
    return 0;
}
